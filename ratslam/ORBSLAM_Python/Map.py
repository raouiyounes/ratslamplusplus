
import sets
import threading
import KeyFrame

class Map:
    def __init__(self):
        self.mbMapUpdated= False
        self.mnMaxKFid = 0;

        self.mMutexMap = threading.Lock()
        self.mspMapPoints=set()
        self.mspKeyFrames=set()
    def AddKeyFrame(self,pKF):
        my_lock = self.mMutexMap.acquire()
        self.mspKeyFrames.add(pKF)
        if (pKF.mnId > self.mnMaxKFid)
            self.mnMaxKFid = pKF.mnId;
        self.mbMapUpdated = True;

    def EraseMapPoint(self,pMP):
        my_lock = self.mMutexMap.acquire()
        self.mspMapPoints.erase(pMP);
        self.mbMapUpdated = True;

    def EraseKeyFrame(self,pKF):
        my_lock = self.mMutexMap.acquire()
        self.mspKeyFrames.erase(pKF);
        self.mbMapUpdated = True;


    def SetReferenceMapPoints(self,vpMPs):
        my_lock = self.mMutexMap.acquire()
        self._mvpReferenceMapPoints = vpMPs;

    def GetAllMapPoints(self):
        my_lock = self.mMutexMap.acquire()
        return self._mspMapPoints


    def MapPointsInMap(self):
        my_lock = self.mMutexMap.acquire()
        return len(self.mspMapPoints)

    def KeyFramesInMap(self):
        my_lock = self.mMutexMap.acquire()
        return len(self.mspKeyFrames)

    def GetReferenceMapPoints(self):
        my_lock = self.mMutexMap.acquire()
        return self._mvpReferenceMapPoints

    def isMapUpdated(self):
        my_lock = self.mMutexMap.acquire()
        return self.mbMapUpdated;


    def GetMaxKFid(self):
        my_lock = self.mMutexMap.acquire()
        self._mbMapUpdated = True;

    def GetMaxKFid(self):
        my_lock = self.mMutexMap.acquire()
        self._mbMapUpdated=False;

    def GetMaxKFid(self):
        my_lock = self.mMutexMap.acquire()

        return self._mnMaxKFid;

    def clear(self):
        self.mspMapPoints.clear()
        self.mspKeyFrames.clear()
        self.mnMaxKFid = 0;
        self.mvpReferenceMapPoints.clear();



    mvpReferenceMapPoints=property(GetReferenceMapPoints,SetReferenceMapPoints)

    mspMapPoints=property(GetAllMapPoints)
    mnMaxKFid=property(GetMaxKFid)
    mbMapUpdated =property(GetMaxKFid,GetMaxKFid,GetMaxKFid)






