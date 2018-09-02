import numpy as np
import math
import itertools
import numpy
from enum import Enum
from pylab import *
import sys
import pdb
class PosecellExperience: 
    x_pc = 0.0
    y_pc = 0.0
    th_pc = 0.0
    vt_id = 0

class PosecellVisualTemplate:
    pc_x = 0.0
    pc_y = 0.0
    pc_th = 0.0
    decay = 0.0
    exps = [];

    def __init__(self):

        self.pc_x = 0.0
        self.pc_y = 0.0
        self.pc_th = 0.0
        self.decay = 0.0
        self.exps = [];


class PosecellNetwork:
    PosecellAction=Enum('PosecellAction','NO_ACTION,CREATE_NODE,CREATE_EDGE,SET_NODE',start=0)

    visual_templates=[]
    experiences=[]
        
    def __init__(self):
        #pdb.set_trace()
        self.PC_VT_INJECT_ENERGY = 0.1
        self.PC_DIM_XY = 21
        self.PC_DIM_TH = 36
        self.PC_W_E_VAR = 1
        self.PC_W_E_DIM = 7
        self.PC_W_I_VAR = 2
        self.PC_W_I_DIM = 5
        self.PC_GLOBAL_INHIB = 0.00002
        # self.PC_W_EXCITE = self.create_pc_weights(self.PC_W_E_DIM, self.PC_W_E_VAR)
        # self.PC_W_INHIB = self.create_pc_weights(self.PC_W_I_DIM, self.PC_W_I_VAR)
        self.PC_W_EXCITE = np.zeros(self.PC_W_E_DIM * self.PC_W_E_DIM * self.PC_W_E_DIM)
        self.PC_W_INHIB = np.zeros(self.PC_W_E_DIM * self.PC_W_E_DIM * self.PC_W_E_DIM)
        self.PC_W_E_DIM_HALF = int(np.floor(self.PC_W_E_DIM / 2.))
        self.PC_W_I_DIM_HALF = int(np.floor(self.PC_W_I_DIM / 2.))
        self.PC_C_SIZE_TH = (2.*np.pi) / self.PC_DIM_TH
        # self.PC_E_XY_WRAP = range(self.PC_DIM_XY - self.PC_W_E_DIM_HALF, self.PC_DIM_XY) + range(self.PC_DIM_XY) + range(self.PC_W_E_DIM_HALF)
        self.pca_new_memory=np.zeros((self.PC_DIM_XY+2)**2)
        
        self.PC_E_XY_WRAP = range(self.PC_DIM_XY + self.PC_W_E_DIM - 1)
        self.PC_E_XY_WRAP = self.generate_wrap(self.PC_E_XY_WRAP, self.PC_DIM_XY - self.PC_W_E_DIM_HALF, self.PC_DIM_XY, 0, self.PC_DIM_XY, 0, self.PC_W_E_DIM_HALF);
        self.PC_E_TH_WRAP = range(self.PC_DIM_TH + self.PC_W_E_DIM - 1)
        
        self.PC_E_TH_WRAP = self.generate_wrap(self.PC_E_TH_WRAP, self.PC_DIM_TH - self.PC_W_E_DIM_HALF, self.PC_DIM_TH, 0, self.PC_DIM_TH, 0, self.PC_W_E_DIM_HALF);
        
        
       # self.PC_E_TH_WRAP = range(self.PC_DIM_TH - self.PC_W_E_DIM_HALF, self.PC_DIM_TH) + range(self.PC_DIM_TH) + range(self.PC_W_E_DIM_HALF)
        self.PC_I_XY_WRAP = range(self.PC_DIM_XY - self.PC_W_I_DIM_HALF, self.PC_DIM_XY) + range(self.PC_DIM_XY) + range(self.PC_W_I_DIM_HALF)
        self.PC_I_TH_WRAP = range(self.PC_DIM_TH - self.PC_W_I_DIM_HALF, self.PC_DIM_TH) + range(self.PC_DIM_TH) + range(self.PC_W_I_DIM_HALF)            
        self.PC_CELL_X_SIZE = 0.015
        self.PC_XY_SUM_SIN_LOOKUP = np.sin(np.multiply(range(1, self.PC_DIM_XY + 1), (2 * np.pi) / self.PC_DIM_XY))
        self.PC_XY_SUM_COS_LOOKUP = np.cos(np.multiply(range(1, self.PC_DIM_XY + 1), (2 * np.pi) / self.PC_DIM_XY))
        self.PC_TH_SUM_SIN_LOOKUP = np.sin(np.multiply(range(1, self.PC_DIM_TH + 1), (2 * np.pi) / self.PC_DIM_TH))
        self.c_size_th = math.pi / 18
        self.PC_TH_SUM_COS_LOOKUP = np.cos(np.multiply(range(1, self.PC_DIM_TH + 1), (2 * np.pi) / self.PC_DIM_TH))
        self.PC_CELLS_TO_AVG = 3;
        self.PC_CELLS_X_SIZE=1.0
        self.PC_AVG_XY_WRAP = range(self.PC_DIM_XY + 2 * self.PC_CELLS_TO_AVG)  # + range(self.PC_DIM_XY) + range(self.PC_CELLS_TO_AVG)
        self.PC_AVG_TH_WRAP = range(self.PC_DIM_TH + 2 * self.PC_CELLS_TO_AVG)  # , self.PC_DIM_TH) + range(self.PC_DIM_TH) + range(self.PC_CELLS_TO_AVG)
        self.generate_wrap(self.PC_AVG_XY_WRAP,self.PC_DIM_XY-self.PC_CELLS_TO_AVG,self.PC_DIM_XY, 0, self.PC_DIM_XY,0,self.PC_CELLS_TO_AVG)
        self.generate_wrap(self.PC_AVG_TH_WRAP,self.PC_DIM_TH-self.PC_CELLS_TO_AVG, self.PC_DIM_TH, 0,self.PC_DIM_TH,0,self.PC_CELLS_TO_AVG)
        
        self.IMAGE_Y_SIZE = 640
        self.IMAGE_X_SIZE = 480
        self.IMAGE_VT_Y_RANGE = slice((480 / 2 - 80 - 40), (480 / 2 + 80 - 40))
        self.IMAGE_VT_X_RANGE = slice((640 / 2 - 280 + 15), (640 / 2 + 280 + 15))
        self.IMAGE_VTRANS_Y_RANGE = slice(270, 430)
        self.IMAGE_VROT_Y_RANGE = slice(75, 240)
        self.IMAGE_ODO_X_RANGE = slice(180 + 15, 460 + 15)
        self.VT_GLOBAL_DECAY = 0.1
        self.VT_ACTIVE_DECAY = 1.0
        self.VT_SHIFT_MATCH = 20
        self.VT_MATCH_THRESHOLD = 0.09
        self.EXP_DELTA_PC_THRESHOLD = 1.0
        self.EXP_CORRECTION = 0.5
        self.EXP_LOOPS = 100
        self.VTRANS_SCALE = 100
        self.VISUAL_ODO_SHIFT_MATCH = 140
        self.ODO_ROT_SCALING = np.pi / 180. / 7.
        self.POSECELL_VTRANS_SCALING = 1. / 10.
        self.C_C_SIZE_TH = (2.0 * math.pi) / self.PC_DIM_TH
        self.posecells_elements = self.PC_DIM_XY * self.PC_DIM_XY * self.PC_DIM_TH
        self.posecells_memory_size = self.PC_DIM_XY * self.PC_DIM_XY * self.PC_DIM_TH
        self.posecells_memory = numpy.zeros(self.posecells_memory_size)
        pca_new_memory = numpy.zeros(self.posecells_memory_size)
        self.avg_wdim = 7
        self.cells_avg = 3
        self.avg_dim_half = self.avg_wdim / 2
        self.current_exp=0
        self.xy_sum_sin = sin(arange(self.PC_DIM_XY) * 2 * float64(pi) / self.PC_DIM_XY)
        self.xy_sum_cos = cos(arange(self.PC_DIM_XY) * 2 * float64(pi) / self.PC_DIM_XY)
        self.th_sum_sin = sin(arange(self.PC_DIM_TH) * 2 * float64(pi) / self.PC_DIM_TH)
        self.th_sum_cos = cos(arange(self.PC_DIM_TH) * 2 * float64(math.pi) / self.PC_DIM_TH)
        self.vt_delta_pc_th=0.0
        self.avg_xywrap = range(self.PC_DIM_XY - self.avg_dim_half, self.PC_DIM_XY) + \
                          range(0, self.PC_DIM_XY) + \
                          range(0, self.PC_DIM_XY - self.avg_dim_half)
        self.avg_thwrap = range(self.PC_DIM_TH - self.avg_dim_half, self.PC_DIM_TH) + \
                          range(0, self.PC_DIM_TH) + \
                          range(0, self.PC_DIM_TH - self.avg_dim_half)

    # set up the wrap lookups
    	self.PC_W_E_DIM__ALF = self.PC_W_E_DIM / 2.0
    	self.PC_W_I_DIM_HALF = self.PC_W_I_DIM / 2.0
        # sin and cosine lookups

    	self.PC_XY_SUM_SIN_LOOKUP = []
    	self.PC_XY_SUM_COS_LOOKUP = []
    	self.PC_TH_SUM_SIN_LOOKUP = []
    	self.PC_TH_SUM_COS_LOOKUP = []
        #
        self.pca_new = zeros([self.PC_DIM_TH, self.PC_DIM_XY, self.PC_DIM_XY])
        #self.pca_new_rot_ptr2 = np.zeros(self.PC_DIM_XY + 2)
        
        self.posecells = np.zeros([self.PC_DIM_TH, self.PC_DIM_XY, self.PC_DIM_XY])

        self.current_vt=0
        xxx=PosecellVisualTemplate
        self.visual_templates.append(xxx)
        self.PC_VT_RESTORE=0.05
        s=[self.PC_DIM_XY+2,self.PC_DIM_XY+2]
        #self.pca_new_rot_ptr=np.zeros(self.PC_DIM_XY*SELF)#[[0]*(self.PC_DIM_XY+2) for i in range(self.PC_DIM_XY+2)]
        self.pca_new_rot_ptr2=[[0]*(self.PC_DIM_XY+2)*(self.PC_DIM_XY+2) for i in range((self.PC_DIM_XY+2)*(self.PC_DIM_XY+2))]
        self.pca_new_rot_ptr=[[0]*(self.PC_DIM_XY+2)*(self.PC_DIM_XY+2) for i in range((self.PC_DIM_XY+2)*(self.PC_DIM_XY+2))]

        self.posecells_plane_th=[]*(self.PC_DIM_XY+2)*(self.PC_DIM_XY+2)
        self.best_x = floor(self.PC_DIM_XY / 2.0);
        self.best_y = floor(self.PC_DIM_XY / 2.0);
        self.best_th = floor(self.PC_DIM_TH / 2.0);
        self.posecells[self.best_th][self.best_y][self.best_x] = 1;
        self.odo_update=False
        self.vt_update=False
        self.prev_vt=0
        self.DBL_MAX=sys.float_info.max

    	for i in range(self.PC_DIM_XY):
        	self.PC_XY_SUM_SIN_LOOKUP.append(math.sin(float(i + 1) + 2 * math.pi / self.PC_DIM_XY))
        	self.PC_XY_SUM_COS_LOOKUP.append(math.cos(float(i + 1) * 2 * math.pi / self.PC_DIM_XY))

    	for i in range(self.PC_DIM_TH):
        	self.PC_TH_SUM_SIN_LOOKUP.append(math.sin((float)(i + 1) + 2 * math.pi / self.PC_DIM_TH))
        	self.PC_TH_SUM_COS_LOOKUP.append(math.cos((float)(i + 1) + 2 * math.pi / self.PC_DIM_TH))

    	total = 0
    	k = 0
    	next = 0
    	dim_centre = self.PC_W_E_DIM / 2
    # define the function norm2d

    	for k in range(self.PC_W_E_DIM):
        	for j in range(self.PC_W_E_DIM):
        		for i in range(self.PC_W_E_DIM):
        			self.PC_W_EXCITE[next] = self.norm2d(self.PC_W_E_VAR, i, j, k, dim_centre)
                	total += self.PC_W_EXCITE[next]
                	next += 1
        
        for next in range(self.PC_W_E_DIM * self.PC_W_E_DIM * self.PC_W_E_DIM):
            self.PC_W_EXCITE[next] /= total
        total = 0
        dim_centre = self.PC_W_I_DIM / 2
        next = 0


    	for k in range(self.PC_W_I_DIM):
        	for j in range(self.PC_W_I_DIM):
        		for i in range(self.PC_W_I_DIM):
        			self.PC_W_INHIB[next] = self.norm2d(self.PC_W_I_VAR, i, j, k, dim_centre)
            		total += self.PC_W_INHIB[next]
            		next += 1



    	for next in range(self.PC_W_I_DIM * self.PC_W_I_DIM * self.PC_W_I_DIM):
        	self.PC_W_INHIB[next] /= total
            
    def inject(self, act_x, act_y, act_z, energy):
        if act_x < self.PC_DIM_XY and act_x >= 0 and act_y < self.PC_DIM_XY and act_y >= 0 and act_z < self.PC_DIM_TH and act_z >= 0 :
            self.posecells[act_z][act_y][act_x] += energy


    def generate_wrap(self,wrap,start1,end1,start2,end2,start3,end3):
        i=0
        for j in range(start1,end1):
            wrap[i]=j
            i+=1
        for j in range(start2,end2):
            wrap[i]=j
            i+=1
        for j in range(start3,end3):
            wrap[i]=j
            i+=1
        return 1
    
    
    def create_pc_weights(self, dim, var):
        dim_center = int(np.floor(dim / 2.))
        
        weight = np.zeros([dim, dim, dim])
        for x, y, z in itertools.product(xrange(dim), xrange(dim), xrange(dim)):
            dx = -(x - dim_center) ** 2
            dy = -(y - dim_center) ** 2
            dz = -(z - dim_center) ** 2
            weight[x, y, z] = 1.0 / (var * np.sqrt(2 * np.pi)) * np.exp((dx + dy + dz) / (2.*var ** 2))
    
        weight = weight / np.sum(weight)
        return weight
    

    def excite(self):
        self.pca_new_memory = np.zeros(self.posecells_memory_size)

        # loop in all three dimensions
        for i in range(self.PC_DIM_XY):
            for j in range(self.PC_DIM_XY):
                for k in range(self.PC_DIM_TH):
                    if self.posecells[k][i][j] != 0:
                        self.pose_cell_excite_helper(i, j, k)

        self.posecells=self.pca_new
        self.posecells_memory = self.pca_new_memory
        

    def inhibit(self):
        self.pca_new_memory = zeros(self.posecells_memory_size)
        for i in range(self.PC_DIM_XY):
            for j in range(self.PC_DIM_XY):
                for k in range(self.PC_DIM_TH):
                    if self.posecells[k][i][j] != 0 :
                        self.pose_cell_inhibit_helper(i, j, k)

        for i in range(self.posecells_elements):
            self.posecells_memory[i] -= self.pca_new_memory[i]
        
    
    
    def global_inhibit(self):
        for i in range(self.posecells_elements):
    
            if self.posecells_memory[i] >= self.PC_GLOBAL_INHIB:
                self.posecells_memory[i] = (self.posecells_memory[i] - self.PC_GLOBAL_INHIB)
            else:
                self.posecells_memory[i] = 0
        return True
    def pose_cell_excite_helper(self, x, y, z):
        excite_index = 0
        for zl in range(z, z + self.PC_W_I_DIM):
            for yl in range(y, y + self.PC_W_I_DIM):
                for xl in range(x, self.PC_W_I_DIM):
                    xw = self.PC_E_XY_WRAP[xl]
                    yw = self.PC_E_XY_WRAP[yl]
                    zw = self.PC_E_TH_WRAP[zl]
                    self.pca_new[zw][yw][xw] += self.posecells[x][y][z] * self.PC_W_EXCITE[excite_index]
                    excite_index = +1
        self.posecells=self.pca_new
        return True
    
    def pose_cell_inhibit_helper(self, x, y, z):
        inhib_index = 0


        for zl in range(z, z + self.PC_W_I_DIM):
            for yl in range(y, y + self.PC_W_I_DIM):
                for xl in range(x, self.PC_W_I_DIM):
                    xw = self.PC_I_XY_WRAP[xl]
                    yw = self.PC_I_XY_WRAP[yl]
                    zw = self.PC_I_TH_WRAP[zl]
                    self.pca_new[zw][yw][xw] += self.posecells[z][y][x] * self.PC_W_INHIB[inhib_index]
                    inhib_index += 1
        self.posecells=self.pca_new
        return True
                

    def normalize(self):
        total = 0
        for i in range(self.posecells_elements):
            total += self.posecells_memory[i]
        assert total > 0

        for i in range(self.posecells_elements):
            self.posecells_memory[i] /= total

        return True
    
    
    def path_integration(self,vtrans,vrot):
        
        #pdb.set_trace()
        # this is a new branch
        angle_to_add=0
        vtrans/=self.PC_CELLS_X_SIZE
        
        
        if vtrans<0:
            vtrans=-vtrans
            angle_to_add=math.pi
        for dir_pc in range(0,self.PC_DIM_TH):
            dir=dir_pc*self.PC_C_SIZE_TH+angle_to_add
            self.rot90_square(self.posecells[dir_pc], self.PC_DIM_XY, 4-int(math.floor((dir*2.0)/math.pi)))
            dir90=dir-math.floor(dir*2/math.pi)*math.pi/2
            
            for j in range(self.PC_DIM_XY):
                self.pca_new_rot_ptr[j+1]=self.posecells[dir_pc][j][0]
            weight_sw=vtrans**2*math.cos(dir90)*sin(dir90)
            weight_se=vtrans*math.sin(dir90)*(1.0-vtrans*math.cos(dir90))
            weight_nw=vtrans*math.cos(dir90)*(1.0-vtrans*math.sin(dir90))
            weight_ne=1.0-weight_sw-weight_se-weight_nw


            self.pca_new[dir_pc][0][0]=self.pca_new[dir_pc][0][0]*weight_ne+self.pca_new[dir_pc][0][self.PC_DIM_XY-1]*weight_se+self.pca_new[dir_pc][self.PC_DIM_XY-1][0]*weight_nw
            #self.pca_new_rot_ptr2[0][0]=self.pca_new_rot_ptr[0][0]*weight_ne+self.pca_new_rot_ptr[0][self.PC_DIM_XY+1]*weight_se+self.pca_new_rot_ptr[self.PC_DIM_XY+1][0]*weight_nw
            
            for i in range(1,self.PC_DIM_XY+1):
                self.pca_new[dir_pc][0][i-1]=self.pca_new[dir_pc][0][i-1]*weight_ne+self.pca_new[dir_pc][0][i-2]*weight_se+self.pca_new[dir_pc][self.PC_DIM_XY-1][i-1]*weight_nw
            for j in range(1,self.PC_DIM_XY+1):
                self.pca_new[dir_pc][j-1][0]=self.pca_new[dir_pc][j-1][0]*weight_ne+self.pca_new[dir_pc][j-1][self.PC_DIM_XY-1]*weight_se+self.pca_new[dir_pc][j-2][0]*weight_nw
                for i in range(1,self.PC_DIM_XY+1):
                    self.pca_new[dir_pc][j-1][i-1]=self.pca_new[dir_pc][j-1][i-1]*weight_ne+self.pca_new[dir_pc][j-1][i-1]*weight_se+self.pca_new[dir_pc][j-2][i-1]*weight_nw
                    print self.pca_new[dir_pc][j-1][i-1]
            self.circshift2d(self.pca_new, self.posecells_plane_th, self.PC_DIM_XY+2, self.PC_DIM_XY+2, 1, 1)
            
            
            
            #pca_new = pca_new.*weight_ne + [pca_new(:,end) pca_new(:,1:end-1)].*weight_nw + [pca_new(end,:); pca_new(1:end-1,:)].*weight_se 
            #+ circshift(pca_new, [1 1]).*weight_sw;
    
    
            """
            self.pca_new = self.pca_new*weight_ne + \
                          np.roll(self.pca_new, 1, 1) * weight_nw + \
                          np.roll(self.pca_new, 1, 0) * weight_se + \
                          np.roll(np.roll(self.pca_new, 1, 1), 1, 0) * weight_sw        

            """
            for i in range((self.PC_DIM_XY+2)*(self.PC_DIM_XY+2)-1):
                self.pca_new_rot_ptr2[0][i]+=self.pca_new_rot_ptr[0][i]*weight_sw
             
            
                
            for j in range(self.PC_DIM_XY):
                for i in range(self.PC_DIM_XY):
                    self.posecells[dir_pc][j][i]=self.pca_new[dir_pc][j][i]
                    
                    
            for i in range(self.PC_DIM_XY-1):
                self.posecells[dir_pc][0][i]+=self.pca_new[dir_pc][self.PC_DIM_XY-1][i]
            for i in range(self.PC_DIM_XY-1):
                self.posecells[dir_pc][j][0]+=self.pca_new[dir_pc][j][self.PC_DIM_XY-1]
            
            
            self.posecells[dir_pc][0][0]+=self.pca_new[dir_pc][self.PC_DIM_XY-1][self.PC_DIM_XY-1]
            
            
            self.posecells[dir_pc,:,:]=rot90(self.posecells[dir_pc,:,:],4-int(math.floor(dir*2.0/math.pi)))
            
        if vrot !=0:
            weight=abs(vrot)/self.PC_C_SIZE_TH
            while(weight>1):
                weight-=1
            if (weight==0):
                weight=1.0
            k=0
            
        
            for i in range(self.PC_DIM_TH):
                for j in range(self.PC_DIM_XY):
                    for k in range(self.PC_DIM_XY):
                        self.posecells_memory[k]=self.posecells[i,j,k]    
                        k+=1
            self.pca_new_memory=self.posecells_memory
            
            if vrot<0:
                sign_vrot=-1
                
            else:
                sign_vrot=1
            shifty1=int(sign_vrot*math.floor(abs(vrot))/self.PC_C_SIZE_TH)
            shifty2=int(sign_vrot*math.ceil(abs(vrot)/self.PC_C_SIZE_TH))
            while(shifty1>0):
                shifty1-=self.PC_DIM_TH

            while(shifty2>0):
                shifty2-=self.PC_DIM_TH
            indice_of_pose_memory=0
            for j in range(self.PC_DIM_XY):
                for i in range(self.PC_DIM_XY):
                    for k in range(self.PC_DIM_TH):
                        newk1=(k-shifty1)%self.PC_DIM_TH
                        newk2=(k-shifty2)%self.PC_DIM_TH
                        
                        if newk1<self.PC_DIM_TH and newk2<self.PC_DIM_TH and newk1>=0 and newk2>=0:
                            self.posecells[k][j][i]=self.pca_new[newk1,j,i]*(1.0-weight)+self.pca_new[newk2,j,i]*weight
                            indice_of_pose_memory+=1
                 
    def find_best(self):
        #pdb.set_trace()
        x=-1
        y=-1
        th=-1
        max=0
        for k in range(self.PC_DIM_TH):
            for j in range(self.PC_DIM_XY):
                for i in range(self.PC_DIM_XY):
                    if self.posecells[k][j][i]>max:
                        max=self.posecells[k][j][i]
                        x=double(i)
                        y=double(j)
                        th=double(k)
        x_sums=self.posecells[:,0,0]
        y_sums=self.posecells[:,1,0]
        z_sums=self.posecells[:,2,0]
        for k in range(int(th),int(th+self.PC_CELLS_TO_AVG*2+1)):
            for j in range(int(y),int(y+self.PC_CELLS_TO_AVG*2+1)):
                for i in range(int(x),int(x+self.PC_CELLS_TO_AVG*2+1)):
                    
                    
                    z_sums[self.PC_AVG_TH_WRAP[k]]+=self.posecells[self.PC_AVG_TH_WRAP[k]][self.PC_AVG_XY_WRAP[j]][self.PC_AVG_XY_WRAP[i]]
                    y_sums[self.PC_AVG_XY_WRAP[j]]+=self.posecells[self.PC_AVG_TH_WRAP[k]][self.PC_AVG_XY_WRAP[j]][self.PC_AVG_XY_WRAP[i]]
                    x_sums[self.PC_AVG_XY_WRAP[i]]+=self.posecells[self.PC_AVG_TH_WRAP[k]][self.PC_AVG_XY_WRAP[j]][self.PC_AVG_XY_WRAP[i]]
        sum_x1=0
        sum_x2=0
        sum_y1=0
        sum_y2=0
        for i in range(self.PC_DIM_XY):
            sum_x1+=self.PC_XY_SUM_SIN_LOOKUP[i]*x_sums[i]
            sum_x2+=self.PC_XY_SUM_COS_LOOKUP[i]*x_sums[i]
            sum_y1+=self.PC_XY_SUM_SIN_LOOKUP[i]*y_sums[i]
            sum_y2+=self.PC_XY_SUM_COS_LOOKUP[i]*y_sums[i]
        x=math.atan2(sum_x1, sum_x2)*self.PC_DIM_XY/(2.0*math.pi)-1.0
        while (x<0):
            x+=self.PC_DIM_XY
            
        while (x>self.PC_DIM_XY):
            x-=self.PC_DIM_XY
            
        y=math.atan2(sum_y1,sum_y2)*(self.PC_DIM_XY)/(2.0*math.pi)-1.0
        while(y<0):
            y+=self.PC_DIM_XY
        while(y>self.PC_DIM_XY):
            y-=self.PC_DIM_XY
            
        sum_x1=0
        sum_x2=0
        for i in range(self.PC_DIM_TH):
            sum_x1+=self.PC_TH_SUM_SIN_LOOKUP[i]*z_sums[i]
            sum_x2+=self.PC_TH_SUM_COS_LOOKUP[i]*z_sums[i]
        th=math.atan2(sum_x1, sum_x2)*(self.PC_DIM_TH)/(2.0*math.pi)-1.0
        while(th<0):
            th+=self.PC_DIM_TH
        while th>self.PC_DIM_TH:
            th-=self.PC_DIM_TH
            
        if x<0 or y<0 or x>self.PC_DIM_XY or y>self.PC_DIM_XY or th>self.PC_DIM_TH:
            print "ERROR",x, ", ",y, " , ", th, " ,", "out of range", "\n"
        self.best_x=x
        self.best_y=y
        self.best_th=th
        print "gggggggggggggggggggg",x
        return max
        
        
    """           
    def find_best(self):
        xywrap = self.avg_xywrap
        thwrap = self.avg_thwrap
        self.shape = [self.PC_DIM_XY, self.PC_DIM_XY, self.PC_DIM_TH]
        (x, y, z) = unravel_index(self.posecells.argmax(), self.posecells.shape)
        z_posecells = zeros(self.shape) 
        
        zval = self.posecells[ix_(xywrap[x:x + 7], xywrap[y:y + 7], thwrap[z:z + 7])]
        
        z_posecells[ix_(self.avg_xywrap[x:x + self.cells_avg * 2 + 1],
                    self.avg_xywrap[y:y + self.cells_avg * 2 + 1],
                    self.avg_thwrap[z:z + self.cells_avg * 2 + 1])] = zval
        
        # get the sums for each axis
        x_sums = sum(sum(z_posecells, 2), 1) 
        y_sums = sum(sum(z_posecells, 2), 0)
        th_sums = sum(sum(z_posecells, 1), 0)
        th_sums = th_sums[:]
        
        # now find the (x, y, th) using population vector decoding to handle 
        # the wrap around 
        x = (arctan2(sum(self.xy_sum_sin * x_sums),
                     sum(self.xy_sum_cos * x_sums)) * \
            self.shape[0] / (2 * pi)) % (self.shape[0])
            
        y = (arctan2(sum(self.xy_sum_sin * y_sums),
                     sum(self.xy_sum_cos * y_sums)) * \
            self.shape[0] / (2 * pi)) % (self.shape[0])
            
        th = (arctan2(sum(self.th_sum_sin * th_sums),
                      sum(self.th_sum_cos * th_sums)) * \
             self.shape[2] / (2 * pi)) % (self.shape[2])

        self.best_x=x
        self.best_y=y
        self.best_th=th

    """ 
    
    def get_cells(self):
        return self.posecells_memory
    
    def set_cells(self, cells):
        self.posecells_memory = cells
        if self.posecells_memory is None:
            return True
        else:
            return False
    
    def get_delta_pc(self, x, y, th):
        pc_th_corrected = self.best_th - self.vt_delta_pc_th
        if pc_th_corrected < 0:
            pc_th_corrected = self.PC_DIM_TH + pc_th_corrected
        if pc_th_corrected >= self.PC_DIM_TH:
            pc_th_corrected = pc_th_corrected - self.PC_DIM_TH
        return math.sqrt(self.get_min_delta(self.best_x, x, self.PC_DIM_XY) ** 2 + self.get_min_delta(self.best_y, y, self.PC_DIM_XY) ** 2 + self.get_min_delta(pc_th_corrected, th, self.PC_DIM_TH) ** 2)
    
    def get_min_delta(self, d1, d2, max):
        absval = abs(d1 - d2)
        return min(absval, max - absval)
    
   
    
    def pose_cell_inhib_helper(x, y, z):
        inhib_index = 0
        for zl in range(z, z + self.PC_W_I_DIM):
            for yl in range(y, y + self.PC_W_I_DIM):
                for xl in range(x, x + self.PC_W_I_DIM):
                    xw = self.PC_I_XY_WRAP[xl]
                    yw = self.PC_I_XY_WRAP[yl]
                    zw = self.PC_I_TH_WRAP[zl]
    
                    self.pca_new[zw][yw][xw] += self.posecells[z][y][x] * self.PC_W_INHIB[inhib_index]
                    inhib_index += 1
    
        return True
    
    def rot90_square(self, array, dim, rot):
        centre = (double)(dim - 1) / 2.0
        if(rot < 0):
            rot += 4
        if (rot % 4 == 0):
            return 1
        elif (rot % 4 == 1):
            a = 0
            b = -1
            c = 1
            d = 0
            # break
        elif (rot % 4 == 2):
            a = -1
            b = 0
            c = 0
            d = -1
            # break
        elif (rot % 4 == 3):
            a = 0
            b = 1
            c = -1
            d = 0
            # break
        else: 
            return 1
    
        if rot % 2 == 1:
            for j in range((int)(centre) + (1 - dim % 2)):
                for i in range(int(centre) + 1):
                    id = i
                    jd = j
                    tmp_old = array[j][i]
                    for quad in range(4):
                        is1 = id
                        js1 = jd
                        id = (int)(a * ((float)(is1) - centre) + b * ((float)(js1) - centre) + centre)
                        jd = (int)(c * ((float)(is1) - centre) + d * ((float)(js1) - centre) + centre)
                        tmp_new = array[jd][id]
                        array[jd][id] = tmp_old
                        tmp_old=tmp_new
        else:
            self.rot90_square(array, dim, 1)
            self.rot90_square(array, dim, 1)
        
        return True
    
    
    
    def generate_wrap(self, wrap, start1, end1, start2, end2, start3, end3):
        i = 0
        for j in range(start1, end1):
            wrap[i] = j
            i += 1
        for j in range(start2, end2):
            wrap[i] = j
            i += 1
        for j in range(start3, end3):
            wrap[i] = j
            i += 1
        return wrap
    
    
    def norm2d(self, var, x, y, z, dim_centre):
        return 1.0 / (var * math.sqrt(2.0 * math.pi)) * math.exp((-x - dim_centre) * (x - dim_centre) - (y - dim_centre) * (y - dim_centre) - (z - dim_centre) * (z - dim_centre) / (2.0 * var * var))
    def normalise(self):
        total = 0.0
        for i in range(self.posecells_elements):
            total += self.posecells_memory[i]
            
        # assert total>0
        for i in range(self.posecells_elements):
            self.posecells_memory[i] /= total
        return True
    
    
    def on_odo(self, vtrans, vrot, time_diff_s):
        vtrans = vtrans * time_diff_s
        vrot = vrot * time_diff_s
        print time_diff_s
        self.excite();
        self.inhibit();
        self.global_inhibit();
        self.normalise();
        self.path_integration(vtrans, vrot);
        self.find_best();
        
        self.odo_update = True;
    
    def get_current_exp_id(self):
        return self.current_exp

    def x(self):
        return self.best_x
    def y(self):
        return self.best_y
    def th(self):
        return self.best_th

    def create_experience(self):
       # pcvt=self.visual_templates[self.current_vt]
        #self.experiences.resize(len(self.experiences)+1)
        self.current_exp=len(self.experiences)
        #exp=self.experiences[current_exp]
        exp=PosecellExperience()
        exp.x_pc=self.x()
        exp.y_pc=self.y()
        exp.th_pc=self.th()
        exp.vt_id=self.current_vt
        self.experiences.append(exp)
        self.visual_templates[self.current_vt-1].exps.append(self.current_exp)

    def get_action(self):
        #pdb.set_trace()
        experience=PosecellExperience()
        action=PosecellNetwork.PosecellAction.NO_ACTION
        
        if self.odo_update ==True and self.vt_update==True:

            self.odo_update=False
            self.vt_update=False
            
        else:

            return action
        if len(self.visual_templates)==0:
            action=self.PosecellAction.NO_ACTION
            
            return action
        if len(self.experiences)==0:
            self.create_experience()
            action =self.PosecellAction.CREATE_NODE
        else:

            experience=self.experiences[self.current_exp]
            
            delta_pc=self.get_delta_pc(experience.x_pc,experience.y_pc,experience.th_pc)
            pcvt=self.visual_templates[self.current_vt]
            if len(pcvt.exps)==0:

                self.create_experience()
                action=self.PosecellAction.CREATE_NODE
            elif delta_pc>self.EXP_DELTA_PC_THRESHOLD or self.current_vt!=self.prev_vt:

                matched_exp_id=-1
                min_delta_id=-1
                min_delta=self.DBL_MAX
                for i in range(len(pcvt.exps)):
                    if self.current_exp==pcvt.exps[i]:
                        continue
                    experience=self.experiences[pcvt.exps[i]]
                    delta_pc=self.get_delta_pc(experience.x_pc, experience.y_pc, experience.th_pc)
                    if delta_pc<min_delta:
                        min_delta=delta_pc
                        min_delta_id=pcvt.exps[i]
                if min_delta<self.EXP_DELTA_PC_THRESHOLD:
                    matched_exp_id=min_delta_id
                    action=self.PosecellAction.CREATE_EDGE
                if self.current_exp!= matched_exp_id:
                    if matched_exp_id==-1:
                        self.create_experience()
                        action=self.PosecellAction.CREATE_NODE
                    else:
                        self.current_exp=matched_exp_id
                        if action==self.PosecellAction.NO_ACTION:
                            action=self.PosecellAction.SET_NODE
            
                
                elif self.current_vt==self.prev_vt:
                    self.create_experience()
                    action=self.PosecellAction.CREATE_NODE
        return action
    
    
    
    def on_view_template(self,vt,vt_rad):
        pcvt=PosecellVisualTemplate
        if vt>=len(self.visual_templates):
            self.create_view_template()
            #assert vt == len(self.visual_templates-1)
        else:
            pcvt=self.visual_templates[vt]
            
            if vt<len(self.visual_templates)-10:
                if vt!=self.current_vt:
                    print "this is for tests"
                else:
                    pcvt.decay+=self.VT_ACTIVE_DECAY
                
                energy=self.PC_VT_INJECT_ENERGY*1.0/30.0*(30.0*math.exp(1.2*pcvt.decay))
                if energy>0:
                    self.vt_delta_pc_th=vt_rad/(2.0*math.pi)*self.PC_DIM_TH
                    pc_th_corrected=pcvt.pc_th+vt_rad/(2.0*math.pi)*self.PC_DIM_TH
                    if pc_th_corrected<0:
                        pc_th_corrected=self.PC_DIM_TH+pc_th_corrected
                    if pc_th_corrected>=self.PC_DIM_TH:
                        pc_th_corrected=pc_th_corrected-self.PC_DIM_TH
                    self.inject(int(pcvt.pc_x), int(pcvt.pc_y),int(pc_th_corrected), energy)
        for i in range(len(self.visual_templates)):
            self.visual_templates[i].decay-=self.PC_VT_RESTORE
            if self.visual_templates[i].decay<self.VT_ACTIVE_DECAY:
                self.visual_templates[i].decay=self.VT_ACTIVE_DECAY
        self.prev_vt=self.current_vt
        self.current_vt=vt
        self.vt_update=True
        
    def get_relative_rad(self):
        return self.vt_delta_pc_th*2.0*math.pi/self.PC_DIM_TH
    
    def create_view_template(self):
        pcvt=PosecellVisualTemplate()
        #pcvt=self.visual_templates[len(self.visual_templates)-1]
        pcvt.pc_x=self.x()
        pcvt.pc_y=self.y()
        
        pcvt.pc_th=self.th()
        
        pcvt.decay=self.VT_ACTIVE_DECAY
        self.visual_templates.append(pcvt)
        
        
        
    def circshift2d(self,array,array_buffer,dimx,dimy,shiftx,shifty):
        #pdb.set_trace()
        if shifty==0:
            if shiftx==0:
                return
            array_buffer=array
        elif shifty>0:
            array_buffer=array[(dimy-shifty)*dimx][:]
            array_buffer[shifty*dimx]=array
        else:
            array_buffer=array[-shifty*dimx]
            array_buffer[(dimy+shifty)*dimx]
        if shiftx==0:
            array=array_buffer
        elif shiftx>0:
            for i in range(dimy):
                array[i*dimx]=array_buffer[i*dimx+dimx-shiftx]
                array[i*dimx+shiftx]=array_buffer[i*dimx]
        else:
            for i in range(dimy):
                array[i*dimx]=array_buffer[i*dimx-shiftx]
                array[i*dimx+dimx+shiftx]=array_buffer[i*dimx]