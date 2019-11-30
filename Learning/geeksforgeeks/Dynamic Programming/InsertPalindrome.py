'''
Find the minimum number of insertions in the substring str[l+1,…….h].
Find the minimum number of insertions in the substring str[l…….h-1].
Find the minimum number of insertions in the substring str[l+1……h-1].
'''

def findMinInsertion(s,n):
    table = [[0 for i in range(n)] for i in range(n)]
    l,h,gap = 0,0,0
    for gap in range(1,n):
        l=0
        for h in range(gap,n):
            if s[l]==s[h]:
                table[l][h]=table[l+1][h-1]
            else:
                table[l][h]=min(table[l][h-1], table[l+1][h])+1
            l+=1
    return table[0][n-1]

n = int(input())
for _ in range(n):
    s = input()
    print(findMinInsertion(s, len(s)))