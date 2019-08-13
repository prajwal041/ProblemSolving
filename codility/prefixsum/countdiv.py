def solution(a,b,k):
    if a%k==0:
        return (b-a)//k+1
    else:
        return (b-(a-a%k))//k

a=6
b = 11
k=2
print(solution(a,b,k))