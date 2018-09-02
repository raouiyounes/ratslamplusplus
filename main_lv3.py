#! /usr/bin/env python

import roslib
#roslib.manifest('package')
import sys
import random
import numpy
import numpy as np
import rospy
import cv2
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
lv=ratslam.local_view_match.LocalViewMatch()
topic_root=''
def image_callback(image,pub_vt):
    

    imdatatest=np.zeros(image.width*image.height*3)
    imdata=ros_numpy.numpify(image)
    k=0
    
    for i in range(image.height):
        for j in range(image.width):
            imdatatest[k]=imdata[i][j]
            #imdatatest[k+1]=imdata[i][j][1]
            #imdatatest[k+2]=imdata[i][j][2]
            k+=1
          
    lv.on_image(imdatatest,False,image.width,image.height)
    vt_output=ViewTemplate()
    vt_output.header.stamp=rospy.Time.now()
    vt_output.header.seq+=1
    vt_output.current_id=lv.get_current_vt()
    vt_output.relative_rad=lv.get_relative_rad()
    pub_vt.publish(vt_output)
   
    pub_objects=rospy.Publisher(topic_root+"/objects",VisualObjet,queue_size=0) 
    object_i=VisualObjet()
    cv=[[10,11],[3,2],[2,33],[11,2],[33,9],[11,2],[333,3]]
    lvb=[1,2,3,4,5,6,7]
    index=random.randint(0,4)
    object_i.x=float(cv[index][0])
    object_i.y=float(cv[index][1])
    object_i.label=lvb[index]
    pub_objects.publish(object_i)
    
    
    
def listener():
    
    #pub_vt.publish(vt_output)
    topic_root=""
    lv=ratslam.local_view_match
    pub_vt=rospy.Publisher(topic_root+"/LocalView/Template",ViewTemplate,queue_size=0)
    sub=rospy.Subscriber(topic_root+"/camera/rgb/image_raw",Image,image_callback,pub_vt)
  
    rospy.spin()
if __name__=='__main__':
    rospy.init_node('RatSLAMLocalViewCells',anonymous=True)
    listener()
    
    
    
    
    
    
