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
    #index on the graph
    current_ob=0
    def __init__(self):
        
        self.V1=[]
        self.objetGraphTemplates=[]
        self.objects=nx.Graph()
        self.emax=150
        self.imageTemplate=[]
        EM_Object_s.current_ob+=1
        self.graphTemplates=[]
    def addObject(self,x,y,lv,index_im):
        v=Vertex(x,y,lv,index_im)
        
        self.objects.add_node(v)
        return v
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
    
    def get_current_ob(self):
        return EM_Object_s.current_ob

    #def createGTemplate(self):
    

    def on_objets(self,current_objects,index_of_img,image):
        self.imageTemplate.append(image)
        V1=[]
        for object in current_objects:
            position=object["bb_o"]
            x=(position[1]+position[3])/2
            y=(position[0]+position[2])/2
            label=object["class"]
            V1.append(self.addObject(x, y, label,index_of_img))
            #self.V.addObject(x, y, label,index_of_img)
        
        self.graphTemplates.append(V1)
        return V1
        
        