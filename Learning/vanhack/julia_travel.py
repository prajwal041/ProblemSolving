src = [1,2,4,6]
dst = [3,3,3,4]
t=1
hash = {}
for j in src:
    i = 1
    while i <= j:
        if (j % i == 0):
            hash[j]=i
        i = i + 1
res1=[]
for i in src:
    if hash[i]>t:
        res1.append(1)
    else:
        res1.append(0)

hash={}
for j in dst:
    i = 1
    while i <= j:
        if (j % i == 0):
            hash[j]=i
        i = i + 1
res2=[]
for i in dst:
    if hash[i]>t:
        res2.append(1)
    else:
        res2.append(0)

print(res1)
print(res2)
res = []
for i in range(len(res1)):
    res.append(res1[i] and res2[i])

print(res)
