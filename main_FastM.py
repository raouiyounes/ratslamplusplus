#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Example Python node to listen on a specific topic.
"""

# Import required Python code.
import pdb 
import sys
import mpl_toolkits.mplot3d.axes3d as p3
import rospy
import ratslam.posecell_networkv
from nav_msgs.msg import Odometry
from matplotlib import pyplot as plot
from ratslam_ros.msg import TopologicalAction
from ratslam_ros.msg import ViewTemplate
from ratslam_ros.msg import signalFromCNN
from ratslam_ros.msg import GraphObjectTemplate
import ratslam.EM_Objects as ob
import ratslam.FASTSlam as fslam


fastM=fslam.FASTSlam()
rospy.Subscriber("/odom",odom_callbck,self.callback,(pc,pub_pc))

reader=pickle.load(open('graphObj.obj','rb'))
Observation=list(reader.nodes)
prev_time=0

i=0

p=[]

def metricalMapping(objectR,packetCAN):	
	currentObjects=Observation[i]	
	for i in len(G1):
		ob_i=G1[i]
		fastM.mapping(currentObjects,packetCAN):


	for i in range(N):
			beta+=random.random()*2.0*mw
			while beta>w[index]:
				beta-=w[index]
				index=(index+1)%N
	p3.append(p[index])



	i+=1	


def odom_callbck(odom_data):
	
	global prev_time
	if (prev_time>0):
		time_diff_s=odom_data.header.stamp.to_sec()-prev_time
		fastM.onOdo(odom_data.twist.twist.linear.x, odom_data.twist.twist.angular.z,time_diff_s)
	prev_time=odom_data.header.stamp.to_sec()

def listener(self):
		
		# subscribe to odom and weight topics
		rospy.Subscriber("/odom",odom_callbck,self.callback,(pc,pub_pc))
		rospy.Subscriber('/Weights',metricalMapping,(pc,pub_pc))
		
		
		
		# Wait for messages on topic, go to callback function when new messages
		# arrive.
		rospy.spin()
