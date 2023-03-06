N = int(input())

dp = [0] * (N+1)
dp[1] = 1

# n = 7 인 경우까지 찾아보니깐 그냥 피보나치 수열처럼 되길래 해봄
for i in range(2,N+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[N])