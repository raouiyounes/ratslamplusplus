


class packet:
	def __init__(self):
		self.x=[]
		self.y=[]
		self.th=[]

class Map:
	def __init__(self):
		self.muX=0
		self.muY=0
		self.muZ=0
		self.vObject=Vertex()



class Robot: 
    def __init__(self):
        self.x=random.random()*world_size
        self.y=random.random()*world_size
        self.orientation=random.random()*2.0*pi
        self.forward_noise=0.0
        self.turn_noise=0.0
        self.sense_noise=0.0

class FASTSlam:
	
	def __init__(self,groundTruth):
		
		
		pk=packet()
		self.truePose=groundTruth	
		# all the poses of the robot as obtained from pcn
		self.packetS=[]
		self.mapR=[]
		self.observation=[]
		self.Rt=0.2*np.eye(2,2)
		self.EXP_INITIAL_EM_DEG=90.0
        self.accum_delta_facing=self.EXP_INITIAL_EM_DEG*math.pi/180
		self.accum_delta_x=0
		self.accum_delta_y=0		
		# particles
		self.p=[]
		self.objectObsDb=dict()
		
	
	def initiateParticles(self):
		for i in range(1000):
			r=Robot()
			self.p.append(r)
		
	# receive packet from can and place it in a list
	
	# computation of a fingerprint of the observations of objects
	def computeFingerPrint(self):
		#objects detected objects at time t
		detectedObj=dict()
		for i in len(objects):
			ob=objects[i]
			if ob in self.objectObsDb:
				detectedObj[ob]+=1
			else:
				detectedObj[ob]=1
		for i in detectedObj:
			if i in self.objectObsDb :
				self.objectObsDb[i]+=1
			else:
				self.objectObsDb[i]=1
				
		return detectedObj
	
	
	def setPacket(self,packetCAN):
		pk=packet()
		pk.x=packetCAN.x
		pk.y=packetCAN.y
		pk.th=packetCAN.th
		self.packets.append(pk)
	# compute the 3D coordinate of an object	
	
	
	def getWeights(self):
		
	
	def RaoBlackwellizedF(self):
		myrobot=robot()
		for i in len(self.p):
			r=robot()
            r.set_noise(0.05, 0.05, 5.0)
			p.append(r)
		 myrobot=myrobot.move(0.1,0.5)
		 p2=[]
         for i in range(N):
			 p2.append(p[i].move(0.1,0.5))
		 p=p2
		 w=getWeights()
		 
		  
			
	
	def t3DObject(self,objectR):
		
	# data association
	def mapping(self,objectR,packetCAN,vtrans,vrot,time_diff_s):
		
		# computation of the true positions
		vtrans=vtrans*time_diff_s
        vrot*=time_diff_s
        self.accum_delta_facing=self.clip_rad_180(self.accum_delta_facing+vrot)
        self.accum_delta_x=self.accum_delta_x+vtrans*math.cos(self.accum_delta_facing)
        self.accum_delta_y=+vtrans*math.sin(self.accum_delta_facing)
        self.accum_delta_time_s+=time_diff_s
 #tracking of features
 
 # ading a loop that interates on all the objects of a precise view
		numberOflandmarks=0
		
		if (len(self.mapR)!=0):
			for i in len(self.mapR):
				#data association
				landmark2Object=landm2Feat(self.mapR[i])
				#active search
				if objectR.cv== landmark2Object.cv and objectR.lv==landmark2Object.lv and match(objectR.indexOfView,landmark2Object.indexOfView)==1:
					distPoseLand=np.zeros(len(packetCAN.x))
					direcPoseLand=np.zeros(len(packetCAN.x))
					# Update Kalman Filters
					for j in len(packetCAN):
						Mu=[mapR[i].x,mapR[i].y]
						distPoseLand[j]=sqrt((packetCAN.x[j]-Mu[0])**2+(packetCAN.y[j]-Mu[1])**2)
						direcPoseLand[j]=math.atan((packetCAN.y[j]-Mu[1])/(packetCAN.x[j]-Mu[0]))
					
						TruedistPoseLand[j]=sqrt((self.accum_delta_x-Mu[0])**2+(self.accum_delta_y-Mu[1])**2)
						TruedirecPoseLand[j]=math.atan((self.accum_delta_y-Mu[1])/(self.accum_delta_x-Mu[0]))
					
						G=self.ComputeJacobG([packetCAN.x[j],packetCAN.y[j]],Mu,distPoseLand[j])
						Qn=np.transpose(G)*Cov*G+self.Rt
						
						zt_pred=[distPoseLand[j] direcPoseLand[j]]
						zt_measure=[TruedistPoseLand[j],TruedirecPoseLand[j]]
						wn=sqrt(np.abs(2*math.pi*Qn))**-1*np.exp(-0.5*(
						K=Cov*G*np.linalg.inv(Q)
						Cov=(np.eye(3,3)-K*G)*Cov
						self.updateMeasCova()
				
				else:
					numberOflandmarks+=1
		
			if numberOflandmarks==len(mapR)-1:
				Mu=self.feat3land(objects)
				map_i=Map()
				map_i.muX=Mu[0]
				map_i.muY=Mu[1]
				map_i.muZ=Mu[2]
				map_i.vObject=objectR
				self.mapR.append(map_i)
				
				
			
				
				
	 def ComputeJacobG(self,poseOfPartic,poseOflandM,r):
		 
		 return [[poseOfPartic[0]-poseOflandM[0], poseOfPartic[1]-poseOflandM[1],0],[(poseOflandM[1]-poseOfPartic[1])/r, (poseOfPartic[0]-poseOflandM[0])/r,-1]]
		 
				
				
				
	def isRobPerceLand(self,dis,dire):
		# verifiying the values from which we can say that there is an observation
				
				
			
		
		
		
		
		
	
