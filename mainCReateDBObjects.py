#! /usr/bin/env python
# -*- coding: utf-8 -*-
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
import pickle
#from src.ratslam_python.src.main_detectObjects import index_of_img
#from src.ratslam_python.src.main_detectObjects import vObjects

topic_root='irat_red'

net = object_detection.Net(graph_fp='%s/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/src/tf_object_detection/faster_rcnn_resnet101_coco_11_06_2017/frozen_inference_graph.pb' %'',
                           labels_fp='/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/src/tf_object_detection/data/label.pbtxt',
                           num_classes=90,
                           threshold=0.6)


vObjects=ob.EM_Object_s()
index_of_img=0


def objDetect(data,file):
	
    #global file
    global index_of_img
    e_max=4
    V1=ob.EM_Object_s()
    V2=ob.EM_Object_s()
    br = CvBridge()
    try:
        img=br.imgmsg_to_cv2(data,"bgr8")
    except CvBridgeError as e:
        print e
    current_objects=net.predict(img,display_img=img)
    beta=e_max/2
    for object in current_objects:
        position=object["bb_o"]
        x=(position[1]+position[3])/2
        y=(position[0]+position[2])/2
        label=object["class"]
        print "label",label 
        
        ptOb=[cv2.KeyPoint(x,y,10)]
		surfObj=self.surf.compute(img,ptOb)
		
        
        vObjects.addObject(x,y,label,index_of_img,surfObj)
        vObjects.createEdge(x,y,label,index_of_img)
    index_of_img+=1
    cv2.imshow('scene at time t',img)

    cv2.waitKey(800)
    cv2.destroyAllWindows() 

def listener():
	reader=pickle.load(open('graphObj.obj','rb'))
	
	nd= list(reader.nodes)	
	print nd[0].cv, "i am here"
	'''
    filehandler = open("graphObj.obj", 'w')
    sub=rospy.Subscriber('/camera/rgb/image_raw',Image,objDetect,file)
    rospy.spin()
    #nx.write_gml(vObjects.objects, "objectDB.gml")
    pickle.dump(vObjects.objects, filehandler)
    '''
if __name__=='__main__':
    rospy.init_node('RatSLAMObjects',anonymous=True)
    listener()
    




