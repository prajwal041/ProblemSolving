def decode(s):
    n = len(s)+1
    dp = [0] * n
    dp[0] = 1

    for i in range(1, n):
        if s[i-1] in '123456789':
            dp[i] = dp[i-1]
        if i>1 and '10' <=s[i-2:i] <= '26':
            dp[i]+=dp[i-2]

    return dp[-1]


s = input()
print(decode(s))