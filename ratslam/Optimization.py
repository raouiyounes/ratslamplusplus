import random
import networkx as nx
from OpenGL.GL.feedback import Vertex
import numpy as np
import math
from match_ponce import Matching
from docutils.nodes import image
import pdb
#pdb.set_trace()

'''
Created on 23 fevr. 2018

@author: younes
'''




class DbObjects:

    def __init__(self, objectsDb):
        self.objectsDb = objectsDb
        self.e_max = 150
        self.topoMap = nx.Graph()
        self.topoMapT=nx.Graph()
        self.constructGraph()
        self.VertexObject = []
    def constructGraph(self):

        index=0
        for ob in self.objectsDb:
            self.topoMap.add_node(ob)

        for vx_0 in self.topoMap:
            for vx_1 in self.topoMap:
                if vx_0 != vx_1:
                    e = self.normal(vx_0.cv, vx_1.cv)
                    if e<self.e_max:
                        self.topoMap.add_edge(vx_0, vx_1)

    def normal(self, cvi, cvj):
        sigma = 0.2
        mean = math.sqrt((cvi[0] - cvj[1]) ** 2 + (cvj[0] - cvj[1]) ** 2)
        e = np.random.normal(mean, sigma, 1000)
        return np.mean(e)

    def getVectex(self, indexOfVertex):

        return self.topoMap.node(self.objectsDb[indexOfVertex])

    def update(self, obj_i):
        self.topoMap.add_node(obj_i)



class currentObject(Matching):

    def __init__(self, db):
        self.subgraphG1 = None
        self.subgraphG2 = None
        self.db = db

    def on_object(self, newObj):

        self.newObj=newObj


    # ompare between the actual graph and all the graphs of objects
    def OptimizationScore(self):
        score = []
        Matching.__init__(self, self.subgraphG1, self.subgraphG2, self.imageTemplate)
        Hl = self.create_Hl()
        Hr = self.create_Hr()
        H = [[[[0] * len(Hr[0][0][0])] * len(Hr[0][0])] * len(Hr[0])] * len(Hr)
        for i in range(len(Hr)):
            for j in range(len(Hr[0])):
                for k in range(len(Hr[0][0])):
                    for l in range(len(Hr[0][0][0])):
                        H[i][j][k][l] = Hr[i][j][k][l] * Hl[i][j][k][l]

        # score.append(self.compute_X(H))
        score.append(self.compute_X())

        minScore = min(score)
        print("minScore", minScore)
        if minScore < self.minMatchingScore:
            self.current_ob = score.index(minScore)
        else:
            self.current_ob += 1

    def compute_G1(self):
        # add the new current object to G1


        self.H = nx.DiGraph(self.db.topoMap)
        if self.newObj in self.H:
            descendents = list(self.H.successors(self.newObj))
            print("descendent",len(descendents))
            self.subgraphG1 = self.H.subgraph(descendents)
        else: print("it is not in the graph")
    def compute_G2(self):
        self.subgraphG2=self.H.copy()
        print("talle db",len(self.H))

        self.subgraphG2.remove_nodes_from(n for n in self.subgraphG1 if n in self.H)





