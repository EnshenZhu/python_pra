#version 2.0 <type> factor is for identifying whether the labour cost OR the working hours need to be estimated
#version 2.1 enhancing the user-friendly property, by which users can input the factors while running the program

import math

def estimate(type=None,size=1,other=None):
    if type==1: # type 1 is to estimate the labour cost, factor <other> represents the working hours
        labour=math.ceil(size*80/other)
        time_minute=math.ceil(other*60)
        print('%d labours are required to acomplish the %.1f standard-sized project in %.1f working hours (%d minutes)' %(labour,size,other,time_minute))
        
    if type==2: # type 2 is to estimate the working hours, factor <other> represents the labour costed
        time=size*80/other
        time_minute=math.ceil(time*60)
        print('%.1f working hours (%d minutes) are required to acomplish the %.1f standard-sized project in %d labours' %(time,time_minute,size,other))

type=int(input('press 1 to estimate the required labour cost, press 2 to estimate the required working hours'
               '\n type='))
if type==1:
    estimate(type,
         size=float(input('What is size of the project, decimal number can be accepted'
                        '\n size=')),
         other=float(input('How many working hours are given, decimal number can be accepted'
                         '\n hours='))
         )
    
if type==2:
    estimate(type,
         size=float(input('What is size of the project, decimal number can be accepted'
                        '\n size=')),
         other=float(input('How many labours are given, decimal number can be accepted'
                         '\n labours='))
         )