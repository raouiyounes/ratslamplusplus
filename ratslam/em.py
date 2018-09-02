import math
from cmath import atan


# une experience
class Experience:
    def __init__(self):
        self.id=0
        self.pc_id=0
        self.x_m=0
        self.y_m=0
        self.th_rad=0
        self.vt_id=0
        self.links_from=[]
        self.links_to=[]

# un lien
class Link:
    def __init__(self):
        self.d=0.0
        self.heading_rad=0
        self.exp_to_id=0
        self.exp_from_id=0
        self.delta_time_s=0

experiences=[]
# la carte d'experience

class ExperienceMap:
    def __init__(self):
        self.accum_delta_x=0
        self.accum_delta_y=0
        self.current_exp_id=0
        self.links=[]
    def create_experience(self,exp_id,vt_id):
        exp=Experience()
        exp.pc_id=exp_id
        exp.x_m=self.experiences[self.current_exp_id]+self.accum_delta_x
        exp.y_m=self.experiences[self.current_exp_id]+self.accum_delta_y
        #exp.th_rad=self.experiences[self.current_exp_id]+self.accum_delta_facing
        exp.vt_id=vt_id
        self.experiences.append(exp)
    def create_link(self,exp_from,exp_to):
        dij=math.sqrt(self.accum_delta_x**2+self.accum_delta_y**2)
        th_ij=atan(self.accum_delta_y/self.accum_delta_x)
        l=Link()
        l.d=dij
        l.heading_rad=th_ij
        l.exp_from_id=exp_from
        l.exp_to_id=exp_to
        self.links.append(l)
        self.accum_delta_x=0
        self.accum_delta_y=0
    
    
    def set_experience(self,new_exp_id):
	#TO DO    
    
    def on_odo(self,vtrans,vrot,time_diff_s):
        
        vtrans=vtrans*time_diff_s
        vrot*=time_diff_s
        self.accum_delta_facing=self.clip_rad_180(self.accum_delta_facing+vrot)
        self.accum_delta_x=self.accum_delta_x+vtrans*math.cos(self.accum_delta_facing)
        self.accum_delta_y=+vtrans*math.sin(self.accum_delta_facing)
        self.accum_delta_time_s+=time_diff_s
 
        
        si=similarity(experiences,[Pi,Vi])
        if si>smax:
            create_experience(Pi,Vi)
            create_link()

    
