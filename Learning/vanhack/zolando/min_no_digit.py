'''
Find minimum no the in the digits range
1. n =9 ----->0
2. n = 95 --->10
3. n = 125 -->100
'''
def solution(n):
    if n>=0 and n<=9:
        return 0
    else:
        n=len(str(n))
        result = '1'
        for i in range(n-1):
            result+='0'
        return int(result)

n = int(input())
print(solution(n))