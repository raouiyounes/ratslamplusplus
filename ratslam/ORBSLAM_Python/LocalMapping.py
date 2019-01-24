#! /usr/bin/env python2.7


from multiprocessing import Process, Lock
import threading
import rospy

import time
class LocalMapping(threading.Thread):
    def __init__(self):

        self.mlNewKeyFrames=[]
        self.mMutexNewKFs=asyncio.Lock()

    def run(self):
        rate = rospy.Rate(500)  # 10hz
        while not rospy.is_shutdown():
            if (self.CheckNewKeyFrames()):
                # Tracking will see that Local Mapping is busy
                self.SetAcceptKeyFrames(False)

                # BoW conversion and insertion in Map
                ProcessNewKeyFrame();

                # Check recent MapPoints
                MapPointCulling();

                # Triangulate new MapPoints
                CreateNewMapPoints();

                # Find more matches in neighbor keyframes and fuse point duplications
                SearchInNeighbors();

                mbAbortBA = false;

                """if (not CheckNewKeyFrames() and  not stopRequested()):
                #Local BA
                Optimizer::LocalBundleAdjustment(mpCurrentKeyFrame, & mbAbortBA);"""

                # Check redundant local Keyframes
                KeyFrameCulling();

                #mpMap->SetFlagAfterBA();

                # Tracking will see Local Mapping idle
                #if (!CheckNewKeyFrames()):
                #       SetAcceptKeyFrames(true);


                #mpLoopCloserInsertKeyFrame(mpCurrentKeyFrame);


                # Safe area to stop
                if (stopRequested()):

                    Stop();
                    r2 = rospy.Rate(500)  # 10hz

                    while (isStopped() and  not rospy.is_shutdown()):
                        r2.sleep();


                SetAcceptKeyFrames(true);


            ResetIfRequested();
            r.sleep();

    def InsertKeyFrame(self,lock,pKF):
        lock.acquire()

        Process(target=f, args=(lock, num)).start()
        self.mlNewKeyFrames.appende(pKF)
        self.mbAbortBA=True

    """def SetAcceptKeyFrames(flag)

    boost::mutex::scoped_lock lock(mMutexAccept);
        self.mbAcceptKeyFrames=flag;"""





