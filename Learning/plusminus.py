n = int(input())
li = list(input())
lst = list(map(float,li))
min=plu=nue=0
count = 0
for i in lst:
    if i< 1:
        min +=1
    elif i > 1:
        plu +=1
    else:
        nue +=1
    count +=1
print(float(min/n))
print(float(plu/n))
print(float(nue/n))


n = float(input())
lst = [int(x) for x in input().split()]
print(format(len([x for x in lst if x > 0])/n, ".6f"))
print(format(len([x for x in lst if x < 0])/n, ".6f"))
print(format(len([x for x in lst if x == 0])/n, ".6f"))