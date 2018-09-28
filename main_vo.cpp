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
using namespace std;

#include "utils/utils.h"
#include "ratslam/visual_odometry.h"

#include <boost/property_tree/ini_parser.hpp>

#include <ros/ros.h>
#include <sensor_msgs/Image.h>
#include <sensor_msgs/CompressedImage.h>
#include <nav_msgs/Odometry.h>

#include <opencv2/opencv.hpp>
#include <opencv2/highgui/highgui.hpp>

#include <image_transport/image_transport.h>
#include <iostream>


#include <image_transport/image_transport.h>
#include <cv_bridge/cv_bridge.h>
#include <sensor_msgs/image_encodings.h>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <ratslam_ros/myViOdom.h>


using namespace std;
ratslam::VisualOdometry *vo = NULL;

ros::Publisher myPub_vo;
using namespace ratslam;
ratslam_ros::myViOdom odom_output;

//odom_output.mySeq=0;
void image_callback(sensor_msgs::ImageConstPtr image)
{
	
	cout<<"bbbbbbbbbbbbbb";
  ROS_DEBUG_STREAM("VO:image_callback{" << ros::Time::now() << "} seq=" << image->header.seq);
std::cout<<"i am in the v o";

/*
  static ratslam_ros::myViOdom odom_output;
cout<<"i am an image"<<image->height<<endl;


  vo->on_image(&image->data[0], (image->encoding == "bgr8" ? false : true), image->width, image->height, &odom_output.linVel, &odom_output.angVel);
cout<<"i am an image"<<image->height<<endl;


  //odom_output.myTimeSt = image->header.stamp;
  odom_output.mySeq++;

  myPub_vo.publish(odom_output);
  */
}


int main(int argc, char * argv[])
{
  ROS_INFO_STREAM(argv[0] << " - openRatSLAM Copyright (C) 2012 David Ball and Scott Heath");
  ROS_INFO_STREAM("RatSLAM algorithm by Michael Milford and Gordon Wyeth");
  ROS_INFO_STREAM("Distributed under the GNU GPL v3, see the included license file.");

  if (argc < 2)
  {
    ROS_FATAL_STREAM("USAGE: " << argv[0] << " <config_file>");
    exit(-1);
  }

  std::string topic_root = "";

  boost::property_tree::ptree settings, general_settings, vo_settings;
  read_ini(argv[1], settings);
  ratslam::get_setting_child(vo_settings, settings, "visual_odometry", true);
  ratslam::get_setting_child(general_settings, settings, "general", true);
  ratslam::get_setting_from_ptree(topic_root, general_settings, "topic_root", (std::string) "");

  vo = new ratslam::VisualOdometry(vo_settings);

  if (!ros::isInitialized())
  {
    ros::init(argc, argv, "RatSLAMVisualOdometry");
  }
  ros::NodeHandle node;

  myPub_vo  = node.advertise<ratslam_ros::myViOdom>("/visualOdomVel", 0);


  image_transport::ImageTransport it(node);
  image_transport::Subscriber sub = it.subscribe("/image_topic_2", 1, image_callback);

  ros::spin();

  return 0;
}
