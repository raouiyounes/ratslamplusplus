import random
import networkx as nx
from OpenGL.GL.feedback import Vertex
import numpy as np
import math
'''
Created on 23 fevr. 2018

@author: younes
'''

         
class Vertex:     
    def __init__(self,x,y,lv,index_im):
        self.cv=[x,y]
        self.lv=lv
        self.indexOfView=index_im

class EM_Object_s:
    
    def __init__(self):
        self.objects=nx.Graph()
        self.emax=150
    def addObject(self,x,y,lv,index_im):
        v=Vertex(x,y,lv,index_im)
        self.objects.add_node(v)
    def createEdge(self,x,y,lv,index_im):
        vx_i=Vertex(x,y,lv,index_im)
        for ob in list(self.objects.nodes()):
            vx=ob
            e=self.normal(vx.cv,vx_i.cv)
            
            if (e<self.emax and ob!=vx_i):
                self.objects.add_edge(vx,vx_i)
            
    def normal(self,cvi,cvj):
        sigma=0.2
        mean=math.sqrt((cvi[0]-cvj[1])**2+(cvj[0]-cvj[1])**2)
        e=np.random.normal(mean,sigma,1000)
        return np.mean(e)
    """
    def findRecentObjects(self):
        for vertexi in self.objects:
            cv=vertexi.cv
            lv=vertexi.lv
    """
    




'''
object_database={}

class EM_Object_s(ExperienceMap):
    objects=[]
    def addObject(self,x,y,lv):
        v=Vertex(x,y,lv)
        EM_Objects.objects.append(v)
    def __init__(self):
        self.objects=[]
    
    def get_objects(self):
        detect_objects=True
        while detect_objects==True:
            object_index=random.randint(1,10)
            descritor_object=object_database[object_index]
            self.objects.append(descritor_object)
    def createEdge(self):



        
    def normal(self,cvi,cvj):
        
        cov=[0.2,0.2]
        mean=[cvi.x-cvj.x,cvj.y-cvj.y]
        x, y = np.random.multivariate_normal(mean, cov, 5000).T
        return x,y
        
    def findRecentObjects(self):
        for vertexi in self.objects:
            cv=vertexi.cv
            lv=vertexi.lv
'''    

        
        
    