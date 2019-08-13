from itertools import cycle
def optimalPoint(m,d):
    start = 0
    i = 1
    j=0
    p = m[0] - d[0] + m[1]
    while i< len(m)-1:
        j = 0
        p = p - d[i] + m[i + 1]
        if i == len(m)-1:
            p = p - d[i + 1]
        if p<=0:
            start+=1
            j=-1
        else:
            return start
        i+=1

    if j==-1:
        return -1

    # for i in range(1,len(m)-1):
    #     p = p -d[i]+m[i+1]
    #     print(p)
    #     # for k in range(i):
    #     #     p = p - d[k]+m[k+1]
    #     #     print(p)
    # p = p - d[i+1]
    # if i
    # print(p)


# magic = [10,6,3,8,1]
# dist = [1,3,8,4,3]
# magic = [2,4,5,2]
# dist = [4,3,1,3]
magic = [8,4,1,9]
dist = [10,9,3,5]
r = optimalPoint(magic,dist)
print("Result=",r)