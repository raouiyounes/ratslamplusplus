import os
import numpy as np
import cv2
from matplotlib import pyplot as plt
import pdb
import math
from numpy import array
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
                self.desglob=[]
                self.kpglob=[]
	def read_images(self):
		path_of_objects="/home/younes/Images/ratslam_test/rospyy/src/ratslam_ros/src/objects/"
		for image_name in os.listdir(path_of_objects):

			self.image_matrices.append(cv2.imread(path_of_objects+image_name,1))
	def extract_surf(self):
		#pdb.set_trace()
		# threshold of the Hessian
		orb=cv2.ORB_create(400)
		print "aaaaaaaaaaaa",len(self.image_matrices)
		for i in range(len(self.image_matrices)):
                    object_index=i
			#print "object's number : ", i 
                    kp=orb.detect(self.image_matrices[i],None)
                    kp,des=orb.compute(self.image_matrices[i],kp)
                    self.desglob+=list(des)
                    self.kpglob+=list(zip(  [kp[x].pt[0] for x in range(len(kp))] ,[kp[y].pt[1] for y in range(len(kp))],[kp[s].size for s in range(len(kp))],[self.histogram_of_orientation(kp[th].angle) for th in range(len(kp))],[object_index]*len(kp)))    
                
                
                for j in range(len(kp)):
                    self.descriptors_of_entire_db.append(des[j])
                    self.descriptors_of_entire_db.append(i)

                    #for ikp in range(len(kp1)):
                        #   self.points_of_all_images.append([kp1[ikp].pt[0],kp1[ikp].pt[1]])

                self.image_instance=self.image_matrices[i]
                for i1 in range(len(kp)):
                    scale=kp[i1].size
                    orientations=self.histogram_of_orientation(kp[i1].angle)
                    database.write(str(kp[i1].pt[0])+" "+str(kp[i1].pt[1])+" "+str(scale)+" "+str(orientations))
                    database.write("\n")

	
	def histogram_of_orientation(self,angle):
	
	
	 # set a histogram of orientations
            histogram_map=dict()
            histogram=range(1,360,10)
            for i in range(len(histogram)):
                histogram_map[histogram[i]]=0
            distance_angle_histo=[0]*len(histogram)

            for i in range(len(histogram)):
                distance_angle_histo[i]=abs(-histogram[i]+angle)
            index_of_bin=distance_angle_histo.index(np.min(distance_angle_histo))
            #print index_of_bin
            histogram_map[histogram[index_of_bin]]+=1
            return histogram_map
	
	
class Recognition(LearnToDetect):
	#pdb.set_trace()
	def __init__(self):
		frame=cv2.imread("/home/younes/Bureau/ratslampy/node_example/src/test.jpg",1)
                self.im_test_matrix = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		self.keypoint=[]
		self.descriptor=[]
	def extract_features_of_test(self):
		surf=cv2.ORB_create()
		self.keypoint,self.descriptor=surf.detectAndCompute(self.im_test_matrix,None)
            
	
	
	def matching_1(self,des2_db,K_points):
                #pdb.set_trace()
                desco=np.ones(len(des2_db[0]))
		desc_np=np.zeros([len(des2_db),len(des2_db[0])])
		
		for i in range(len(des2_db)):
                    desc_np[i]=des2_db[i]
		bf=cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck=True)
		matches=bf.match(np.array(self.descriptor),np.array(des2_db))
                return matches
        def construct_votes_structure(self,matches,K_points):
                #pdb.set_trace()

                votes=[0]*len(self.keypoint)
                
                for i in range(len(matches)):
                    votes[matches[i].queryIdx]=K_points[matches[i].trainIdx]
                print votes
                x_coord=[0]*len(K_points)
                y_coord=[0]*len(K_points)
                scale_coord=[0]*len(K_points)
                orient_coord=[0]*len(K_points)
                
                for i in range(len(K_points)):
                    x_coord[i]=K_points[i][0]
                    y_coord[i]=K_points[i][1]
                    scale_coord[i]=K_points[i][2]
                    orient_coord[i]=K_points[i][3]
                
                # this loop creates the hough space
                for j in range(len(self.keypoint)):
                    
                    pose=votes[j]
                    histogram_angles=range(1,360,10)
            
                    x=pose[0]
                    y=pose[1]
                    size=pose[2]
                    theta=self.histogram_of_orientation(pose[2])
                    xdiff=[a-b for a,b in zip( x_coord,[x]*len(x_coord))]
                    hough[j][0]=xdiff.index(min(xdiff)) 
                    hough[j][1]=y_coord.index(min(y_coord-[y]*len(y_coord)))
                    hough[j][2]=scale_coord.index(min(scale_coord-size))
                    for k in range(len(orient_coord)):
                        tdiff[k]=max(theta-orient_coord[k])
                    min_orient_index=orient_coord.index(min(orient_coord))
                    orient_index=min_orient_index.index(max(min_orient_index))
                    hough[j][3]=min_orient_index
                    
                
        #def geometrical_verification(self):
                    
	def matching(self,des2_db,K_points):
                #pdb.set_trace()
                desco=np.ones(len(des2_db[0]))
		desc_np=np.zeros([len(des2_db),len(des2_db[0])])
		
		for i in range(len(des2_db)):
                    desc_np[i]=des2_db[i]
		bf=cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck=True)
		matches=bf.match(np.array(self.descriptor),np.array(des2_db))
		
		#matches=sorted(matches,key=lambda x:x.distance)
                
                #chaque keypoint dans l'image test et son correspondant
                vote_vues=[0]*len(matches)
                print "rrrr",len(K_points)
                
                for i in range(len(matches)):
                    vote_vues[i]=K_points[matches[i].trainIdx][-1]
                criteria=(cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER,10,1.0)
                ret,label,center=cv2.kmeans(np.float32(vote_vues),4,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
                
                print "eee",label
                
                a=list()
                # les features dans l'image test qui votent sur la meme pose(vue) 
                #for i in label:
                    
                    #indice=(i for i,v in enumerate(label) if v==i)
                    #print list(indice)
                    #a=vote_vues[indice[0:4]]
                    #print a

                print label
                # "ee",matches
                hash_vues={0:[],1:[],2:[],3:[],4:[],5:[],6:[]}
                for j in range(5):
                    for i in range(len(label)):
                        #print label[i]
                        if (label[i]==j):
                            hash_vues[j].append(i)
                            
                print hash_vues

		
		



#pdb.set_trace()

learn_object=LearnToDetect("/home/younes/Bureau/ratslampy/node_example/src")
learn_object.read_images()
learn_object.extract_surf()
reco=Recognition()

reco.extract_features_of_test()

print len(learn_object.kpglob)

reco.matching(learn_object.desglob,learn_object.kpglob)
x=reco.matching_1(learn_object.desglob,learn_object.kpglob)
reco.construct_votes_structure(x,learn_object.kpglob)

keypoints=learn_object.points_of_all_images
#reco=Recognition("/home/younes/Images/testIm/test.jpg")
#reco.extract_features_of_test()









