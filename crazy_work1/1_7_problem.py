#find out i and j in 1/i+1/j=1/7, i and j should not be identical

k=0
for i in range(1,101):
        for j in range(1,i+1):
                if (i!=j) and (1/i+1/j==1/12):
                        k=k+1
                        print('the %d combination is %d and %d' %(k,i,j))