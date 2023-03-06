import sys

N = int(sys.stdin.readline())

wine = [0] * N
dp = [0] * N

for i in range(N):
    wine[i] = int(sys.stdin.readline())

dp[0] = wine[0]

# N > 1
if N > 1:
    dp[1] = wine[0] + wine[1]
# N > 2
if N > 2:
    dp[2] = max(dp[1], wine[2]+wine[1], wine[2]+wine[0])

# 그 뒤의 경우
for i in range(3,N):
    dp[i] = max(dp[i-1],dp[i-2]+wine[i],dp[i-3]+wine[i-1]+wine[i])

print(dp[N-1])