'''
Reverse words in a given string

Input:
2
i.like.this.program.very.much
pqr.mno

Output:
much.very.program.this.like.i
mno.pqr

T ~ O(n)
S ~ O(1)
'''

def solution(n):
    for _ in range(n):
        seperator = '.'
        print(seperator.join(input().split('.')[::-1]))

n = int(input())
solution(n)