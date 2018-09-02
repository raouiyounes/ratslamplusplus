import sys
import numpy as np
import math
import pdb
from PIL.ImageChops import offset
class VisualTemplate:
    #instance=[]
    def __init__(self):
        self.id=0
        self.data=np.array([])
        self.mean=0
        #self.instance.append(self)
    
class LocalViewMatch:
    def __init__(self):
        self. VT_MIN_PATCH_NORMAISATION_STD=0.0
        self.VT_PATCH_NORMAISATION=0.0
        self.VT_NORMALISATION=0.0
        self.VT_SHIFT_MATCH=4.0
        self.VT_PANORAMIC=False
        self.VT_MATCH_THRESHOLD=0.03
        self.TEMPLATE_X_SIZE=60
        self.TEMPLATE_Y_SIZE=20
        self.IMAGE_VT_X_RANGE_MIN=0
        self.IMAGE_VT_X_RANGE_MAX=-1
        self.IMAGE_VT_Y_RANGE_MIN=0
        self.IMAGE_VT_Y_RANGE_MAX=150
        self.TEMPLATE_SIZE=self.TEMPLATE_X_SIZE*self.TEMPLATE_Y_SIZE
        self.current_mean=0
        #self.templates=np.array([])
        #self.templates.resize(10000)
                
        #for i in range(10000):
         #   self.templates[i]=x
        #self.templates.resize(10000)
        self.current_view=np.zeros(self.TEMPLATE_SIZE)
        self.current_view.resize(self.TEMPLATE_SIZE)
        self.xxx=0
        self.cdiff=2

        self.current_vt=0
        self.prev_vt=0
        self.DBL_MAX=sys.float_info.max
        self.VT_STEP_MATCH=1
        #self.view_rgb=""
        self.vt_match_id=0
        self.grayscale=False
        self.prev_vt=0
        self.min_offset=0

        self.vt_relative_rad=0
        
        self.vt_error=0
        self.VT_NORMALISATION=0.0
        self.VT_MIN_PATCH_NORMALISATION_STD=0.0
        
        
        self.templates=[]*10000
        xxx=VisualTemplate()
        xxx.id=0
        xxx.data=[]
        xxx.mean=0.0
        self.templates.append(xxx)
        self.data=np.array([])
        self.VT_SHIFT_MATCH=4
        self.vt_match_id=0
    def on_image(self,view_rgb,greyscale,image_width,image_height):
        
        if view_rgb==[]:
            return
            
        self.IMAGE_WIDTH=image_width
        self.IMAGE_HEIGHT=image_height
        
        if self.IMAGE_VT_X_RANGE_MAX==-1:
            self.IMAGE_VT_X_RANGE_MAX=self.IMAGE_WIDTH
        if self.IMAGE_VT_Y_RANGE_MAX==-1:
            self.IMAGE_VT_Y_RANGE_MAX=self.IMAGE_HEIGHT
            
        self.view_rgb=view_rgb
        self.grayscale=greyscale
        
        self.convert_view_to_view_template(greyscale)  
        self.prev_vt=self.get_current_vt()
        self.compare()
        if self.vt_error<=self.VT_MATCH_THRESHOLD:
            self.set_current_vt(int(self.vt_match_id))
            print "VTM[", self.get_current_vt(),"]","\n"
            
            sys.stdout.flush()  
        else:
            self.vt_relative_rad=0
            self.set_current_vt(self.create_template())
            print "VTN[",self.get_current_vt(),"]","\n"
            sys.stdout.flush()
        
    def LocalViewMatch(self,x,y):
        self.vt_relative_rad=0
        if x<0:
            x=0
        elif x>self.TEMPLATE_X_SIZE-1:
            x=self.TEMPLATE_X_SIZE-1
        if y<0:
            y=0
        elif y>self.TEMPLATE_Y_SIZE-1:
            y=self.TEMPLATE_Y_SIZE-1
    
    
    def convert_view_to_view_template(self,grayscale):
        data_next=0
        sub_range_x=self.IMAGE_VT_X_RANGE_MAX-self.IMAGE_VT_X_RANGE_MIN
        sub_range_y=self.IMAGE_VT_Y_RANGE_MAX-self.IMAGE_VT_Y_RANGE_MIN
        
        x_block_size=sub_range_x/self.TEMPLATE_X_SIZE
        y_block_size=sub_range_y/self.TEMPLATE_Y_SIZE
        
        for i in range(len(self.current_view)):
            self.current_view[i]=0
        if self.grayscale==True:
            y_block=self.IMAGE_VT_Y_RANGE_MIN
            for y_block_cout in range(self.TEMPLATE_Y_SIZE):
                x_block=self.IMAGE_VT_X_RANGE_MIN
                for x_block_count in range(self.TEMPLATE_X_SIZE):

                    for x in range(x_block,x_block+x_block_size):
                        for y in range(y_block,y_block+y_block_size):
                            pos=x+y*self.IMAGE_WIDTH
                            self.current_view[data_next]+=float(self.view_rgb[pos])
                    self.current_view[data_next]/=255.0
                    self.current_view[data_next]/=x_block_size*y_block_size
                    data_next+=1
                    x_block+=x_block_size
                y_block+=y_block_size
        else:
            y_block=self.IMAGE_VT_Y_RANGE_MIN
            for y_block_count in range(self.TEMPLATE_Y_SIZE):
                x_block=self.IMAGE_VT_X_RANGE_MIN
                for x_block_count in range(self.TEMPLATE_X_SIZE):
                    for x in range(x_block,x_block+x_block_size):
                        for y in range(y_block,y_block+y_block_size):
                            pos=(x+y*self.IMAGE_WIDTH)*3
                            self.current_view[data_next]+=float(self.view_rgb[pos])+float(self.view_rgb[pos+1])+float(self.view_rgb[pos+2])
                    self.current_view[data_next]/=255.0*3.0
                    self.current_view[data_next]/=x_block_size*y_block_size
                    data_next+=1
                    x_block+=x_block_size
                y_block+=y_block_size
        if self.VT_NORMALISATION>0:
            avg_value=0
            for i in range(len(self.current_view)):
                avg_value+=self.current_view[i]
            avg_value/=len(self.current_view)
            for i in len(self.current_view):
                self.current_view[i]=max(0.0,min(self.current_view[i]*self.VT_NORMALISATION/avg_value,1))
        
        '''
    
  // now do patch normalisation
  // +- patch size on the pixel, ie 4 will give a 9x9
''' 
        if self.VT_PATCH_NORMAISATION>0:
            patch_size=self.VT_PATCH_NORMAISATION
            patch_total=(patch_size*2+1)*(patch_size*2+1)
   #    // first make a copy of the view
         
            current_view_copy=np.array([])
            current_view_copy.resize(len(self.current_view))
            for i in range(len(self.current_view)):
                current_view_copy[i]=self.current_view[i]

    #    // this code could be significantly optimimised ....

            for x in range(self.TEMPLATE_X_SIZE):
                for y in range(self.TEMPLATE_Y_SIZE):
                    patch_sum=0
                    for patch_x in range(x-patch_size,x+patch_size):
                        for patch_y in range(y-patch_size,y+patch_size+1):
                            patch_x_clip=patch_x
                            patch_y_clip=patch_y
                            self.clip_view_x_y(patch_x_clip,patch_y_clip)
                            patch_sum+=((current_view_copy[patch_x_clip+patch_y_clip*self.TEMPLATE_X_SIZE]-patch_mean)*\
                                (current_view_copy[patch_x_clip+patch_y_copy*self.TEMPLATE_X_SIZE]-patch_mean))
                           
                    patch_std=math.sqrt(patch_sum/patch_total)
                    if patch_std<self.VT_MIN_PATCH_NORMALISATION_STD:
                        self.current_view[x+y*self.TEMPLATE_X_SIZE]=0.5
                    else:
                        self.current_view[x+y*self.TEMPLATE_X_SIZE]=max(0.0,min(1.0,(((self.current_view_copy[x+y*self.TEMPLATE_X_SIZE]-patch_mean)/patch_std)+3.0)/6.0))
                
                
        sum=0
