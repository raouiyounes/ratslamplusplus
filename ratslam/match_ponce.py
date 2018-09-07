import math
import cv2
import numpy as np
import pdb
from cmath import sqrt
class Object:
	def __init__(self):
		self.x_i=0
		self.y_i=0
		self.lv=''
class Matching:

	def __init__(self,V1,V2,all_images):
		self.THRESHOLD_SURF_MATCH=1
		self.V1=V1
		self.V2=V2
		self.all_views=all_images
		Vl_1=list(self.V1.nodes)
		Vl_2=list(self.V2.nodes)
		self.Hl=[]
		self.Hr=[]
		self.surf=cv2.xfeatures2d.SURF_create(400)
		self.matchX1X2=0
		
	def normalfx(self,cv_i,cv_j):
		 mean=[cv_i[0]-cv_j[0],cv_i[1]-cv_j[1]]
		 return np.random.multivariate_normal(mean,[[1, 0], [0, 100]],2)
	
	
	
	'''def kNearestNeighbors(self):
		Vl_1=list(self.V1.objects.nodes)
		Vl_2=list(self.V2.objects.nodes)
		
		
		
		for ob_graph in Vl_2:
			ob=[ob_graph.cv[0],ob_graph.cv[1],ob_graph.indexOfView]
			
			
		knn=cv2.KNearest()
			knn.train
			
	'''
		
		
	
	def create_Hr(self):
		Vl_1=list(self.V1.nodes)
		Vl_2=list(self.V2.nodes)
		emax=2
		for i1 in Vl_1:
			Hj3=[]
			for i2 in Vl_2:
				Hj2=[]
				for j1 in Vl_1:
					Hj1=[]
					for j2 in Vl_2:
						cv11=[i1.cv[0],i1.cv[1]]
						cv12=[j1.cv[0],j1.cv[1]]
						e_i1_j1=self.normalfx(cv11,cv12)
						e_i1_j1=e_i1_j1[0]
						
						cv21=[i2.cv[0],i2.cv[1]]
 						cv22=[j2.cv[0],j2.cv[1]]
 						e_i2_j2=self.normalfx(cv21,cv22)
 						e_i2_j2=e_i2_j2[0]
 						Hj1.append(emax-math.sqrt((e_i1_j1[0]-e_i2_j2[0])**2+(e_i1_j1[1]-e_i2_j2[1])**2))
 					Hj2.append(Hj1)
 		 		Hj3.append(Hj2)
 			self.Hr.append(Hj3)
 		return self.Hr
 	
	
	
	
	'''
	def create_Hr(self):
		Vl_1=list(self.V1.objects.nodes)
		Vl_2=list(self.V2.objects.nodes)
		emax=2
		for i1 in Vl_1:
			Hj3=[]
			for i2 in Vl_2:
				Hj2=[]
				for j1 in Vl_1:
					Hj1=[]
					for j2 in Vl_2:
						cv11=[i1.cv[0],i1.cv[1]]
						cv12=[j1.cv[0],j1.cv[1]]
						e_i1_j1=self.normal(cv11,cv12)
						e_i1_j1=e_i1_j1[0]
						cv21=[i2.cv[0],i2.cv[1]]
 						cv22=[j2.cv[0],j2.cv[1]]
 						e_i2_j2=self.normal(cv21,cv22)
 						e_i2_j2=e_i2_j2[0]
 						Hj1.append(emax-math.sqrt((e_i1_j1[0]-e_i2_j2[0])**2+(e_i1_j1[1]-e_i2_j2[1])**2))
 					Hj2.append(Hj1)
 		 		Hj3.append(Hj2)
 			self.Hr.append(Hj3)
 		return self.Hr
 	'''
	def create_Hl(self):
		Vl_1=list(self.V1.nodes)
		Vl_2=list(self.V2.nodes)
		for i1 in Vl_1:
			Hj3=[]
			for i2 in Vl_2:
				Hj2=[]
				for j1 in Vl_1:
					Hj1=[]
					for j2 in Vl_2:
						if (i1.lv==i2.lv  and  j1.lv==j2.lv):
							Hj1.append(1)
						else:	
							Hj1.append(0)
					Hj2.append(Hj1)
				Hj3.append(Hj2)
			self.Hl.append(Hj3)
		return self.Hl
	def match_points(self,ob1,ob2):
		indexOb1=ob1.indexOfView
		indexOb2=ob2.indexOfView
		imOb1=self.all_views[indexOb1-1]
		imOb2=self.all_views[indexOb2-1]
		obj1X=ob1.cv[0]
		obj1Y=ob1.cv[1]
		obj2X=ob2.cv[0]
		obj2Y=ob2.cv[1]
		ptOb1=[cv2.KeyPoint(obj1X,obj1Y,10)]
		surfObj1=self.surf.compute(imOb1,ptOb1)
		ptOb2=[cv2.KeyPoint(obj2X,obj2Y,10)]
		surfObj2=self.surf.compute(imOb2,ptOb2)
		descObj1=surfObj1[1][0]
		descObj2=surfObj2[1][0]
		diff2desc=[j-i for i,j in zip(descObj1,descObj2)]
		matchscorei=abs(sum(diff2desc))
		if np.sqrt(matchscorei)> abs(np.mean(diff2desc)): #self.THRESHOLD_SURF_MATCH:
			return 1
		else:
			return 0
		
	def compute_X(self,H):
		Vl_1=list(self.V1.nodes)
		Vl_2=list(self.V2.nodes)
		scoreX=0
		Hl=self.Hl
		X1=[[0]*len(Hl[0])]*len(Hl)
		X2=[[0]*len(Hl[0][0][0])]*len(Hl[0][0])
		for i1 in range(len(Hl)):
			for i2 in range(len(Hl[0])):
				for j1 in range(len(Hl[0][0])):
					for j2 in range(len(Hl[0][0][0])):
						ob1=Vl_1[i1]
						ob2=Vl_2[i2]
						X1[i1][i2]=self.match_points(ob1,ob2)
						ob1=Vl_1[j1]
						ob2=Vl_2[j2]
						X2[j1][j2]=self.match_points(ob1,ob2)
						x1_ind=X1[i1][i2]
						x2_ind=X2[j1][j2]
						h_ind=H[i1][i2][j1][j2]
						def computeScoreX(h_ind,x1_ind,x2_ind):
							return  h_ind*x1_ind*x2_ind 
						scoreX+=computeScoreX(h_ind,x1_ind,x2_ind)
		return scoreX		

	
	def create_Hstar(self):
		self.Hstar=self.Hr*self.Hl
