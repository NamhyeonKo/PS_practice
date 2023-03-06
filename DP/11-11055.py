# LSI에 대해 공부하기
# DP로 풀면 O(n^2)
import sys

N = int(sys.stdin.readline())

num = list(map(int, sys.stdin.readline().split()))
dp = [1 for _ in range(N)]
sum = [0 for _ in range(N)]
sum[0] = num[0]

for i in range(1,N):
    for j in range(i):
        if num[i] > num[j]:
            dp[i] = max(dp[j]+1,dp[i])
            sum[i] = max(sum[i],sum[j] + num[i])
        # 그냥 수 하나가 이제까지 부분 수열의 합보다 클 수 있으므로 max로 비교해서 넣어주기
        else:
            sum[i] = max(sum[i],num[i])

print(max(sum))