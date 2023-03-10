N = int(input())

def dynamicp(N):
    N = N // 2
    dp = [3, 11]
    # 점화식을 구하면 직전 경우의 4배에 전전 경우를 뺀거랑 같음
    for i in range(2,N):
        dp.append(dp[i-1]*4 - dp[i-2])
    print(dp[N-1])

if N % 2 == 1:
    print(0)
else:
    dynamicp(N)