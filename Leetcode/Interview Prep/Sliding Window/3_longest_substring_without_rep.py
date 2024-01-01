def longestSubstring(s):
    if len(s) == 0 or len(s) == 1:
        return len(s)
    count = 0
    l = 0
    charSet = set()
    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l+=1
        charSet.add(s[r])
        count = max(count, r-l+1)
    return count

s = "abcabcbb"
print(longestSubstring(s))

'''
Time : O(n)
space : O(n)
'''