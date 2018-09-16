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

# Import custom message data.
from ratslam_ros.msg import NodeExampleData
counter = 0
timo=0
prev_time=0
pc_output=TopologicalAction()
topic_root=''
pose_pc_robot=open("poses_pc_robot22.txt","w")
pcx=0
pcy=0


class  POSE: 
	def __init__(self):
		self.signGlob=0
	
	
	def signalFromObjNode(self,sign):
		if (sign.signalCNN !=0):
			self.signGlob= 1
            
	def callback(self,odom_data,pc_args_1):
		#pdb.set_trace()
		pc=pc_args_1[0]
		pub_pc=pc_args_1[1]
		
		'''
		Callback function for the subscriber.
		'''
		if 1.0==1.0:
			#self.signGlob=0
			global prev_time
			if (prev_time>0):
				global counter
				pc_output.src_id=pc.get_current_exp_id()
				time_diff_robot=odom_data.header.stamp.to_sec()-prev_time
				pc.on_odo(odom_data.twist.twist.linear.x, odom_data.twist.twist.angular.z, time_diff_robot);
				temp_action=pc.get_action()
				pc_output.action=temp_action.value
				if pc_output.action!=0:
					
					pc_output.header.stamp=rospy.Time.now()
					pc_output.header.seq+=1
					pc_output.dest_id=pc.get_current_exp_id()
					pc_output.relative_rad=pc.get_relative_rad()
					pub_pc.publish(pc_output)
					print(rospy.Time.now().to_sec(),pc_output.header.seq,pc_output.action, pc_output.src_id,pc_output.dest_id)
			prev_time=odom_data.header.stamp.to_sec()
			 
			pcx=pc.best_x
			pcy=pc.best_y
			pcth=pc.best_th
			print "xesti= "+str(pcx)+"yesti= "+str(pcy)+"thethest ="+str(pcth)
			pose_pc_robot.write(str(pc.best_x)+" "+str(pc.best_y)+" "+str(pc.best_th)+"\n")
	def template_callback(self,ot,arg_template):
		print "jjjjjjjjjj"
		pc=arg_template[0]
		pub_pc=arg_template[1]
		pc.on_view_template(ot.current_id,0.0)
	def listener(self):
		'''
		Main function.
		'''
		# Create a subscriber with appropriate topic, custom message and name of
		# callback function.
		pc=ratslam.posecell_networkv.PosecellNetwork()
		
		pub_pc=rospy.Publisher(topic_root+"/PoseCell/TopologicalAction",TopologicalAction,queue_size=0)
		rospy.Subscriber(topic_root+"/odom",Odometry,self.callback,(pc,pub_pc))
		sub=rospy.Subscriber('/signalCNN',signalFromCNN,self.signalFromObjNode)

		rospy.Subscriber(topic_root+'/LocalView/Template',ViewTemplate,self.template_callback,(pc,pub_pc))
		#rospy.Subscriber('/LocalObjectGraph/Template',GraphObjectTemplate,self.template_callback,(pc,pub_pc))
       
		# Wait for messages on topic, go to callback function when new messages
		# arrive.
		rospy.spin()

# Main function.
if __name__ == '__main__':
    # Initialize the node and name it.
    rospy.init_node('RatSLAMPoseCells')
    motion=POSE()
    # Go to the main loop.
    motion.listener()
