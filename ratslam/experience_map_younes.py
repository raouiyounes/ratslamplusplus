import rospy
import random
import sys
import Queue as Q
from collections import  deque
from _heapq import heapify, heappop
import math
import numpy as np
import pdb
from Utils.files import *
#pdb.set_trace()

experience_trace=open("em_trace.txt","w")

class Position:
    def __init__(self,x,y,th):
        self.x=x
        self.y=y
        self.theta=th


class snappingThreshold:
    def __init__(self):
        self.count=0
        self.derivation=Position(0.0,0.0,0.0)

class Link:
    d=0.0
    heading_rad=0.0
    exp_to_id=0
    exp_from_id=0
    delta_time_s=0.0
        


class Pair:
    def __init__(self,x,y):
        self.x=x
        self.y=y

class Experience:
    def __init__(self):
        self.id=0
        self.pc_id=0
        self.x_m=0
        self.y_m=0
        self.th_rad=0
        self.vt_id=0
        self.links_from=[]              #links from this experience
        self.links_to=[]                #links to this experience
        #gloal for navigation
        self.time_from_current_s=0
        self.goal_to_current=0
        self.current_to_goal=0
        self.diffFromMean=Position(0,0,0)
        self.vObjects=[]
        self.objects_id=[]
        
        
        
class ExperienceMap:
    def __init__(self):
        self.MAX_GOALS=10
        self.current_exp_id=0
        self.waypoint_exp_id=0
        self.goal_timeout_s=0
        self.goal_success=False
        self.EXP_INITIAL_EM_DEG=90.0
        self.accum_delta_facing=self.EXP_INITIAL_EM_DEG*math.pi/180
        self.accum_delta_x=0.0
        self.accum_delta_y=0.0
        self.accum_delta_time_s=0.0
        self.ID=id
        self._EVAL=eval
        self.snapp_counter=0
        # for loop closure
        self.EXP_LOOPS=20
        self.snapThresh=snappingThreshold()
        self.DBL_MAX=sys.float_info.max
        self.exp_creation_Timestamp=0
        self.exp_active_Timestamp=0
        self.links=[]
        self.EXP_CORRECTION=0.5
        self.goal_list=deque([])
        self.goal_path_final_exp_id=0
        self.goal_timeout_s=0
        self.goal_path_final_exp_id=0  #  ??
        self.MAX_GOALS=10
        exp_init=Experience()
        self.experiences=[]
        self.experiences.append(exp_init)
        self.vObjects=[]
    '''
 * create a new experience for a given position
 * @param exp_id    PoseCell ID for new experience
 * @return            experience map ID of created new experience
'''

    
    
    def on_create_experience2(self,exp_id):
#  //ROS_DEBUG_STREAM ("int ExperienceMap::on_create_experience(unsigned int exp_id) : " << exp_id);

        if(self._EVAL==True):  #for data evaluation
     
            if(self.exp_creation_Timestamp==0):
                self.exp_creation_Timestamp=rospy.Time.now().to_sec()
            
            time=rospy.Time.now().to_sec()-self.exp_creation_Timestamp
            path=path_created_EXPs
            if(self.ID>=0):
                s=str(self.ID)
                
            if(len(self.experiences)==0):
                vec=[]
                p=Pair(0,0)
                vec.append(p)
                writeToFile(s,vec)
            else :
                p=Pair(self.experiences,time)
                vec=[]
                vec.append(p)
                writeToFile(s,vec)
        #self.experiences.resize(len(self.experiences)+1)
        exp_i=Experience()

        if len(self.experiences)==0:
            
            exp_i.x_m=0
            exp_i.y_m=0
            exp_i.th_rad=0
        else:
            exp_i.x_m=self.experiences[self.current_exp_id].x_m+self.accum_delta_x
            exp_i.y_m=self.experiences[self.current_exp_id].y_m+self.accum_delta_y
            exp_i.th_rad=self.experiences[self.current_exp_id].th_rad=self.clip_rad_180(self.accum_delta_facing)

