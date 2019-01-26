
# -*- coding: utf-8 -*
'''
Created on 2 janv. 2019

@author: younes
'''
import numpy as np
import cv2
import MapPoint
import Converter as convt
import sys

sys.path.append('/home/younes/PycharmProjects/RatSLAM++1.0/CSAIL_Lim/src/ratslam_python/src/ratslam')
import DBoWpy.TemplateVocabulary as mpORBvocabulary

import DBoWpy.BoWvector

import
from cv_bridge import CvBridge, CvBridgeError

FRAME_GRID_ROWS=48
FRAME_GRID_COLS=64

class Frame(object):
    '''
    classdocs
    '''

    nNextId=0
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
        self.mbInitialComputations=True
        self.mDistCoef=[]
        self.mvScaleFactors=mvScaleFactors
        mBowVec=

        orb = cv2.ORB_create(nfeatures=int(.25 * (bd.shape[0] * bd.shape[1])),
                             edgeThreshold=patch_size,
                             scaleFactor=1.2,
                             nlevels=8,
                             patchSize=patch_size,
                             WTA_K=4,
                             scoreType=cv2.ORB_FAST_SCORE)

        # find the keypoints with ORB
        mvKeys = orb.detect(img,None)
        # compute the descriptors with ORB
        self.mvKeys, self.mDescriptors = orb.compute(im_, mvKeys)

        N=len(self.mvKeys)
        if not self.mvKeys:
            return 
        self.mvpMapPoints=[]
        for i in range(N):
            mvpMapPoints.append(MapPoint(null))
        self.UndistortKeyPoints();

        if self.mbInitialComputations:
            self.ComputeImageBounds()

            self.fx=K[0,0]
            self.fy=K[1,1]
            self.cx=K[0,2]
            self.cy=K[1,2]
            self.mbInitialComputations = False;

        # This is done for the first created Frame
        mnId = Frame.nNextId+1;
        self.mfScaleFactor=orb.getScaleFactor()
        self.mnScaleLevels=orb.getNLevels()

        self.mvScaleFactors=np.zeros(self.mnScaleLevels)
        self.mvLevelSigma2=np.zeros(self.mnScaleLevels)
        self.mvScaleFactors[0] = 1.0
        self.mvLevelSigma2[0] = 1.0
        for i in range(1,self.mnScaleLevels):
            self.mvScaleFactors[i] = self.mvScaleFactors[i - 1] * self.mfScaleFactor;
            self.mvLevelSigma2[i] = self.mvScaleFactors[i] * self.mvScaleFactors[i];

        self.mvInvLevelSigma2=np.zeros(len(self.mvLevelSigma2))
        for i in range(self.mnScaleLevels):
            self.mvInvLevelSigma2[i] =1/self.mvLevelSigma2[i];

        self.mvInvLevelSigma2.reshape(len(self.mvLevelSigma2))
        for i in range(self.mnScaleLevels):
            self.mvInvLevelSigma2[i]=1/self.mvInvLevelSigma2[i]

        #Assign Features to Grid Cells
        nReserve = 0.5 * N/(FRAME_GRID_COLS*FRAME_GRID_ROWS)
        for i in range(FRAME_GRID_COLS):
            for j in range(FRAME_GRID_ROWS):
                mGrid=[[[0]*nReserve]*FRAME_GRID_ROWS]*FRAME_GRID_COLS


        for i in range(len(self.mvKeysUn)):
            kp=self.mvKeysUn[i]
            nGridPosX=0, nGridPosY=0;
            if self.PosInGrid(kp,nGridPosX,nGridPosY):
                mGrid[nGridPosX][nGridPosY].append(i)


        # TODO -->  mvbOutlier = vector < bool > (N, false);

        # computation of bag of words
    def ComputeBoW(self):
        self.BOW.add(self.mDescriptors)

        if not self.mBowVec:
            vCurrentDesc=convt.toDescriptorVector(self.mDescriptors)
            mpORBvocabulary.transform(vCurrentDesc,mBowVec,mFeatVec,4);

        
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
        



    def PosInGrid(kp,posX,posY):
        posX = np.round((kp.pt.x-Frame.mnMinX)*self.mfGridElementWidthInv)
        posY = np.round((kp.pt.y-Frame.mnMinY)*self.mfGridElementHeightInv)
        #    //Keypoint's coordinates are undistorted, which could cause to go out of the image
        if posX<0 or posX>=FRAME_GRID_COLS or posY <0 or posY>=FRAME_GRID_ROWS:
            return False
        return True




