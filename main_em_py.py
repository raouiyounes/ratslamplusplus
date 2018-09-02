#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Example Python node to listen on a specific topic.
"""

# Import required Python code.

import pdb
from geometry_msgs.msg import Point
from std_msgs.msg import  String
import rospy
import numpy as py
import math
import roslib
import sys
import ratslam.experience_map_younes
from nav_msgs.msg import Odometry
from geometry_msgs.msg import  PoseStamped
# Import custom message data.
from ratslam_ros.msg import NodeExampleData
from ratslam_ros.msg import TopologicalMap
from ratslam_ros.msg import TopologicalAction
from ratslam_ros.msg import TopologicalNode
from ratslam_ros.msg import TopologicalEdge
from visualization_msgs.msg import Marker
import geometry_msgs
import nav_msgs
from matplotlib import pyplot as plot
from bdb import set_trace
import Queue
counter = 0
timo=0
time_diff=0
prev_time=0
em_map=TopologicalMap()
global pub_goal_path
Topo=TopologicalAction()
pose_output=geometry_msgs.msg.PoseStamped()
topic_root=''

pub_pose=rospy.Publisher(topic_root+"/ExperienceMap/RobotPose",PoseStamped,queue_size=10)
pub_em=rospy.Publisher(topic_root+"/ExperienceMap/Map",TopologicalMap,queue_size=10)
em_marker=Marker()
pub_em_markers=rospy.Publisher(topic_root+'/ExperienceMap/MapMarker',Marker,queue_size=10)
pub_goal_path=rospy.Publisher(topic_root + "/ExperienceMap/PathToGoal",nav_msgs.msg.Path,queue_size=10)
file = open("em.dat","w") 
kidnaped_robot=False
kidnap_recoveryTime=rospy.Time()

#pdb.set_trace()
def odo_callback(odom_data,em):
   
    print "odo_callback"
    #pdb.set_trace()
    '''
    Callback function for the subscriber.
    '''
    # Simply print out values in our custom message
    #rospy.loginfo(rospy.get_name() + " I heard %s", data.message +
    #             ", a + b = %d" % (data.a + data.b))
    global time_diff
    global prev_time
    #time_diff=  odom_data.header.stamp.to_sec()
    
    time_diff_robot=0
    if (prev_time>0):
        global counter
        time_diff_robot=odom_data.header.stamp.to_sec()-prev_time

        em.on_odo(odom_data.twist.twist.linear.x, odom_data.twist.twist.angular.z, time_diff_robot);
    
    if em.get_current_goal_id()>=0:
        prev_goal_update=odom_data.header.stamp
        em.calculate_path_to_goal(odom_data.header.stamp.to_sec())
        path=nav_msgs.msg.Path()
        if em.get_current_goal_id()>=0:
            em.get_goal_waypoint()
            path.header.stamp=rospy.get_rostime()
            path.header.frame_id="1"
            pose.header.sec=0
            pose.header.frame_id="1"
            path.poses.clear()
            trace_exp_id=em.get_goals()[0]
            while trace_exp_id != em.get_goal_path_final_exp():
                pose.pose.position.x=em.get_experience(trace_exp_id).x_m
                print pose.pose.position.x
                pose.pose.position.y=em.get_experience(trace_exp_id).y_m
                path.poses.append(pose)
                pose.header.seq+=1
                trace_exp_id=em.get_experience(trace_exp_id).goal_to_current
            pub_goal_path.publish(path)
        else : 
            path.header.stamp=rospy.Time.now()
            path.header.frame_id="1"
            #path.poses=[]
            pub_goal_path.publish(path)
            path.header.seq+=1    
    prev_time=odom_data.header.stamp.to_sec()
    
def action_callback(action,em):
    #pdb.set_trace()
    rospy.logerr("EM:action_callback{%d }action= %d src=%d dst=%d", rospy.get_rostime().to_sec(),action.action,action.src_id,action.dest_id)
    if action.action==Topo.CREATE_NODE:
        print "topo_create_node",action.src_id
        em.on_create_experience2(action.dest_id)
        em.on_set_experience(action.dest_id,0)
    elif action.action==Topo.CREATE_EDGE:
        em.on_create_link2(action.src_id,action.dest_id,action.relative_rad)
        em.on_set_experience(action.dest_id,action.relative_rad)
        print "topo_create_edge"
        #break
    elif action.action==Topo.SET_NODE:
        em.on_set_experience(action.dest_id,action.relative_rad)
        #break                  
    em.show_experiences()
    em.iterate()
    #pose_output.header.stamp=rospy.get_rostime().to_sec()
    pose_output.header.seq+=1
    pose_output.header.frame_id="1"
    pose_output.pose.position.x=em.get_experience(em.get_current_id()).x_m
    pose_output.pose.position.y=em.get_experience(em.get_current_id()).y_m
    pose_output.pose.position.z=0
    pose_output.pose.orientation.x=0
    pose_output.pose.orientation.y=0
    pose_output.pose.orientation.z=math.sin(em.get_experience(em.get_current_id()).th_rad/2.0)
    pose_output.pose.orientation.w=math.cos(em.get_experience(em.get_current_id()).th_rad/2.0)
    pub_pose.publish(pose_output)
    #   static ros::Time prev_pub_time(0); ???
    prev_pub_time=rospy.Time(0)
    
    if action.header.stamp-prev_pub_time>rospy.Duration(30.0):
        #pdb.set_trace()
        prev_pub_time=action.header.stamp
        em_map.header.stamp=rospy.Time.now()
        em_map.header.seq+=1
        em_map.node_count=em.get_num_experiences()
        #em_map.node.resize(em.get_num_experiences())
        topo_node=TopologicalNode()
        xs=[]
        ys=[]
        plot.title("Experience Map Python")
        for i in range(em.get_num_experiences()-1):
            topo_node.id=em.get_experience(i).id
            topo_node.pose.position.x=em.get_experience(i).x_m
            topo_node.pose.position.y=em.get_experience(i).y_m
            topo_node.pose.orientation.x=0
            topo_node.pose.orientation.y=0
            topo_node.pose.orientation.z=math.sin(em.get_experience(i).th_rad/2.0)
            topo_node.pose.orientation.w=math.cos(em.get_experience(i).th_rad/2.0)
            em_map.node.append(topo_node)
        x_exp_vec=em.get_experience(em.get_current_id()).x_m
        y_exp_vec=em.get_experience(em.get_current_id()).y_m
        plot.plot(x_exp_vec,y_exp_vec,'bo')
        plot.pause(0.1)
   
        em_map.edge_count=em.get_num_links()
        #em_map.edge.resize(em.get_num_links())
        
        topo_edge=TopologicalEdge()
        for i in range(em.get_num_links()):
            topo_edge.source_id=em.get_link(i).exp_from_id 
            topo_edge.destination_id=em.get_link(i).exp_to_id
            topo_edge.duration=rospy.Duration(em.get_link(i).delta_time_s)
            topo_edge.transform.translation.x=em.get_link(i).d*math.cos(em.get_link(i).heading_rad)
            topo_edge.transform.translation.y=em.get_link(i).d*math.sin(em.get_link(i).heading_rad)
            topo_edge.transform.rotation.x=0
            topo_edge.transform.rotation.y=0
            topo_edge.transform.rotation.z=math.sin(em.get_link(i).facing_rad/2.0)
            em_map.edge.append(topo_edge)
        pub_em.publish(em_map)
        em_marker.header.stamp=rospy.Time.now()
        em_marker.header.seq+=1
        em_marker.header.frame_id="1"
        em_marker.type=Marker.LINE_LIST
        #em_marker.points.resize(em.get_num_links()*2)
        em_marker.action=Marker.ADD
        em_marker.scale.x=0.01
        em_marker.color.a=1
        em_marker.ns="em"
        em_marker.id=0
        em_marker.pose.orientation.x=0
        em_marker.pose.orientation.y=0
        em_marker.pose.orientation.z=0
        em_marker.pose.orientation.w=1
        
        point_marker=Marker()
        
        
        points_expe=Point()
    
        for i in range(em.get_num_links()):
            points_expe.x=em.get_experience(em.get_link(i).exp_from_id).x_m
            points_expe.y=em.get_experience(em.get_link(i).exp_from_id).y_m
            points_expe.z=0
            em_marker.points.append(points_expe)
            points_expe.x=em.get_experience(em.get_link(i).exp_to_id).x_m
            points_expe.y=em.get_experience(em.get_link(i).exp_to_id).y_m
            points_expe.z=0
            em_marker.points.append(points_expe)
        pub_em_markers.publish(em_marker)
    
def set_goal_pose_callback(pose,em):
    em.add_goal2(pose.pose.position.x,pose.pose.position.y)
    print "set_goal_pose_callback",pose.pose.position.x

def listener():
    '''
    Main func"tion.
    '''
    # Create a subscriber with appropriate topic, custom message and name of
    # callback function.
    em=ratslam.experience_map_younes.ExperienceMap()
    #subscribers
    sub_odometry= rospy.Subscriber(topic_root+"/odom",Odometry,odo_callback,em)
    sub_action=rospy.Subscriber(topic_root+"/PoseCell/TopologicalAction",TopologicalAction,action_callback,em)
    sub_goal=rospy.Subscriber(topic_root+"/ExperienceMap/RobotPose",PoseStamped,set_goal_pose_callback,em)
    rospy.spin()

# Main function.
if __name__ == '__main__':
    # Initialize the node and name it.
    rospy.init_node('RatSLAMExperienceMap')
    # Go to the main loop.
    listener()
