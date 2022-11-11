#bubble sort
#all units in list1 are random numbers

import random

def bubble_sort(array):
    n=len(array)
    for i in range(n):
        for j in range(0,n-i-1):
            if(array[j]>array[j+1]):
               array[j], array[j+1]=array[j+1], array[j] 
               #line 7,8,9 can be used to find out the local maximum number in each round of the i loop
               
    return array
               
list1=[]
for _ in range(10):
    list1.append(random.randint(0,100))

print(list1)
print(bubble_sort(list1))