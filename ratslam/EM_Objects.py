import random
import networkx as nx
from OpenGL.GL.feedback import Vertex
import numpy as np
import math
from match_ponce import Matching
from docutils.nodes import image

'''
Created on 23 fevr. 2018

@author: younes
'''

         
class Vertex:     
    def __init__(self,x,y,lv,index_im):
        self.cv=[x,y]
        self.lv=lv
        self.indexOfView=index_im

class EM_Object_s(Matching):
    #index on the graph
    current_ob=0
    def __init__(self):
        self.minMatchingScore=0
        self.V1=[]
        self.objetGraphTemplates=[]
        self.objects=nx.Graph()
        self.emax=150
        self.imageTemplate=[]
        EM_Object_s.current_ob+=1
        self.graphTemplates=[]
        self.current_ob=0
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
    
 
    #def createGTemplate(self):
    
    def reset(self):
        self.objects.clear()
    def on_objects(self,current_objects,image,index_of_img):
        self.imageTemplate.append(image)
        for object in current_objects:
            position=object["bb_o"]
            x=(position[1]+position[3])/2
            y=(position[0]+position[2])/2
            label=object["class"]
            self.addObject(x, y, label,index_of_img)
            #self.V.addObject(x, y, label,index_of_img)
        
        self.graphTemplates.append(self.objects)
        return self.objects
    
    # ompare between the actual grapg and all the graphs of objects
    def compare(self,V1):
        
        score=[]
        for oneObjectTemplate in self.graphTemplates:
            Matching.__init__(self, V1, oneObjectTemplate, self.imageTemplate)        
            Hl=self.create_Hl()
            Hr=self.create_Hr()
            H=[[[[0]*len(Hr[0][0][0])]*len(Hr[0][0])]*len(Hr[0])]*len(Hr)
            for i in range(len(Hr)):
                for j in range(len(Hr[0])):
                    for k in range(len(Hr[0][0])):
                        for l in range(len(Hr[0][0][0])):
                            H[i][j][k][l]=Hr[i][j][k][l]*Hl[i][j][k][l]
            
            score.append(self.compute_X(H))
        
        minScore=min(score)
        print  "minScore",minScore 
        if minScore<self.minMatchingScore:
            self.current_ob=score.index(minScore)
        else:
            self.current_ob+=1
                
    def get_current_ob(self):
        return self.current_ob
        