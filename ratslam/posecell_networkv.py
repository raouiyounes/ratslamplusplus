import numpy as np
import math
import itertools
import numpy
from enum import Enum
from pylab import *

class PosecellExperience: 
    def __init__(self):
        self.x_pc = 0.0
        self.y_pc = 0.0
        self.th_pc = 0.0
        self.vt_id = 0
class PosecellVisualTemplate:
    def __init__(self):
        self.pc_y = 0.0
        self.pc_th = 0.0
        self.decay = 0.0
        self.exps = [];


class PosecellNetwork:
    '''
    class PosecellAction(Enum):
        NO_ACTION=0
        CREATE_NODE=1
        CREATE_EDGE=2
        SET_NODE=3
    '''
    PosecellAction=Enum('PosecellAction','NO_ACTION,CREATE_NODE,CREATE_EDGE,SET_NODE',start=0)

    #visual_templates=[]
    experiences=[]
        
    def __init__(self):
        self.visual_templates=[]	
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
        self.PC_AVG_XY_WRAP = range(self.PC_DIM_XY + 2 * self.PC_CELLS_TO_AVG)  # + range(self.PC_DIM_XY) + range(self.PC_CELLS_TO_AVG)
        self.PC_AVG_TH_WRAP = range(self.PC_DIM_TH + 2 * self.PC_CELLS_TO_AVG)  # , self.PC_DIM_TH) + range(self.PC_DIM_TH) + range(self.PC_CELLS_TO_AVG)
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
        posecells_memory = numpy.zeros(self.posecells_memory_size)
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
        self.pca_new = zeros([self.PC_DIM_XY, self.PC_DIM_XY, self.PC_DIM_TH])
        self.pca_new_rot_ptr2 = np.zeros(self.PC_DIM_XY + 2)
        
        self.posecells = np.zeros([self.PC_DIM_XY, self.PC_DIM_XY, self.PC_DIM_TH])

        self.current_vt=0
        xxx=PosecellVisualTemplate()
        self.visual_templates.append(xxx)
        self.PC_VT_RESTORE=0.05
         #  // the starting position within the posecell network

        self.best_x = floor(self.PC_DIM_XY / 2.0);
        self.best_y = floor(self.PC_DIM_XY / 2.0);
        self.best_th = floor(self.PC_DIM_TH / 2.0);
        self.posecells[int(self.best_x)][int(self.best_y)][int(self.best_th)] = 1;
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
                    if self.posecells[i][j][k] != 0:
                        #// spread the pose cell energy

                        self.pose_cell_excite_helper(i, j, k)
#  //  pc.Posecells = pca_new;

        self.posecells_memory = self.pca_new_memory
        

    def inhibit(self):
        self.pca_new_memory = bytearray(self.posecells_memory_size)
        #  // set pca_new to 0

        for i in range(self.PC_DIM_XY):
            for j in range(self.PC_DIM_XY):
                for k in range(self.PC_DIM_TH):
                    if self.posecells[i][j][k] != 0 :
