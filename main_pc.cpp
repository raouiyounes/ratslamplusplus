/*
 * openRatSLAM
 *
 * utils - General purpose utility helper functions mainly for angles and readings settings
 *
 * Copyright (C) 2012
 * David Ball (david.ball@qut.edu.au) (1), Scott Heath (scott.heath@uqconnect.edu.au) (2)
 *
 * RatSLAM algorithm by:
 * Michael Milford (1) and Gordon Wyeth (1) ([michael.milford, gordon.wyeth]@qut.edu.au)
 *
 * 1. Queensland University of Technology, Australia
 * 2. The University of Queensland, Australia
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */
#include <iostream>
#include "utils/utils.h"
#include <fstream>
#include <boost/property_tree/ini_parser.hpp>
#include <ros/ros.h>
#include "ratslam/posecell_network.h"
#include <ratslam_ros/TopologicalAction.h>
#include<ratslam_ros/signalFromCNN.h>
#include <nav_msgs/Odometry.h>
#include <ratslam_ros/ViewTemplate.h>
#include <ratslam_ros/GraphObjectTemplate.h>
#include <ratslam_ros/weights.h>

#include <fstream>
#if HAVE_IRRLICHT
#include "graphics/posecell_scene.h"
ratslam::PosecellScene *pcs;
bool use_graphics;
#endif
typedef double Posecell;

using namespace std;
using namespace ratslam;

ofstream pose_of_my_robot("poses_my_robot.txt");
ofstream file_for_time("time.txt");
ratslam_ros::TopologicalAction pc_output;


static void odo_callback(nav_msgs::OdometryConstPtr odo, ratslam::PCN_tmp *pc, ros::Publisher * pub_pc,ros::Publisher * pub_whgts)
{

  ROS_DEBUG_STREAM("PC:odo_callback{" << ros::Time::now() << "} seq=" << odo->header.seq << " v=" << odo->twist.twist.linear.x << " r=" << odo->twist.twist.angular.z);
  static ros::Time prev_time(0);
  ratslam_ros::weights  wghts;
  if (prev_time.toSec() > 0)
  {
    double time_diff = (odo->header.stamp - prev_time).toSec();
    pc_output.src_id = pc->get_current_exp_id();
   pc->on_odo(odo->twist.twist.linear.x,odo->twist.twist.angular.z,time_diff);
   
   
 vector<vector<vector<float> > >weights;
weights=pc->getEnergy();


    pub_whgts->publish(wghts);
    pc_output.action = pc->get_action();

    if (pc_output.action != ratslam::PosecellNetwork::NO_ACTION)
    {
      pc_output.header.stamp = ros::Time::now();
      pc_output.header.seq++;
      pc_output.dest_id = pc->get_current_exp_id();
	  pc_output.relative_rad = pc->get_relative_rad();
	  pub_pc->publish(pc_output);
      ROS_DEBUG_STREAM("PC:action_publish{odo}{" << ros::Time::now() << "} action{" << pc_output.header.seq << "}=" <<  pc_output.action << " src=" << pc_output.src_id << " dest=" << pc_output.dest_id);
    }

/*
#ifdef HAVE_IRRLICHT
	if (use_graphics)
	{
		pcs->update_scene();
		pcs->draw_all();
	}
#endif
  */
//std::cout<<"x= :"<<pc->best_x<<"\n";
pose_of_my_robot<<pc->best_x<<" "<<pc->best_y<<" "<<pc->best_th<<endl;

std::cout<<"weights"<<pc->posecells[0][0][0];

}
  prev_time = odo->header.stamp;
  }


static void template_callback(ratslam_ros::GraphObjectTemplateConstPtr ot, ratslam::PosecellNetwork *pc, ros::Publisher * pub_pc	)
{
  ROS_DEBUG_STREAM("PC:ot_callback{" << ros::Time::now() << "} seq=" << ot->header.seq << " id=" << ot->current_id << " rad=" << ot->relative_rad);

  std::cout<<"current id: "<<ot->current_id<<" relative rad : "<<0.0<<"\n";
  if (pc->visual_templates.size()==ot->current_id)

  pc->on_view_template(ot->current_id, ot->relative_rad);
}


