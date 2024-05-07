n = int(input())  # input

dp = [0] * (1000 + 1)

dp[1] = 1
dp[2] = 2
dp[3] = 1
 
for i in range(4, n+1):
    dp[i] = dp[i-3] + 1

print('SK' if dp[n]%2 else 'CY')