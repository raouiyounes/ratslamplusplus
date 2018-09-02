'''
Created on 2 sept. 2018

@author: younes
'''
import networkx as nx
import roslib
#roslib.manifest('package')
import sys
import numpy
import numpy as np
import rospy
import math
from cv_bridge import CvBridge,CvBridgeError
import cv2
import ros_numpy
from std_msgs.msg import String
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import  Image
from ratslam_ros.msg import VisualObjet
from cmath import sqrt
import ratslam.networkx as nx
import ratslam.EM_Objects as ob
from tf_object_detection.models import object_detection 
from tf_object_detection.config import config
import tensorflow
import pdb
import tensorflow as tf
from ratslam_ros.msg import signalFromCNN
import time
import pdb

ddd

topic_root='irat_red'

qqqqqqqqqqqqqqqqqqq


def objDetect(data,file):
    #global file
    global index_of_img
    e_max=4
    V1=ob.EM_Object_s()
    V2=ob.EM_Object_s()
    pub_cnn.publish(0.0)
    br = CvBridge()
    V_temp=ob.EM_Object_s()

    try:
        img=br.imgmsg_to_cv2(data,"bgr8")
    except CvBridgeError as e:
        print e
      
    current_objects=net.predict(img,display_img=img)
    beta=e_max/2
    all_images.append(img)
    for object in current_objects:
        position=object["bb_o"]
        x=(position[1]+position[3])/2
        y=(position[0]+position[2])/2
        label=object["class"]
        print "label",label 
        vObjects.addObject(x,y,label,index_of_img)
        vObjects.createEdge(x,y,label,index_of_img)
        V.addObject(x, y, label,index_of_img)
    index_of_img+=1
    cv2.imshow('scene at time t',img)

    cv2.waitKey(1)
    cv2.destroyAllWindows()
    
def listener():
    file=open("/home/younes/eclipse-workspace/Hamburg_Lim/scoreMatching.txt","a")

    sub=rospy.Subscriber('/camera/rgb/image_raw',Image,objDetect,file)
    rospy.spin()
    
if __name__=='__main__':
    rospy.init_node('RatSLAMObjects',anonymous=True)
    listener()
    










if __name__ == '__main__':
    pass