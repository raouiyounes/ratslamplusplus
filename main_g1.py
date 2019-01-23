#! /usr/bin/env python2.7
# -*- coding: utf-8 -*-

'''
Created on 16 avr. 2018

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
import ratslam.local_view_match
from std_msgs.msg import String
from ratslam_ros.msg import ViewTemplate   
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import  Image
from sensor_msgs.msg import PointCloud2 
from ratslam_ros.msg import VisualObjet
from cmath import sqrt
import ratslam.networkx as nx
import ratslam.Optimization as ob
import matplotlib.pyplot as plt
from tf_object_detection.models import object_detection 
from tf_object_detection.config import config
import tensorflow
topic_root='irat_red'
import pdb
import tensorflow as tf
from ratslam_ros.msg import signalFromCNN
import time
import pyrosbag as prb
import pdb
from ratslam.match_ponce import Matching
from ratslam_ros.msg import GraphObjectTemplate
import pickle
from collections import defaultdict

INTERVAL=3



reader=pickle.load(open('/home/younes/workMOON/prjMapping/CSAIL_Lim/src/ratslam_python/src/graphObjdb.obj','rb'))


objectsVertices= list(reader.nodes)  

indexOfVertex=0


db=ob.DbObjects(objectsVertices)
currObj = ob.currentObject(db)


def objDetect(data,pub_ot):
    global indexOfVertex
    currentObj=objectsVertices[indexOfVertex]
    currObj.on_object(currentObj)
    currObj.compute_G1()
    currObj.compute_G2()

    currObj.OptimizationScore()


    '''

    object.currentOobject(objectsVertices[step])

    print(object.current_ob)

    index_of_img+=1



    G.compare(O)
    ot_output=GraphObjectTemplate()
    ot_output.header.stamp=rospy.Time.now()
    ot_output.header.seq+=1
    ot_output.current_id=G.get_current_ob()
    G.reset()
    print "ot_output.current_id",ot_output.current_id
    pub_ot.publish(ot_output)
    cv2.imshow('scene at time t',img)
    cv2.waitKey(1)
    cv2.destroyAllWindows()
    '''    

    indexOfVertex+=1

def listener():
    
    pub_ot=rospy.Publisher('/LocalObjectGraph/Template',GraphObjectTemplate,queue_size=10)
    sub=rospy.Subscriber('/camera/rgb/image_raw',Image,objDetect,pub_ot)
    
    
    rospy.spin()
    
if __name__=='__main__':
    rospy.init_node('RatSLAMObjects',anonymous=True)
    listener()
    
    
    
    
    
    
