def solution(a):
    occurence = [False]*(len(a)+1)
    for i in a:
        if 1<=i<=len(a)+1:
            occurence[i-1]=True
    for i in range(len(a)+1):
        if occurence[i]==False:
            return i+1
    return -1


a = [1,4,6,5,1,2]
# a =list(set(a))
print(solution(a))