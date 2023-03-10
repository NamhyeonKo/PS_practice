N, K = map(int, input().split())
MOD = 1000000000

dp = [[0] * (N+1) for _ in range(K+1)]
dp[0][0] = 1

# 2차 배열로 가로를 N,세로를 K로 놓고 풀면
# 윗 줄의 자기 인덱스까지의 합이 결과값이 됨 
for i in range(1,K+1):
    for j in range(N+1):
        dp[i][j] = sum(dp[i-1][0:j+1])

print(dp[K][N] % MOD)