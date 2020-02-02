def staircase_recursive(n):
    if n<=1:
        return 1
    return staircase_recursive(n-1) + staircase_recursive(n-2)

def staircase_bottm_up(n):
    dp = [0] * (n+1)
    dp[0] = 1
    dp[1] = 1
    if n == 0 or n==1:
        return 1
    for i in range(2,n+1):
        dp[i] = dp[i-1]+dp[i-2]
    return dp[n]

def staircase_dp(n):
    a,b = 1,2
    for i in range(n-1):
        a,b = b, a+b
    return a

def staircase_with_steps_dp(n,x):
    dp = [0]*(n+1)
    dp[0] = 1
    dp[1] = 1
    if n == 0 or n==1:
        return 1
    for i in range(2, n+1):
        dp[i]+=sum(dp[i-j] for j in x if i-j >=0)
    return dp[n]

n = 4
print(f"Recursive approach {staircase_recursive(n)}")
print(f"Dynamic Programming approach {staircase_dp(n)}")
print(f"Bottom-up approach {staircase_bottm_up(n)}")

x = [1,2]
print(f"With steps {staircase_with_steps_dp(4,x)}")

