import sys

N = int(sys.stdin.readline())

stair = [0] * N
dp = [0] * N

for i in range(N):
    stair[i] = int(sys.stdin.readline())

dp[0] = stair[0]

# 2156(wine) 문제랑 똑같은데 다른점은
# wine은 해당 와인이 나와도 지나갈 수 있지만
# 계단은 밟으면 무조건 횟수에 들어가기 때문에 경우가 본인이 포함된 경우만 가능

# N > 1
if N > 1:
    dp[1] = stair[0] + stair[1]
# N > 2
if N > 2:
    dp[2] = max(stair[2]+stair[1], stair[2]+stair[0])

# 그 뒤의 경우
for i in range(3,N):
    dp[i] = max(dp[i-2]+stair[i],dp[i-3]+stair[i-1]+stair[i])

print(dp[N-1])