import math

def writeToFiles(filename,value):
    if filename==None:
        return -1
    f=open(filename,'a')
    f.write(value)
    f.write("\n")
    f.close()
    return 0


def clip_rad_180(angle):
    while angle > math.pi:
        angle-=2.0*math.pi
    while angle<=-math.pi:
        angle+=2.0*math.pi
    return angle

def get_signed_delta_rad(angle1,angle2):
    dir=clip_rad_180(angle1-angle1)
    delta_angle=clip_rad_180(angle1)-clip_rad_180(angle2)
    delta_angle=abs(delta_angle)
    if delta_angle<2.0*math.pi-delta_angle:
        if dir>0:
            return delta_angle
        else:
            return -delta_angle
    else:
        if dir>0:
            return 2.0*math.pi-delta_angle
        else:
            return -(2.0*math.pi-delta_angle)

