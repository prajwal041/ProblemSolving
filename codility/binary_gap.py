def solution(n):
    maxi = 0
    current = 0

    while n>0 and n%2==0:
        n//=2
    while n>0:
        remainder = n%2
        if remainder ==0:
            current+=1
        elif current!=0:
            maxi = max(current,maxi)
            current=0
        n//=2
    return maxi

n=9
print(solution(n))