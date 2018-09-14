#! /usr/bin/env python

import roslib
#roslib.manifest('package')
import sys
import random
import numpy
import numpy as np
import rospy
import cv2
import pdb
import ros_numpy
import ratslam.local_view_match
from std_msgs.msg import String
from ratslam_ros.msg import ViewTemplate   
from ratslam_ros.msg import VisualObjet
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import  Image
from sensor_msgs.msg import PointCloud2 
from cmath import sqrt
import Queue
from ratslam_ros.msg import signalFromCNN

import ratslam.networkx as nx
import ratslam.EM_Objects as ob
import matplotlib.pyplot as plt
from tf_object_detection.models import object_detection 
from tf_object_detection.config import config
import tensorflow
topic_root=''
import pdb
import tensorflow as tf
from ratslam_ros.msg import signalFromCNN

#pdb.set_trace()
lv=ratslam.local_view_match.LocalViewMatch()
p=0


vObjects=ob.EM_Object_s()
G=nx.Graph()
# here I will add the part of the code of object recognition with cnn


pub_cnn=rospy.Publisher(topic_root+"/signalCNN",signalFromCNN,queue_size=0)



class Objects:
    def __init__(self):
        self.signGlob=0
    def signalFromObjNode(self,sign):
        if (sign.signalCNN !=0):
            self.signGlob= 1
            
    def image_callback(self,image,args):
        pub_vt=args[0]
        x=args[1]
        if self.signGlob==self.signGlob:
            self.signGlob=0
            imdatatest=np.zeros(image.width*image.height*3)
            imdata=ros_numpy.numpify(image)
            k=0
            for i in range(image.height):
                for j in range(image.width):
                    imdatatest[k]=imdata[i][j][0]
                    imdatatest[k+1]=imdata[i][j][1]
                    imdatatest[k+2]=imdata[i][j][2]
                    k+=1
            
            lv.on_image(imdatatest,True,image.width,image.height)
            vt_output=ViewTemplate()
            vt_output.header.stamp=rospy.Time.now()
            vt_output.header.seq+=1
            vt_output.current_id=lv.get_current_vt()
            vt_output.relative_rad=lv.get_relative_rad()
            pub_vt.publish(vt_output)
        
        
        
    def listener(self):
        
        #pub_vt.publish(vt_output)
        lv=ratslam.local_view_match
        
        pub_vt=rospy.Publisher(topic_root+"/LocalView/Template",ViewTemplate,queue_size=0)
    #sub=rospy.Subscriber(topic_root+"/wide_stereo/left/image_rect",Image,image_callback,pub_vt)
        sub=rospy.Subscriber('/signalCNN',signalFromCNN,self.signalFromObjNode)
       
        x=ob.signGlob
        
        sub=rospy.Subscriber(topic_root+"/camera/rgb/image_raw",Image,self.image_callback,(pub_vt,x))
    
        rospy.spin()
if __name__=='__main__':
    ob=Objects()
    rospy.init_node('RatSLAMLocalViewCells',anonymous=True)
    ob.listener()
    
    
    
    
    
    