#          // if there is energy in the current posecell,
#          // spread the energy

                        self.pose_cell_inhibit_helper(i, j, k)

        for i in range(self.posecells_elements):
            self.posecells_memory[i] -= self.pca_new_memory[i]
    
    
    def global_inhibit(self):
        for i in range(self.PC_DIM_XY):
            for j in range(self.PC_DIM_XY):
                for k in range(self.PC_DIM_XY):
                    if self.posecells[i][j][k]>=self.PC_GLOBAL_INHIB:
                        self.posecells[i][j][k]-=self.PC_GLOBAL_INHIB
                    else:
                        self.posecells[i][j][k]=0
                        
        """
        for i in range(self.posecells_elements):
    
            if self.posecells_memory[i] >= self.PC_GLOBAL_INHIB:
        
                
                self.posecells_memory[i] = (self.posecells_memory[i] - self.PC_GLOBAL_INHIB)
            else:
                self.posecells_memory[i] = 0
        """
        
        
    def pose_cell_excite_helper(self, x, y, z):
        excite_index = 0
        for zl in range(z, z + self.PC_W_I_DIM):
            for yl in range(y, y + self.PC_W_I_DIM):
                for xl in range(x, self.PC_W_I_DIM):
                    xw = self.PC_E_XY_WRAP[xl]
                    yw = self.PC_E_XY_WRAP[yl]
                    zw = self.PC_E_TH_WRAP[zl]
                    self.pca_new[xw][yw][zw] += self.posecells[x][y][z] * self.PC_W_EXCITE[excite_index]
                    excite_index = +1
        return True
    
    def pose_cell_inhibit_helper(self, x, y, z):
        inhib_index = 0

        for zl in range(z, z + self.PC_W_I_DIM):
            for yl in range(y, y + self.PC_W_I_DIM):
                for xl in range(x, self.PC_W_I_DIM):
                    xw = self.PC_I_XY_WRAP[xl]
                    yw = self.PC_I_XY_WRAP[yl]
                    zw = self.PC_I_TH_WRAP[zl]
                    self.pca_new[xw][yw][zw] += self.posecells[x][y][z] * self.PC_W_INHIB[inhib_index]
                    inhib_index += 1
        return True
                

    def normalize(self):
        total = 0
        for i in range(self.PC_DIM_XY):
            for j in range(self.PC_DIM_XY):
                for k in range(self.PC_DIM_TH):
                    total+=self.posecells[i][j][k]
        
        self.posecells/=total
        """
        for i in range(self.posecells_elements):
            total += posecells_memory[i]
        assert total > 0

        for i in range(self.posecells_elements):
            self.posecells_memory[i] /= total
        """
        return True
    
    
    
    def  path_integration(self, vtrans, vrot):
        for dir_pc in xrange(0, self.PC_DIM_TH): 
            direction = float(dir_pc - 1) * self.c_size_th 
            # N,E,S,W are straightforward
          

            if (direction == 0):
                self.posecells[:, :, dir_pc] = \
                    self.posecells[:, :, dir_pc] * (1.0 - vtrans) + \
                    roll(self.posecells[:, :, dir_pc], 1, 1) * vtrans

            elif direction == math.pi / 2:
                self.posecells[:, :, dir_pc] = \
                    self.posecells[:, :, dir_pc] * (1.0 - vtrans) + \
                    roll(self.posecells[:, :, dir_pc], 1, 0) * vtrans
                        
            elif direction == math.pi:
                self.posecells[:, :, dir_pc] = \
                    self.posecells[:, :, dir_pc] * (1.0 - vtrans) + \
                    roll(self.posecells[:, :, dir_pc], -1, 1) * vtrans

           
            elif direction == 3 * math.pi / 2:
                self.posecells[:, :, dir_pc] = \
                    self.posecells[:, :, dir_pc] * (1.0 - vtrans) + \
                    roll(self.posecells[:, :, dir_pc], -1, 0) * vtrans
            

            else:
                pca90 = numpy.rot90(self.posecells[:, :, dir_pc],
                              math.floor(direction * 2 / math.pi))
                dir90 = direction - math.floor(direction * 2 / math.pi) * math.pi / 2
                pca_new = zeros([self.PC_DIM_XY + 2, self.PC_DIM_XY + 2])   
                
                
                pca_new[1:-1, 1:-1] = pca90 
                
                weight_sw = (vtrans ** 2) * math.cos(dir90) * math.sin(dir90)
                weight_se = vtrans * sin(dir90) - \
                            (vtrans ** 2) * math.cos(dir90) * math.sin(dir90)
                weight_nw = vtrans * math.cos(dir90) - \
                            (vtrans ** 2) * math.cos(dir90) * math.sin(dir90)
                weight_ne = 1.0 - weight_sw - weight_se - weight_nw
          
                pca_new = pca_new * weight_ne + \
                          roll(pca_new, 1, 1) * weight_nw + \
                          roll(pca_new, 1, 0) * weight_se + \
                          roll(roll(pca_new, 1, 1), 1, 0) * weight_sw

                pca90 = pca_new[1:-1, 1:-1]
                pca90[1:, 0] = pca90[1:, 0] + pca_new[2:-1, -1]
                pca90[1, 1:] = pca90[1, 1:] + pca_new[-1, 2:-1]
                pca90[0, 0] = pca90[0, 0] + pca_new[-1, -1]

                # unrotate the pose cell xy layer
                self.posecells[:, :, dir_pc] = rot90(pca90,
                                                   4 - floor(direction * 2 / pi))
        # path integration for rot
        if vrot != 0: 
            weight = (abs(vrot) / self.c_size_th) % 1
            if weight == 0:
                weight = 1.0
            shift1 = int(sign(vrot) * floor(abs(vrot) / self.c_size_th))
            shift2 = int(sign(vrot) * ceil(abs(vrot) / self.c_size_th))
            self.posecells = roll(self.posecells, shift1, 2) * (1.0 - weight) + roll(self.posecells, shift2, 2) * (weight)
            
              

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

        
    
    def get_cells(self):
        return self.posecells_memory
    
    def set_cells(self, cells):
        self.posecells_memory = cells
        if self.posecells_memory is None:
            return True
        else:
            return False
    # ompute the distance between the actual experience and the existing ones
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
    
    def circshift2d(self, array, array_buffer, dimx, dimy, shiftx, shifty):
        if shifty == 0:
            if shiftx == 0:
                return
                array_buffer = array
    #    elif shifty > 0 :
     #       array = 
    
    
    def ros90_square(self, array, dim, rot):
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
    
        if rot % 1 == 1:
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
    
    
        else:
            ros90_square(array, dim, 1)
            rot90_square(array, dim, 1)
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
    # determine the actions to construct the graph of the map
    def get_action(self):
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
            if len(pcvt.exps)==1:
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
    
    # when a visual scene is viewed the hebiian learning is applied to update beta
    
    def on_view_template(self,vt,vt_rad):
        print "jkkkkkkkkkk"
        pcvt=PosecellVisualTemplate()
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

"""
class PoseCell2(PosecellNetwork):
    def __init__(self):
        PosecellNetwork.__init__(self)
    def create_view_template(self):
""" 
    
    