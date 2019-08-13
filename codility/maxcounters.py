def solution(n,a):
    result = [0]*n
    for i in a:
        if 1<=i<=n:
            result[i-1]+=1
        else:
            result[:]=[max(result)]*n
    return result

a = [3,4,4,6,1,4,4]
print(solution(5,a))