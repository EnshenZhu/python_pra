import random

def zero_one():
    num_list=[]
    for i in range(200):
        num_list.append(random.randint(0,1))  #genarating a list with 200 units of 0 or 1
    
    count_of_zero=0
    count_of_one=0
    
    for j in num_list:
        if j==0:
            count_of_zero+=1
        else:
            count_of_one+=1  #count for 0 and 1
            
    return count_of_one,count_of_zero,num_list

cum_one_percent=0
cum_zero_percent=0


for round in range(100):
    cum_one_percent+=(zero_one()[0])/len(zero_one()[2])
    cum_zero_percent+=(zero_one()[1])/len(zero_one()[2])
    
print('one% = ',cum_one_percent/100)
print('zero% = ',cum_zero_percent/100)