
# -*- coding: utf-8 -*
'''
Created on 2 janv. 2019

@author: younes
'''
import numpy as np
import cv2
import MapPoint
from cv_bridge import CvBridge, CvBridgeError

class Frame(object):
    '''
    classdocs
    '''


    def __init__(self,im_,timeStamp,extractor,voc,K,distCoef):
        self.mOw=np.zeros(4)
        self.mRcw=np.zeros((3,3))
        self.mtcw=np.zeros(4)
        self.im=im_
        self.N=16
        self.mGrid=[]
        self.nNextid
        self.dictionarySize = 5
        self.BOW = cv2.BOWKMeansTrainer(self.dictionarySize)
        self.fx
        self.fy
        self.cx
        self.cy
        self.mDistCoef=[]
        '''
        Constructor
        '''
        
        orb = cv.ORB_create()
        # find the keypoints with ORB
        mvKeys = orb.detect(img,None)
        # compute the descriptors with ORB
        self.mvKeys, self.mDescriptors = orb.compute(im_, mvKeys)

        N=len(self.mvKeys)
        if not self.mvKeys:
            return 
        mvpMapPoints=[]
        for i in range(N):
            mvpMapPoints.append(MapPoint(null))
        
        
    # computation of bag of words
    def ComputeBoW(self):
        self.BOW.add(self.mDescriptors)
        
    def UndistortKeyPoints(self):
        if self.mDistCoef[0]==0.0:
            self.mvKeysUn=self.mvKeys
            return 
        # fill matrix with points 
        mat=np.zeros(self.mvKeys.shape,np.float)
        mat = cv2.cvtColor(mat, cv2.COLOR_GRAY2BGR)
        for i in len(self.mvKeys):
            mat[i,0]=self.mvKeys[i,0]
            mat[i,0]=self.mvKeys[i,1]
        
        #indistort points
        
        mat=mat.reshape(2)
        
        pts_uv = cv2.undistortPoints(mat, self.camera_matrix, self.mDistCoef)
        mat=mat.reshape(1)
        
    #Fill undistorted keypoint vector
        self.mvKeys.resize(len(self.mDistCoef))
        for i in range(len(self.mvKeys)):
            kp=self.mvKeys[i]
            kp[0]=mat[i,0]
            kp[1]=mat[i,1]
            self.mvKeysUn=kp
        
        # Initiate ORB de
        
