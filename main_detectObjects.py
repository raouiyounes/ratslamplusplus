#! /usr/bin/env python
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
# here I will add the part of the code of object recognition with cnn
pub_cnn=rospy.Publisher(topic_root+"/signalCNN",signalFromCNN,queue_size=0)
allObjects_V=[]
all_images=[]
index_of_img=0
#file=open("/home/younes/eclipse-workspace/Hamburg_Lim/scoreMatching.txt","a")
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
        V1.addObject(x, y, label,index_of_img)
        V.addObject(x, y, label,index_of_img)
    index_of_img+=1
        
    for ob1 in V1.objects:
        for ob2 in V.objects:
            dij=math.sqrt((ob1.cv[0]-ob2.cv[0])**2+(ob1.cv[1]-ob2.cv[1])**2)
            if dij<beta:
                x=ob2.cv[0]
                y=ob2.cv[1]
                lv=ob2.lv
                V_temp.addObject(x,y,lv,index_of_img)
    V_tot=nx.Graph()
    V_tot=nx.compose(V1.objects,V_temp.objects)
    V1.objects=V_tot
    
    
    for i in V.objects:
        if i not in V1.objects:
            x=i.cv[0]
            y=i.cv[1]
            lv=i.lv
            V2.addObject(x,y,lv,index_of_img)
    
    V1.emax=4
    match=Matching(V1,V2,all_images)
    Hr=match.create_Hr()
    Hl=match.create_Hl()
    number_of_1=0
    for i in range(len(Hr)):
        for j in range(len(Hr[0])):
            for k in range(len(Hr[0][0])):
                for l in range(len(Hr[0][0][0])):
                    if (Hl[i][j][k][l]==1):
                        print " je suis un 1"
                        number_of_1+=1
    #print "index of 1",Hl.index(0)
    print "number_of_1",number_of_1
    H=[[[[0]*len(Hr[0][0][0])]*len(Hr[0][0])]*len(Hr[0])]*len(Hr)
    for i in range(len(Hr)):
        for j in range(len(Hr[0])):
            for k in range(len(Hr[0][0])):
                for l in range(len(Hr[0][0][0])):
                    H[i][j][k][l]=Hr[i][j][k][l]*Hl[i][j][k][l]
   
    match.all_views=all_images
    scoreX=match.compute_X(H)
    scoreXVector.append(scoreX)
    print "score X",scoreX
    pub_cnn.publish(1.0)
    cv2.imshow('scene at time t',img)
    cv2.waitKey(1)
    cv2.destroyAllWindows()
    




def listener():
  
    sub=rospy.Subscriber('/camera/rgb/image_raw',Image,objDetect,file)
    rospy.spin()
if __name__=='__main__':
    rospy.init_node('RatSLAMObjects',anonymous=True)
    listener()
    
    
    
    
    
    
