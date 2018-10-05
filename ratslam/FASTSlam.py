


class packet:
	def __init__(self):
		self.x=[]
		self.y=[]
		self.th=[]

class Map:
	def __init__(self):
		self.muX=[]
		self.muY=[]
		self.muZ=[]
class FASTSlam:
	
	def __init__(self):
		
		pk=packet()
			
		# all the poses of the robot as obtained from pcn
		self.packetS=[]
		self.mapR=[]
		self.observation=[]
		
	# receive packet from can and place it in a list
	def setPacket(self,packetCAN):
		
		pk=packet()
		pk.x=packetCAN.x
		pk.y=packetCAN.y
		pk.th=packetCAN.th
		self.packets.append(pk)
	
	
	# compute the 3D coordinate of an object	
	def t3DObject(self,objectR):
		
		
		
	
	# data association
	def dataAssociation(self,objects,packetCAN):
		numberOflandmarks=0
		for i in len(mapR):
			
			landmark2Object=landm2Feat(mapR[i])
			if objectR.cv== landmark2Object.cv and objectR.lv==landmark2Object.lv and match(objectR.indexOfView,landmark2Object.indexOfView)==1:
				distPoseLand=np.zeros(len(packetCAN.x))
				direcPoseLand=np.zeros(len(packetCAN.x))
				for j in len(packetCAN):
					
					
					Mu=[mapR[i].x,mapR[i].y]
					
					distPoseLand[j]=sqrt((packetCAN.x[j]-Mu[0])**2+(packetCAN.y[j]-Mu[1])**2)
					direcPoseLand[j]=math.atan((packetCAN.y[j]-Mu[1])/(packetCAN.x[j]-Mu[0]))
					if (self.isRobPerceLand(distPoseLand[j],direcPoseLand[j])==True):
						self.ComputeJacobG([packetCAN.x[j],packetCAN.y[j]],Mu)
						numberOflandmarks+=1
	
		if numberOflandmarks!=len(mapR)-1:
			
			
			
			
			
		for i in len(poseMap):
			for j in len(poseMap[0]):
				
				of poseMap[i][j]==True:
					
				
				
	 def ComputeJacobG(self,poseOfPartic,poseOflandM):
		 
		 return [[poseOfPartic[0]-poseOflandM[0], poseOfPartic[1]-poseOflandM[1],0],[poseOflandM[1]-poseOfPartic[1], poseOfPartic[0]-poseOflandM[0],-1]]
		 
				
				
				
	def isRobPerceLand(self,dis,dire):
		# verifiying the values from which we can say that there is an observation
				
				
			
		
		
		
		
		
	
