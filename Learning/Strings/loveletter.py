'''
Problem: https://www.hackerrank.com/challenges/the-love-letter-mystery/problem

'''
def love(s):
    c = 0
    for i in range(len(s)//2):
        c+=abs((ord(s[i]))-ord(s[len(s)-i-1]))
    print(c)

s = input()
love(s)
'''
Input: abcd
Output: 4
Explanation:
abcd -->abcc(1)-->abcb(2)-->abca(3)-->abba(4)

Time T ~ O(n)
Space S ~ O(n)
'''