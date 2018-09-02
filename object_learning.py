import os
import numpy as np
import cv2
from matplotlib import pyplot as plt
import pdb
import math

database=open("db.txt","w")

class LearnToDetect:
	Descriptors=[]
	points_of_all_images=[]

	def __init__(self,path_of_db):
		self.path_of_db=path_of_db
		self.image_matrices=[]
		self.descriptors_of_entire_db=[]
                self.points_of_all_images=[]
                self.characteristic_scale=0.0
                self.histogram_map=dict()
                self.image_instance=[]
	def read_images(self):
		path_of_objects="/home/younes/Images/ratslam_test/rospyy/object/"
		for image_name in os.listdir(self.path_of_db):

			self.image_matrices.append(cv2.imread(path_of_objects+image_name,1))
			
	def extract_surf(self):
		#pdb.set_trace()
		# threshold of the Hessian
		orb=cv2.ORB_create(400)
		for i in range(len(self.image_matrices)):
			#print "object's number : ", i 

                    kp,des=orb.detectAndCompute(self.image_matrices[i],None)
                    self.descriptors_of_entire_db.append([des,i])
                    
		 	#for ikp in range(len(kp1)):
                         #   self.points_of_all_images.append([kp1[ikp].pt[0],kp1[ikp].pt[1]])

                    self.image_instance=self.image_matrices[0]
                    for i1 in range(len(kp)):
                        self.compute_scale(kp[i1].pt[0],kp[i1].pt[1])
                        scale=self.characteristic_scale
                        orientations=self.histogram_map
                        database.write(str(kp[i1].pt[0])+" "+str(kp[i1].pt[1])+" "+str(scale)+" "+str(orientations))
                        database.write("\n")

	
	def compute_scale(self,x,y):
            #pdb.set_trace()
            image =self.image_instance
            
            patch=image[x-4:x+4,y-4:y+4]  #si l'image est en couleur
        
            height=np.size(image,0)
            width=np.size(image,1)
            scales= [i for i in np.arange(1,5.0,0.1)]
            s00=len(scales)
            x_window=range(int(x)-4,int(x)+4)
            y_window=range(int(y)-4,int(y)+4)
            
            g=np.zeros((len(x_window),len(y_window),s00),np.float32)
            filtered=[]
	    if x-4>0 and x+4<width  and y-4>0 and y+4<height:
			x_window=range(int(x)-4,int(x)+4)
			y_window=range(int(y)-4,int(y)+4)
                        for i in range(len(x_window)):
                            for j in range(len(y_window)):
                                    for s in range(len(scales)):
                                        #g[i][j][s]=(1/(math.sqrt(2*math.pi)*scales[s]))*np.exp(-(x_window[i]**2+y_window[j]**2)/(2*(scales[s]**2)))
                                        g[i][j][s]=np.random.normal(math.sqrt(x_window[i]**2+y_window[j]**2), scales[s], 1)
            
            filtered=[]
	    
	    un=np.ones([3,3])
	    #pdb.set_trace()
	    for s in range(s00):
                
                filtered.append(cv2.filter2D(patch, -1,g[:,:,s]))
	    
	    sc=[0]*(len(scales))
	    for s in range(len(scales)):
                sc[s]=np.sum(filtered[s])
	    self.characteristic_scale=sc.index(max(sc))



	
	    # set a histogram of orientations
            histogram=range(1,360,10)
            for i in range(len(histogram)):
                self.histogram_map[histogram[i]]=0
            theta=np.zeros([s00,3])
            laplacian_of_scaledpatch=[0]*s00
            r=[0]*s00
            for s in range(s00):
                x,y=3,3
                
                patch_filtered=filtered[s]
                theta[s][0]=math.atan((-patch_filtered[x][y+1][0]+patch_filtered[x][y-1][0])/(-patch_filtered[x+1][y][0]+patch_filtered[x-1][y][0]))
                theta[s][1]=math.atan((-patch_filtered[x][y+1][1]+patch_filtered[x][y-1][1])/(-patch_filtered[x+1][y][1]+patch_filtered[x-1][y][1]))
                theta[s][2]=math.atan((-patch_filtered[x][y+1][2]+patch_filtered[x][y-1][2])/(-patch_filtered[x+1][y][2]+patch_filtered[x-1][y][2]))
                laplacian_of_scaledpatch[s]=np.linalg.norm(cv2.Laplacian(patch_filtered[0:3][0:3][:],cv2.CV_64F))
                r[s]=math.sqrt((patch_filtered[x][y+1][2]-patch_filtered[x][y-1][2])**2+(patch_filtered[x+1][y][2]-patch_filtered[x-1][y][2])**2)
            angle_degree=np.zeros([s00,3])
            distance_angle_histo=[0]*len(histogram)
            for s in range(s00):
                for color_index in range(3):
                    angle_degree[s][color_index]=theta[s][color_index]*180/(math.pi)
                    for i in range(len(histogram)):
                        distance_angle_histo[i]=abs(-histogram[i]+angle_degree[s][color_index])
                    index_of_bin=distance_angle_histo.index(np.min(distance_angle_histo))
                    self.histogram_map[histogram[index_of_bin]]+=1
            print self.histogram_map
            
            #print theta
            
	
	
class Recognition:
	#pdb.set_trace()
	def __init__(self,image_path):
		self.im_test_matrix=cv2.imread(image_path,1)
		self.keypoint=[]
		self.descriptor=[]

	def extract_features_of_test(self):
		surf=cv2.ORB_create()
		self.keypoint,self.descriptor=surf.detectAndCompute(self.im_test_matrix,None)
		plt.imshow(self.im_test_matrix)
		plt.show()
	def matching(self,des2_db):
		bf=cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck=True)
		matches=bf.match(self.descriptor,des2_db)
		matches=sorted(matches,key=lambda x:x.distance)



		
		





learn_object=LearnToDetect("/home/younes/Images/ratslam_test/rospyy/object")
learn_object.read_images()
learn_object.extract_surf()

keypoints=learn_object.points_of_all_images
#reco=Recognition("/home/younes/Images/testIm/test.jpg")
#reco.extract_features_of_test()









