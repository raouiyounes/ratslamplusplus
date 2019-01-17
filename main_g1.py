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
import ratslam.EM_Objects as ob
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

INTERVAL=3

# vector that computes the scores of X

scoreXVector=[]
#pdb.set_trace()
vObjects=ob.EM_Object_s()
G=nx.Graph()

""" code of detection"""

model_name = config.models["2"]
net = object_detection.Net(graph_fp='%s/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/src/tf_object_detection/faster_rcnn_resnet101_coco_11_06_2017/frozen_inference_graph.pb' %'',
                           labels_fp='/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/src/tf_object_detection/data/label.pbtxt',
                           num_classes=90,
                           threshold=0.6)
CAMERA_MODE = 'camera'
STATIC_MODE = 'static'
IMAGE_SIZE = 320
vObjects=ob.EM_Object_s()
V=ob.EM_Object_s()
pub_cnn=rospy.Publisher(topic_root+"/signalCNN",signalFromCNN,queue_size=0)
allObjects_V=[]
all_images=[]
index_of_img=0

reader=pickle.load(open('/home/younes/workMOON/prjMapping/CSAIL_Lim/src/ratslam_python/src/graphObjdb.obj','rb'))
    
objectsVertices= list(reader.nodes)  

step=0

G=ob.EM_Object_s()
def objDetect(data,pub_ot):
    global step
    #global file
    global index_of_img
    e_max=4
    V1=ob.EM_Object_s()
    br = CvBridge()
    V_temp=ob.EM_Object_s()

    try:
        img=br.imgmsg_to_cv2(data,"bgr8")
    except CvBridgeError as e:
        print e
      
    current_objects=objectsVertices[step]
    print(current_objects)
    beta=e_max/2
    all_images.append(img)
    
    O=G.on_objects(current_objects,img,index_of_img)
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
    step+=1

def listener():
    
    pub_ot=rospy.Publisher('/LocalObjectGraph/Template',GraphObjectTemplate,queue_size=10)
    sub=rospy.Subscriber('/camera/rgb/image_raw',Image,objDetect,pub_ot)
    
    
    rospy.spin()
    
if __name__=='__main__':
    rospy.init_node('RatSLAMObjects',anonymous=True)
    listener()
    
    
    
    
    
    