static void template_callbackv(ratslam_ros::ViewTemplateConstPtr vt, ratslam::PosecellNetwork *pc, ros::Publisher * pub_pc	)
{
  //ROS_DEBUG_STREAM("PC:vt_callback{" << ros::Time::now() << "} seq=" << vt->header.seq << " id=" << vt->current_id << " rad=" << vt->relative_rad);


  std::cout<<"current id: "<<vt->current_id<<" relative rad : "<<vt->relative_rad<<"\n";
  if (pc->visual_templates.size()==vt->current_id)
  pc->on_view_template(vt->current_id, vt->relative_rad);
	
/*
#ifdef HAVE_IRRLICHT
	if (use_graphics)
	{
		pcs->update_scene();
		pcs->draw_all();
	}
#endif
*/
}








int main(int argc, char * argv[])
{

  //ROS_INFO_STREAM(argv[0] << " - openRatSLAM Copyright (C) 2012 David Ball and Scott Heath");
  //ROS_INFO_STREAM("RatSLAM algorithm by Michael Milford and Gordon Wyeth");
  //ROS_INFO_STREAM("Distributed under the GNU GPL v3, see the included license file.");
  /*if (argc < 2)
  {
    ROS_FATAL_STREAM("USAGE: " << argv[0] << " <config_file>");
    exit(-1);
  }*/

    if (argc < 2)
    {
      ROS_FATAL_STREAM("USAGE: " << argv[0] << " <config_file>");
      exit(-1);
    }
    std::string topic_root = "";
    boost::property_tree::ptree settings, ratslam_settings, general_settings;
    read_ini(argv[1], settings);

    get_setting_child(ratslam_settings, settings, "ratslam", true);
    get_setting_child(general_settings, settings, "general", true);
    get_setting_from_ptree(topic_root, general_settings, "topic_root", (std::string) "");

    if (!ros::isInitialized())
    {
      ros::init(argc, argv, "RatSLAMPoseCells");
    }
    ros::NodeHandle node;

  ratslam::PCN_tmp * pc = new ratslam::PCN_tmp(ratslam_settings);

  ros::Publisher pub_pc = node.advertise<ratslam_ros::TopologicalAction>(topic_root+"/PoseCell/TopologicalAction", 0);
ros::Publisher pub_whgts = node.advertise<ratslam_ros::weights>("/weights", 0);

  ros::Subscriber sub_odometry = node.subscribe<nav_msgs::Odometry>(topic_root + "/odom", 0, boost::bind(odo_callback, _1, pc, &pub_pc,&pub_whgts), ros::VoidConstPtr(),
                                                                    ros::TransportHints().tcpNoDelay());

  ros::Subscriber sub_template = node.subscribe<ratslam_ros::ViewTemplate>(topic_root+"/LocalView/Template", 0, boost::bind(template_callbackv, _1, pc, &pub_pc),
                                                                       ros::VoidConstPtr(), ros::TransportHints().tcpNoDelay());


  ros::Subscriber sub_template_on=node.subscribe<ratslam_ros::GraphObjectTemplate>(topic_root+"/LocalObjectGraph/Template", 0, boost::bind(template_callback, _1, pc, &pub_pc),ros::VoidConstPtr(), ros::TransportHints().tcpNoDelay());

  /*
  #ifdef HAVE_IRRLICHT
  boost::property_tree::ptree draw_settings;
  get_setting_child(draw_settings, settings, "draw", true);
  get_setting_from_ptree(use_graphics, draw_settings, "enable", true);
  if (use_graphics)
  {
	pcs = new ratslam::PosecellScene(draw_settings, pc);
  }
#endif
*/
  ros::spin();

  return 0;
}
