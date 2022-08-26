list=int(input('sequence length = '))

seq=[0]*list

seq[0]=1
seq[1]=1

def f(x):
    seq[x+2]=seq[x+1]+seq[x]

for i in range(list-2):
    f(i)

print (seq)