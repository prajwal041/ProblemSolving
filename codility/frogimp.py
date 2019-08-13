def solution(x,y,d):
    if y<x or d<=0:
        return 0
    if (y-x)%d==0:
        return (y-x)//d
    else:
        return ((y-x)//d)+1

x = 10
y = 85
d = 30
print(solution(x,y,d))