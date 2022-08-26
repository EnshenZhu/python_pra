import math

#define the function with three factors, the size, the labour and the time
def estimate(size=1,labour=None,time=None):
    
    #the function is used to estimate the labour required in given size and time
    if (labour==None) and (time!=None):
        labour=math.ceil(size*80/time)
        time_minute=math.ceil(time*60)
        print('%d labours are required to acomplish the %.1f standard-sized project in %.1f working hours (%d minutes)' %(labour,size,time,time_minute))
        
    #the function is used to estimate the time required in given size and labour
    elif (labour!=None) and (time==None):
        time=size*80/labour
        time_minute=math.ceil(time*60)
        print('%.1f working hours (%d minutes) are required to acomplish the %.1f standard-sized project in %d labours' %(time,time_minute,size,labour))
    
    #function error (has three none-null factors)
    elif (labour!=None) and (time!=None):
        
        #reset the factors
        x=int(input('Factors error, press 1 to reset labour, press 2 to reset time, your choice = '))
        if x==1:
            estimate(size=int(input('size=')),labour=int(input('labour=')),time=None)
        elif x==2:
            estimate(size=int(input('size=')),time=int(input('labour=')),labour=None)
        else:
            print('Your choice is beyond the requirement')
            estimate(1,1,1)            
        
estimate(size=1.5,labour=2)
estimate(size=0.7,labour=20.0)
estimate(time=70)
estimate(1,1,1)