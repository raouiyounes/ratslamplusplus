


class packet:
	def __init__(self):
		self.x=[]
		self.y=[]
		self.th=[]


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
		
		for i in len(mapR):
			
			landmark2Object=observation[i]
			if objectR.cv== landmark2Object.cv and objectR.lv==landmark2Object.lv and match(objectR.indexOfView,landmark2Object.indexOfView)==1:
				
				for j in len(packetCAN):
					
					distPoseLand=sqrt((packetCAN[j]
					
					
				
				
				
			
		
		
		
		
		
	
