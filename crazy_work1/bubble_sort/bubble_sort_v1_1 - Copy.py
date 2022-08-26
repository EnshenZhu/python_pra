#bubble sort

def bubble_sort(array):
    n=len(array)
    for i in range(n):
        for j in range(0,n-i-1):
            if(array[j]>array[j+1]):
               array[j], array[j+1]=array[j+1], array[j] 
               #line 7,8,9 can be used to find out the local maximum number in each round of the i loop
               
    return array
               
list1=[20,15,17,33,50,22]

print(list1)
print(bubble_sort(list1))