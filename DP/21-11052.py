import sys

N = int(sys.stdin.readline())
P = list(map(int,sys.stdin.readline().split()))

dp = [0] * (N+1)

for i in range(1,N+1):
    # 약간 퀵 정렬 느낌으로 사용
    j = 0
    k = i
    dp[i] = P[i-1]

    # 양 끝 인덱스부터 시작해서 둘이 만날때까지 확인하기
    # N이 4인 경우 0-4, 1-3, 2-2 인경우 비교해서 최대값을 dp에 저장
    while(j <= k):
        if dp[j] + dp[k] > dp[i]:
            dp[i] = dp[j] + dp[k]
        j += 1
        k -= 1

print(dp[N])