#link PoseCell_ID to the new EM_experience
            
        exp_i.pc_id=exp_id
        exp_i.id=len(self.experiences)-1
        exp_i.goal_to_current=-1
        exp_i.current_to_goal=-1
        #exp_i.vObjects=self.get_objects()
        # add the visual objects
        #exp_i.vObjects=self.getObjects()
        self.experiences.append(exp_i)
        if len(self.experiences)!=1:
            self.on_create_link2(self.get_current_id(),len(self.experiences)-1,0)    
        return len(self.experiences)-1
    
    '''
    /**
 * create a new experience for a given position (x,y,theta)
 * @param exp_id    PoseCell ID for new experience
 * @param x            x coordinate value of experience
 * @param y            y coordinate value of experience
 * @param theta        orientation of experience
 * @return            experience map ID of created new experience
 */'''
    




    def on_create_experienceWithObjects(self,exp_id):
#  //ROS_DEBUG_STREAM ("int ExperienceMap::on_create_experience(unsigned int exp_id) : " << exp_id);
        exp_i=Experience()

        if len(self.experiences)==0:
            
            exp_i.x_m=0
            exp_i.y_m=0
            exp_i.th_rad=0
        else:
            exp_i.x_m=self.experiences[self.current_exp_id].x_m+self.accum_delta_x
            exp_i.y_m=self.experiences[self.current_exp_id].y_m+self.accum_delta_y
            exp_i.th_rad=self.experiences[self.current_exp_id].th_rad=self.clip_rad_180(self.accum_delta_facing)

#link PoseCell_ID to the new EM_experience
            
        exp_i.pc_id=exp_id
        exp_i.id=len(self.experiences)-1
        exp_i.goal_to_current=-1
        exp_i.current_to_goal=-1
        exp_i.vObjects=self.get_objects()
