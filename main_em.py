#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Example Python node to listen on a specific topic.
"""

# Import required Python code.
import rospy
import ratslam.posecell_networkv

import ratslam.experience_map_younes
from nav_msgs.msg import Odometry
# Import custom message data.
from ratslam_ros.msg import NodeExampleData
counter = 0
timo=0
prev_time=0
def callback(odom_data,em):
    '''
    Callback function for the subscriber.
    '''
    # Simply print out values in our custom message
    #rospy.loginfo(rospy.get_name() + " I heard %s", data.message +
     #             ", a + b = %d" % (data.a + data.b))
    
    global prev_time
    time_diff=  odom_data.header.stamp.to_sec()
    if (time_diff>0):
        global counter
        time_diff_robot=time_diff-prev_time
        em.on_odo(odom_data.twist.twist.linear.x, odom_data.twist.twist.angular.z, time_diff_robot);
    prev_time=time_diff
def listener():
    '''
    Main function.
    '''
    # Create a subscriber with appropriate topic, custom message and name of
    # callback function.
    #pc=ratslam.posecell_networkv.PosecellNetwork()
    em=ratslam.experience_map_younes.ExperienceMap()
    #slam = ratslam.Ratslam()
    
    #subscribers

    rospy.Subscriber('example', NodeExampleData, callback)
   
    
    rospy.Subscriber('/irat_red/odom',Odometry,callback,em)
    
      #ros::Subscriber sub_odometry = node.subscribe<nav_msgs::Odometry>(topic_root + "/odom", 0, boost::bind(odo_callback, _1, pc, &pub_pc), ros::VoidConstPtr(),
       #                                                             ros::TransportHints().tcpNoDelay());

    
    # Wait for messages on topic, go to callback function when new messages
    # arrive.
    rospy.spin()

# Main function.
if __name__ == '__main__':
    # Initialize the node and name it.
    rospy.init_node('main_em')
    # Go to the main loop.
    listener()
