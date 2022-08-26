#version 2.0 use the <type> factor to identify whether the labour cost OR the working hours need to be estimated

import math

def estimate(type=None,size=1,other=None):
    if type==1: # type 1 is to estimate the labour cost, factor <other> represents the working hours
        labour=math.ceil(size*80/other)
        time_minute=math.ceil(other*60)
        print('%d labours are required to acomplish the %.1f standard-sized project in %.1f working hours (%d minutes)' %(labour,size,other,time_minute))
        
    if type==2: # type 2 is to estimate the working hours, factor <other> represents the labour cost
        time=size*80/other
        time_minute=math.ceil(time*60)
        print('%.1f working hours (%d minutes) are required to acomplish the %.1f standard-sized project in %d labours' %(time,time_minute,size,other))

estimate(1,2,20)