#  // find the mean of the data

        
        for i in range(len(self.current_view)):
            sum+=self.current_view[i]
        self.current_mean=sum/len(self.current_view)

#// create and add a visual template to the collection

        
    def create_template(self):
        
        
        vtt=VisualTemplate()
        vtt.id=len(self.templates)-1
        vtt.data=self.current_view
        vtt.mean=self.current_mean
        #vtt.id=len(self.templates)
        self.templates.append(vtt)
        '''
        self.templates.append(VisualTemplate())
        data_ptr=self.current_view
        
        self.templates[len(self.templates)-1].data=np.array(self.TEMPLATE_SIZE)
        self.templates[len(self.templates)-1].data=data_ptr
        self.templates[len(self.templates)-1].mean=self.current_mean
        '''
        return len(self.templates)-1
    #def compare(self,vt_err,vt_match_id):
    

    """
    // compare a visual template to all the stored templates, allowing for 
// slen pixel shifts in each direction
// returns the matching template and the MSE
"""
    def compare(self):
        #pdb.set_trace()
        if(len(self.templates)==0):
            vt_err=self.DBL_MAX
            self.vt_error=vt_err
            return
        self.data=self.current_view
        mindiff=self.DBL_MAX
        vt_err=self.DBL_MAX
        min_template=0
        vt=VisualTemplate()
        epsilon=0.005
        if (self.VT_PANORAMIC==False):
            indice=0

            for i in range(len(self.templates)):
                indice+=1
                vt=self.templates[i]
                if (abs(self.current_mean-vt.mean)>self.VT_MATCH_THRESHOLD+epsilon):
                    continue
                
                offset=1
                while offset<self.TEMPLATE_X_SIZE:
                    self.cdiff=0
                    template_start_ptr=vt.data[0]+offset
                    column_start_ptr=self.data[0]
                    row_size=self.TEMPLATE_X_SIZE
                    
                    sub_ros_size=self.TEMPLATE_X_SIZE-offset
                    template_row_ptr=offset
                    for column_row_ptr in range(0,self.TEMPLATE_SIZE - offset,self.TEMPLATE_X_SIZE):
                        template_ptr=template_row_ptr
                        for column_ptr in range(column_row_ptr,column_row_ptr+sub_ros_size):
                            self.cdiff+=abs(vt.data[template_ptr]-self.data[column_ptr])
                            template_ptr+=1
                        template_row_ptr+=row_size
                        #fast break
                        if self.cdiff>mindiff:
                            break
                    template_start_ptr=0
                    column_start_ptr=self.TEMPLATE_SIZE-offset
                    row_size=self.TEMPLATE_X_SIZE
                    column_end_ptr=self.TEMPLATE_SIZE
                    sub_row_size=offset
                    
                    template_row_ptr=template_start_ptr
                    column_row_ptr=column_start_ptr
                    while column_row_ptr<column_end_ptr:
                        column_ptr=column_row_ptr
                        template_ptr=template_row_ptr
                        while column_ptr<column_row_ptr+sub_row_size:
                            self.cdiff+=abs(self.data[column_ptr]-vt.data[template_ptr])
                            print self.cdiff
                            template_ptr+=1
                            column_ptr+=1
                       
                        if self.cdiff>mindiff:
                            break
                        column_row_ptr+=row_size
                        template_row_ptr+=row_size

                    
                    if self.cdiff<mindiff:
                        print indice
                        mindiff=self.cdiff
                        min_template=vt.id
                        self.min_offset=offset
                    offset+=self.VT_STEP_MATCH    
            self.vt_relative_rad=float(self.min_offset)/float(self.TEMPLATE_X_SIZE*2.0*np.pi)
            if self.vt_relative_rad>np.pi:
                self.vt_relative_rad=self.vt_relative_rad-2.0*np.pi
            vt_err=mindiff/float(self.TEMPLATE_SIZE)
            self.vt_match_id=min_template
            self.vt_error=vt_err
        else:
            
            for i in range(len(self.templates)-1):
                vt=self.templates[i]
                
                if (abs(self.current_mean-vt.mean)>self.VT_MATCH_THRESHOLD+epsilon):
                    continue
                offset=0
                while offset<self.VT_SHIFT_MATCH*2+1:
                    self.cdiff=0
                    template_start_ptr=offset
                    column_start_ptr=self.VT_SHIFT_MATCH
                    row_size=self.TEMPLATE_X_SIZE
                    column_end_ptr=self.TEMPLATE_SIZE-self.VT_SHIFT_MATCH
                    sub_row_size=self.TEMPLATE_X_SIZE-2*self.VT_SHIFT_MATCH
                    
                    column_row_ptr=column_start_ptr
                    template_row_ptr=template_start_ptr

                    while column_row_ptr<column_end_ptr:
                        template_ptr=template_row_ptr
                        for column_ptr in range(column_row_ptr,column_row_ptr+sub_row_size):
                            self.cdiff+=abs(self.data[column_ptr]-vt.data[template_ptr])
                            template_ptr+=1
                        column_row_ptr+=row_size
                        template_row_ptr+=row_size
                        if self.cdiff>mindiff:
                            break
                    if self.cdiff<mindiff:
                        mindiff=self.cdiff
                        min_template=vt.id
                        self.min_offset=0
                    offset+=self.VT_STEP_MATCH
            
            self.vt_relative_rad=0
    
            vt_err=mindiff/float(self.TEMPLATE_SIZE-2*self.VT_SHIFT_MATCH*self.TEMPLATE_Y_SIZE)
            self.vt_match_id=min_template
            self.vt_error=vt_err
        
        
    def clip_view_x_y(self,x,y):
        if x<0:
            x=0
        elif x>self.TEMPLATE_X_SIZE-1:
            x=self.TEMPLATE_X_SIZE-1
        if y<0:
            y=0
        elif y>self.TEMPLATE_Y_SIZE-1:
            y=self.TEMPLATE_Y_SIZE-1
            
    def get_current_vt(self):
        return self.current_vt
    def get_relative_rad(self):
        return self.vt_relative_rad
    
    def set_current_vt(self,id):
        if self.current_vt!=id:
            self.prev_vt=self.current_view
        self.current_vt=id
