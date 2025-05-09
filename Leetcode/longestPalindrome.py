"""
Problem: https://leetcode.com/problems/longest-palindromic-substring/
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
"""
import time
def get_runtime(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        runtime = end-start
        print(f"Function: {func.__name__} took {runtime} seconds.!")
        return result
    return wrapper

@get_runtime
def long_palindrome(s):
    res = ""
    resLen = 0
    for i in range(len(s)):
        # odd Length
        l, r = i, i
        while l>=0 and r<len(s) and s[l] == s[r]:
            if (r-l+1)> resLen:
                res = s[l:r+1]
                resLen = r-l+1
            l-=1
            r+=1
        # even Length
        l, r = i, i+1
        while l>=0 and r<len(s) and s[l] == s[r]:
            if (r-l+1)>resLen:
                res = s[l:r+1]
                resLen = r-l+1
            l-=1
            r+=1
    return res

s = "babad"
print(long_palindrome(s))