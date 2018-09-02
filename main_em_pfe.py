'''
Created on 29 mars 2018

@author: younes
'''
import rospy
from ratslam.em import  ExperienceMap
from nav_msgs.msg import Odometry

def motion_model(odom_data,em):
    global time_diff
    global prev_time
    #time_diff=  odom_data.header.stamp.to_sec()
    
    time_diff_robot=0
    if (prev_time>0):
        global counter
        time_diff_robot=odom_data.header.stamp.to_sec()-prev_time
        em.on_odo(odom_data.twist.twist.linear.x, odom_data.twist.twist.angular.z, time_diff_robot);

def listener():
    
    em=ExperienceMap()
    sub_odom=rospy.subscriber("/irat_red/odom",Odometry,motion_model,em)
    
    






if __name__ == '__main__':
    listener()
    rospy.init_node('main_em_pfe')
