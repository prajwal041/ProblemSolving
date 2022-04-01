
n = '011100'
v = int(n,2)
count = 0
while v!=0:
    if v%2==0:
        v = v/2
    elif v%2==1:
        v-=1
    count+=1
print(count)