# get the id of the objects at the time the expeience is created
        exp_i.objects_id=self.get_objects_id(time)
        
        # add the visual objects

        
        exp_i.vObjects=self.getObjects()
        self.experiences.append(exp_i)
        if len(self.experiences)!=1:
            self.on_create_link2(self.get_current_id(),len(self.experiences)-1,0)    
        return len(self.experiences)-1

        
        
        
        
        
    
    def on_create_experience(self,exp_id,x,y,theta):
        if(self._EVAL==True):
            if self.exp_creation_Timestamp==0:
                self.exp_creation_Timestamp=rospy.Time.now().to_sec()
            time=rospy.Time.now().to_sec()-self.exp_creation_Timestamp
            path=path_created_EXPs    # ???
            if(self.ID>=0):
                path+=str(self.ID)
            if(len(self.experiences)==0):
                p=Pair(0,0)
                vec=[]
                vec.append(p)
                writeToFile(path,vec)
            else: 
                p=Pair(len(self.experiences),time)
                vec=[]
                vec.append(p)
                writeToFile(path,vec)
        self.experiences.resize(len(self.experiences)+1)
        new_exp=self.experiences(len(self.experiences)-1)  #???
        new_exp.x_m=x
        new_exp.y_m=y
        new_exp.th_rad=theta
        new_exp.pc_id=exp_id
        new_exp.id=len(self.experiences)-1
        new_exp.goal_to_current=-1
        new_exp.curent_to_goal=-1
        if(len(self.experiences)>1):
            self.on_create_link(self.get_current_id(),len(experiences)-1)
        return len(self.experiences)-1
       
       
    '''    
       
       /**
 * create a new experience for a given position if accumulated odometric delta is over a given threshold
 * @param exp_id    PoseCell ID for new experience
 * @param snapped    not snapped before? if true -> create new experience, otherwise do nothing
 * @return            experience map ID of created new experience || return -1 := ERROR
 */
      '''  
    def on_create_experience(self,exp_id,snapped):
        if(not snapped):
            if self.accum_delta_x>0.1 and self.accum_delta_y>0.1:
                if(_EVAL):
                    if(self.exp_creation_Timestamp==0):
                        self.exp_creation_Timestamp=tospy.Time.now().to_sec()
                    time=rospy.Time.now().to_sec()-self.exp_creation_Timestamp
                    path=path_created_EXPs
                    if ID>=0:
                        path+=str(ID)
                    if len(self.experiences)==0:
                        p=Pair(0,0)
                        vec=[]
                        vec.append(p)
                        files.writeToFile(str(path),vec)
                    
                    else:
                        p=Pair(len(self.experiences,time))
                        vec=[]
                        vec.append(p)
                        writeToFile(str(path),vec)
                    new_exp=self.experiences.resize(len(self.experiences)+1)
                    new_exp=self.experiences(len(self.experiences)-1)
                if (len(self.experiences)==0):
                    new_exp.x_m=0
                    new_exp.y_m=0
                    new_exp.th_rad=0
                else:
                    new_exp.x_m=self.experiences[self.current_exp_id].x_m+self.accum_delta_x
                    new_exp.y_m=self.experiences[self.current_exp_id].y_m+self.accum_delta_y
                    new_exp.th_rad=self.clip_rad_180(self.accum_delta_facing)
            
                new_exp.id=len(self.experiences)-1
                new_exp.pc_id=exp_id
                new_exp.goal_to_current=-1
                new_exp.current_to_goal=-1
            
                time_diff_s=1/10
            
                if(len(self.experiences)!=1):
                    self.on_create_experience(self.get_current_id(),len(self.experiences)-1)
                
                return len(self.experiences)-1
            else:
                return self.current_exp_id
                    #ROS_ERROR_STREAM ("Not creating a new experience. New experience is too near to already existent one");

        return -1

    def clip_rad_180(self,angle):
        while angle <=-math.pi:
            angle+=2*math.pi
        while angle>=math.pi:
            angle-=2*math.pi
        return angle

    '''
    /** update the current position of the experience map based on odometric data
     *     (needed for new experience creation || link of experiences)
     * @param vtrans         (double) translational speed
     * @param vrot             (double) rotational speed
     * @param time_diff_s     (double) time-step
     */
'''
    
    def on_odo(self,vtrans,vrot,time_diff_s):
        #pdb.set_trace()
        vtrans=vtrans*time_diff_s
        vrot*=time_diff_s
        self.accum_delta_facing=self.clip_rad_180(self.accum_delta_facing+vrot)
        self.accum_delta_x=self.accum_delta_x+vtrans*math.cos(self.accum_delta_facing)
        self.accum_delta_y=+vtrans*math.sin(self.accum_delta_facing)
        self.accum_delta_time_s+=time_diff_s
 
    '''/**
 * Iterate the experience map. Perform a graph relaxing algorithm to allow
 * the map to converge partially.
 * @return    true
 */
'''
    
    def iterate(self):
        for i in range(self.EXP_LOOPS):
            for exp_id in range(len(self.experiences)):
                link_from=self.experiences[exp_id]
                for link_id in range(len(self.experiences[exp_id].links_from)):
                    #        //%             //% experience 0 has a link to experience 1

                    link=self.links[link_from.links_from[link_id]]
                    link_to=self.experiences[link.exp_to_id]

            #work out where e0 thinks e1 (x,y) should be based on the stored
            #link information
            
                        
                    
                    lx=link_from.x_m+link.d*math.cos(link_from.th_rad+link.heading_rad)
                    ly=link_from.y_m+link.d*math.sin(link_from.th_rad+link.heading_rad)
                    
                    
    
    #% correct e0 and e1 (x,y) by equal but opposite amounts
    #% a 0.5 correction parameter means that e0 and e1 will be fully
    #% corrected based on e0's link information
              
    
                    self.experiences[exp_id].x_m+=(link_to.x_m-lx)*self.EXP_CORRECTION
                    self.experiences[exp_id].y_m+=(link_to.y_m-ly)*self.EXP_CORRECTION
                    self.experiences[link.exp_to_id].x_m-=(link_to.x_m-lx)*self.EXP_CORRECTION
                    self.experiences[link.exp_to_id].y_m-=(link_to.y_m-ly)*self.EXP_CORRECTION
   
        #            //% determine the angle between where e0 thinks e1's facing
        #             //% should be based on the link information
                         
                    df=get_signed_delta_rad(link_from.th_rad+link.facing_rad,link_to.th_rad)
   
        #             //% correct e0 and e1 facing by equal but opposite amounts
        #             //% a 0.5 correction parameter means that e0 and e1 will be fully
        #             //% corrected based on e0's link information
                    
                    self.experiences[exp_id].th_rad=self.clip_rad_180(link_from.th_rad+df*self.EXP_CORRECTION)
                    self.experiences[link.exp_to_id].th_rad=self.clip_rad_180(self.experiences[link.exp_to_id].th_rad-df*self.EXP_CORRECTION)
        
            return True
    
    #  calculate the distace between two experiences
    
    def exp_euclidean_m(self, exp1, exp2):
        return math.sqrt((exp1.x_m-exp2.x_m)**2+(exp1.y_m-exp2.y_m)**2)
    
    
    def make_heap(self,heap,size):
        heap_size=len(heap)
        for i in reversed(range(0,heap_size//1)):
            heapify(heap,heap_size,predicate)
    
    def dijkstra_distance_between_experiences(self,id1,id2):
        exp_heap=Q.PriorityQueue()
        for id in range(len(self.experiences)):
            self.experiences[id].time_from_current_s=self.DBL_MAX   #DBL_MAX ???
            exp_heap.put(self.experiences[id])
        self.experiences[id1].time_from_current_s=0
        self.goal_path_final_exp_id=self.current_exp_id
        
        while not exp_heap.empty():
            self.make_heap(Experience(exp_heap),len(exp_heap))
            exp=Experience(exp_heap[0])
            if(exp.time_from_current_s==self.DBL_MAX):
                return self.DBL_MAX
            heappop(exp_heap)
        
            for id in range(len(exp.links_from)):
                link=self.links[exp.links_from[id]]
                link_time_s=exp.time_from_current_s+link.delta_time_s
                if link_time_s < self.experiences[link.exp_from_id].time_from_current_s:
                    self.experiences[link.exp_from_id].time_from_current_s=link_time_s
                    self.experiences[link.exp_from_id].goal_to_current=exp.id
            for id in range(len(exp.links_from)):
                link=self.links[exp.links_from[id]]
                link_time_s=exp.time_from_current_s+link.delta_time_s
                if link_time_s<self.experiences[link.exp_to_id].time_from_current_s:
                    self.experiences[link.exp_to_id].time_from_current_s=link_time_s
                    self.experiences[link.exp_to_id].goal_to_current=exp_id
                
                
            if exp.id==id2:
                return exp.time_from_current_s
        return self.DBL_MAX

    '''
    /**
     * create a link between two experiences
     * @param exp_id_from     experience-ID of link source, but not used anymore due to use of several EMs
     *                     //Invariant false when multiple EMs: exp_id_from != current_exp_id
                        //new Invariant: current_exp_id represents always current experience
     * @param exp_id_to        experience-ID of link destination
     * @return                true if link created successfully || else: false
     */
    '''


    def on_create_link2(self,exp_id_from,exp_id_to,rel_rad):
        for i in range(len(self.experiences[exp_id_from].links_from)):
            if self.links[self.experiences[self.current_exp_id].links_from[i]].exp_to_id ==exp_id_to:
                return False
        for i in range(len(self.experiences[exp_id_to].links_from)):
            if self.links[self.experiences[exp_id_to].links_from[i]].exp_to_id==exp_id_from:
                return False
        
        l=Link()
       
        l.exp_to_id=exp_id_to
        l.exp_from_id=exp_id_from
        l.d=math.sqrt(self.accum_delta_x**2+self.accum_delta_y**2)
        l.heading_rad=get_signed_delta_rad(self.experiences[exp_id_from].th_rad,math.atan2(self.accum_delta_y,self.accum_delta_x))
        l.facing_rad=get_signed_delta_rad(self.experiences[exp_id_from].th_rad,self.clip_rad_180(self.accum_delta_facing+rel_rad))
        l.delta_time_s=self.accum_delta_time_s
        self.links.append(l)
        self.experiences[exp_id_from].links_from.append(len(self.links)-1)
        self.experiences[exp_id_to].links_to.append(len(self.links)-1)
        return True
    
    
    def show_experiences(self):
        for i in range(len(self.experiences)):
            experience_trace.write("id: "+ str(self.experiences[i].id)+"pc_id: "+str(self.experiences[i].pc_id)+"xm: "+str(self.experiences[i].x_m)+"ym: "+str(self.experiences[i].y_m)+"th_rad: "+str(self.experiences[i].th_rad)+"vt_id: "+str(self.experiences[i].vt_id)+"links_from: "+str(self.experiences[i].links_from)+"links_to: "+str(self.experiences[i].links_to))
            experience_trace.write("\n")
    def calculate_path_to_goal(self,time_s):
        
        waypoint_exp_id=-1
        if(len(self.goal_list)==0):
            
            return False
        
        if(self.exp_euclidean_m(self.experiences[self.current_exp_id], self.experiences[self.goal_list[0]])<0.1 \
            or ((self.goal_timeout_s!=0) and time_s>self.goal_timeout_s)):
            if self.goal_timeout_s!=0 and time_s>self.goal_timeout_s:
                self.goal_success=False
            if(self.exp_euclidean_m(self.experiences[self.current_exp_id],self.experiences[self.goal_list[0]])<0.1):
                self.goal_success=True
            self.goal_list.pop()
            self.goal_timeout_s=0
            for id in range(len(self.experiences)):
                self.experiences[id].time_from_current_s=self.DBL_MAX
        
        if len(self.goal_list)==0:
            return False
        
        if  len(self.goal_list)==0:
            return False
        if self.goal_timeout_s==0:
            exp_heap=Q.PriorityQueue()
        for id in range(len(self.experiences)):
            self.experiences[id].time_from_current_s=self.DBL_MAX
            exp_heap.put(self.experiences[id])
            
        self.experiences[self.current_exp_id].time_from_current_s=0
        goal_path_final_exp_id=self.current_exp_id
        self.make_heap(exp_heap,qsize(lexp_heap))
        
        while not exp_heap.empty():
            
            exp=exp_heap.top()
            print exp.id
            if exp.time_from_current_s==self.DBL_MAX:
                print " enable to find path to goal \n"
                self.goal_list.pop()
                return False
            exp_heap.pop()
            
            for id in range(len(exp.links_to)):
                link=self.links[exp.links_to[id]]
                link_time_s=exp.time_from_current_s+link.delta_time_s
                if link_time_s<self.experiences[link.exp_from_id].time_from_current_s:
                    self.experiences[link.exp_from_id].time_from_current_s=link_time_s
                    self.experiences[link.exp_from_id].goal_to_current=exp.id
            for id in range(len(exp.link_from)):
                link=self.links[exp.links_from[id]]
                link_time_s=exp.time_from_current_s+link.delta_time_s
                if link_time_s<self.experiences[link.exp_to_id].time_from_current_s:
                    self.experiences[link.exp_to_id].time_from_current_s=link_time_s
                    self.experiences[link.exp_to_is].goal_to_current=exp.id
                    
                    
            if not exp_heap.empty():
                make_heap(exp_heap,len(exp_heap))
            
        trace_exp_id=self.goal_list[0]
        while trace_exp_id!=self.current_exp_id:
            self.experiences[self.experiences[trace_exp_id].goal_to_current].current_to_goal=trace_exp_id
            trace_exp_id=self.experiences[trace_exp_id].goal_to_current
            
        if goal_timeout_s==0:
            goal_timeout_s=time_s+self.experiences[self.goal_list[0]].time_from_current_s
            print "Goal timeout in",goal_timeout_s-time_s,"s","\n"
        
        return True
    
    
    def get_goal_waypoint(self):
        if len(self.goal_list)==0:
            return False
        waypoint_exp_id=-1
        trace_exp_id=self.goal_list[0]
        robot_exp=self.experiences[self.current_exp_id]
        while trace_exp_id!=self.goal_path_final_exp_id:
            dist=self.exp_euclidean_m(self.experiences[trace_exp_id], robot_exp)
            waypoint_exp_id=self.experiences[trace_exp_id].id
            if dist< 0.2:
                break
            trace_exp_id=self.experiences[trace_exp_id].goal_to_current
            
        if waypoint_exp_id==-1:
                waypoint_exp_id=self.current_exp_id
                
        return True 
    
    def add_goal2(self,x_m,y_m):
        if x_m>=sys.maxsize or y_m>=sys.maxsize:
            self.goal_list.clear()
            return 
        min_id=-1
        min_dist=self.DBL_MAX
        if self.MAX_GOALS!=0 and len(self.goal_list)>self.MAX_GOALS:
            return
        #str_buff=str(len(self.experiences))    
        
        #sys.stderr.write(str(len(self.experiences))
        
        for i in range(len(self.experiences)):
            dist=math.sqrt((self.experiences[i].x_m-x_m)**2+(self.experiences[i].y_m-y_m)**2)
            if dist<min_dist:
                min_id=i
                min_dist=dist
        
        
        if min_dist<0.1:
            self.add_goal(min_id)
            #str="ExperienceMap::add_goal|Goal [experience"+str(min_id)+"ADDED ("+len(self.goal_list)+"goal in the list"
            #rospy.loginfo(str)
        else:
            print "EXperienceMap::addgoal|GOAL NOT ADDED :>(min_dist<0.1"  #can't fine the equivalent function in python'
            
            
    def get_current_goal_id(self):
        if len(self.goal_list)==0:
            return -1
        else:
            return self.goal_list.pop()
        
        
    def get_goals(self):
        return self.goal_list
    
    
    def get_goal_path_final_exp(self):
        return goal_path_final_exp_id
    
    def get_experience(self,id):
        return self.experiences[id]
    
    def get_num_link(self):
        return len(self.links)
    
    def on_create_experience(self,exp_id,snapped):
        if not snapped:
                if self._EVAL==True:
                    if self.exp_creation_Timestamp==0:
                        self.exp_creation_Timestamp=rospy.Time.now()
                    time=rospy.Time.now()-self.exp_creation_Timestamp
                    path=path_created_EXPs
                    if self.ID>=0:
                        path+=str(self.ID)
                    if len(self.experiences)==0:
                        p=Pair(0,0)
                        vec=[]
                        vec.append(p)
                        WriteToFile(path,vec)
                    else:
                        p=Pair(len(self.experiences),time)
                        vec=p
                        WriteToFile(path,vec)
                if(len(self.experiences)==0):
                    self.experiences[len(self.experiences)].x_m=0
                    self.experiences[len(self.experiences)].y_m=0
                    self.experiences[len(self.experiences)].th_m=0
                else:
                    self.experiences[len(self.experiences)].x_m=self.experiences[self.current_exp_id].x_m+self.accum_delta_x
                    self.experiences[len(self.experiences)].y_m=self.experiences[self.current_exp_id].y_m+self.accum_delta_y
                self.experiences[len(self.experiences)].id=len(self.experiences)
                self.experiences[len(self.experiences)].pc_id=exp_id
                self.experiences[len(self.experiences)].th_rad=self.clip_rad_180(self.accum_delta_facing)
                self.experiences[len(self.experiences)].goal_to_current=-1
                self.experiences[len(self.experiences)].current_to_goal=-1
                
                
                
                
                self.experiences[len(self.experiences)].vObjects=self.get_objects()
                
                
                
                time_diff_s=1/10
                if len(self.experiences)!=1:
                    self.on_create_link(self.get_current_id(),len(self.experiences)-1)
                
                
                
                
                return len(self.experiences)-1
    '''
       
    /**
     * create a link between two experiences
     * @param exp_id_from     experience-ID of link source, but not used anymore due to use of several EMs
     *                     //Invariant false when multiple EMs: exp_id_from != current_exp_id
                        //new Invariant: current_exp_id represents always current experience
     * @param exp_id_to        experience-ID of link destination
     * @return                true if link created successfully || else: false
    '''         
            
    def on_create_link(self,exp_id_from,exp_id_to):
        dest_id=self.get_em_id_from_pc_id(exp_id_to)
        if dest_id>=0:
            exp_id_to=dest_id
        else:
            rospy.logerr("ERROR :dest_id<0")
            return False
    
        '''//exp_id_from is not used anymore due to use of several EMs
    //Invariant false when multiple EMs: exp_id_from != current_exp_id
    //new Invariant: current_exp_id represents always current experience
'''
        
        exp_id_from=current_exp_id
        
        
        for i in range(len(self.experiences[exp_id_from].link_from)):
            if (len(self.experiences[current_exp_id].links_from)>0):
                if self.links[self.experiences[self.current_exp_id].links_from[i]].exp_to_id==exp_id_to:
                    return False
        self.links[len(self.links)].exp_to_id=exp_id_to
        self.links[len(self.links)].exp_from_id=exp_id_from
        self.links[len(self.links)].d=math.sqrt(self.accum_delta_x**2+self.accum_delta_y**2)
        self.links[len(self.links)].heading_rad=self.get_signed_delta_rad(self.current_exp.th_rad,math.atan2(self.accum_delta_y, self.accum_delta_x))
        self.links[len(self.links)].facing_rad=self.get_signed_delta_rad(self.current_exp.th_rad,self.accum_delta_facing)
        self.links[len(self.links)].delta_time_s=self.accum_delta_time_s
   #        // add this link to the 'to exp' so we can go backwards through the em
     
        self.experiences[exp_id_from].links_from.append(len(self.links)-1)
        self.experiences[exp_id_to].links_to.append(len(self.links)-1)
        
        return True
    
    
    
    def get_em_id_from_pc_id(self,src_pc_exp_id):
        if ((src_pc_exp_id>=0)and (len(self.experiences)>0)):
            for i in range(len(self.experiences)):
                if self.experiences[i].pc_id==src_pc_exp_id:
                    return i
                
        return -1
    '''
/**
 * change the current experience
 *     tests for non existent experienceID (if new_exp_id < 0)
 * @param new_exp_id     ID of experience to set to
 * @param reset_odo        default: true | set false if odometry should not be resetted
 * @return    1 if successful | 0 if not
 */'''
    
    
    def on_set_experience(self,new_exp_id,reset_odo):
        if self._EVAL==True:
            reset=dict()
            if ID in reset:
                reset[ID]=True
                
            if self.exp_active_Timestamp==0:
                self.exp_active_Timestamp=rospy.Time.now().to_sec()
            time=rospy.Time.now().to_sec()-self.exp_active_Timestamp
            path=path_current_EXPs
            if self.ID>=0:
                path+=str(self.ID)
            if reset[self.ID]==True:
                p=Pair(0,0)
                WriteToFile(str(path),p,False)
                reset[self.ID]=False
            else:
                p=Pair(new_exp_id,time)
                WriteToFile(str(path),p)
        if new_exp_id<0:
            return -1
        src_id=-1
        src_id=self.get_em_id_from_pc_id(new_exp_id)
        
        new_exp_id=src_id
        if new_exp_id>len(self.experiences)-1:
            return 0
        if new_exp_id==self.current_exp_id:
            return 1
        prev_exp_id=self.current_exp_id
        self.current_exp_id=new_exp_id
        if reset_odo==True:
            self.accum_delta_x=0
            self.accum_delta_y=0
            self.accum_delta_facing=self.experiences[self.current_exp_id].th_rad
            
        return 1
    def get_current_id(self):
        return self.current_exp_id
    
    def get_num_experiences(self):
        return len(self.experiences)
    
    def get_num_links(self):
        return  len(self.links)
    
    
    def get_link(self,id):
        return self.links[id]
    def add_goal(self,id):
        self.goal_list.append(id)

    def get_objects(self):
        i=0
        objects_index=[]
        while i<10:
            index=random.randint(1,10)
            objects_index.append(index)
            i+=1
        return objects_index