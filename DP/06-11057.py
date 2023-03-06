MOD = 10007
N = int(input())

dp = [[0]*10 for i in range(N+1)]
# 숫자가 0부터 시작 가능하므로 모두 1로 채우기
# ex) 01234 도 5자리 오르막수
dp[1] = [1,1,1,1,1,1,1,1,1,1]

for i in range(2,N+1):
    for j in range(10):
        # 가능한 경우는 자기 자신 수보다 같거나 큰 모든 경우가 가능하니깐 앞(i-1)에 있는 경우를 더함.
        # 자기 자신부터 9까지(9포함) 경우를 더함
        dp[i][j] = sum(dp[i-1][j:10])

print(sum(dp[N]) % MOD)