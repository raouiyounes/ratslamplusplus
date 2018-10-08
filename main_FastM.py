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


def metricalMapping(objectR,packetCAN,vtrans,vrot,time_diff_s)

