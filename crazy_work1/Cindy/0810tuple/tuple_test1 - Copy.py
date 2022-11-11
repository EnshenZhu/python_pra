test=(1,2,5,7,9,10,11,12,13,14,15)
for n in range(len(test)-1):
    if test[n+1]-test[n]!=1:
        print(test[n])