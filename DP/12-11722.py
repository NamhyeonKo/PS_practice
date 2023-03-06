# LSI에 대해 공부하기
# DP로 풀면 O(n^2)
import sys

N = int(sys.stdin.readline())

num = list(map(int, sys.stdin.readline().split()))
dp = [1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if num[i] < num[j]:
            dp[i] = max(dp[j]+1,dp[i])

print(max(dp))