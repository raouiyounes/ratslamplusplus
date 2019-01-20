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

         

class DbObjects:

    def __init__(self,objectsDb):
        self.constructGraph()

     def constructGraph(self):
        self.topoMap= nx.Graph()
        for ob in self.objectsDb:
            vertex_i=Vertex(ob.cv,ob.label,ob.index_of_img,ob.listsurf)
            self.topoMap.add_node(vertex_i)

        for vx_0 in self.topoMap:
            for vx_1 in self.topoMap:
                if vx_0!=vx_1:
                    e=self.normal(vx_0.cv,vx_1.cv)    
                        if e<self.e_max:
                            self.topoMap.add_edge(vx_0,vx_1)


    def normal(self,cvi,cvj):
        sigma=0.2
        mean=math.sqrt((cvi[0]-cvj[1])**2+(cvj[0]-cvj[1])**2)
        e=np.random.normal(mean,sigma,1000)
        return np.mean(e)
    
    def getVectex(self,indexOfVertex):

        return self.topoMap.node(self.objectsDb[indexOfVertex])


class Vertex:     
    def __init__(self,cv_i,label,index_of_img,listsurf):
        self.cv=cv_i
        self.lv=label
        self.indexOfView=index_of_img
        self.surf=listsurf




class currentOobject(Matching):
    
    def __init__(self):
    
        self.objetGraphTemplates=[]
        self.e_max=4

    def on_objects(self,newObj):
        
        self.newObj=newObj
        vertex_i=Vertex(newObj.cv,newObj.label,newObj.index_of_img,newObj.listsurf)
            
        self.compute_G1(newObj)

        return self.objects
    
    # ompare between the actual graph and all the graphs of objects
    def OptimizationScore(self):
        
        score=[]
        for oneObjectTemplate in self.graphTemplates:
            Matching.__init__(self, self.subgraphG1, self.subgraphG2, self.imageTemplate)        
            Hl=self.create_Hl()
            Hr=self.create_Hr()
            H=[[[[0]*len(Hr[0][0][0])]*len(Hr[0][0])]*len(Hr[0])]*len(Hr)
            for i in range(len(Hr)):
                for j in range(len(Hr[0])):
                    for k in range(len(Hr[0][0])):
                        for l in range(len(Hr[0][0][0])):
                            H[i][j][k][l]=Hr[i][j][k][l]*Hl[i][j][k][l]
            
            #score.append(self.compute_X(H))
            score.append(self.compute_X())
        
        minScore=min(score)
        print  "minScore",minScore 
        if minScore<self.minMatchingScore:
            self.current_ob=score.index(minScore)
        else:
            self.current_ob+=1

    def compute_G1(self):   
        #add the new current object to G1 
        H=nx.DiGraph(self.topoMap)
        
        #create subgraph
        descendents=list(H.successors(self.newObj))
        self.subgraphG1=nx.subgraph(self.topoMap,[self.newObj,descendents])

    def compute_G2(self):
        for ob in self.topoMap.nodes:
                if ob not in  self.subgraphG1.nodes:
                nbunch.append(ob)
        self.subgraphG2=nx.subgraph(self.topoMap,nbunch)
        





