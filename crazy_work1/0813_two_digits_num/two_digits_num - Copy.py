# find all two digits numbers, whose ones' place and tens' place has a sum. Such sum should has 6 at its ones' place.
# For example, 88 has both 8 at its ones' place and the tens's place. They have a sum of 16, and 16's ones' place is 6

k=0

for i in range(1,10):
    for j in range(10):
        if (i+j)%10 == 6:
            k=k+1
            print ('the %d number is %d' %(k,10*i+j))