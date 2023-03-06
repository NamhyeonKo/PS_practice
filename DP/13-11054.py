# 11053번 문제와 11722문제를 응용해야할 것 같음
# 가운데를 기준으로 lsi를 양쪽으로 돌리는게 나을지도?

# LSI에 대해 공부하기
# DP로 풀면 O(n^2)
import sys

N = int(sys.stdin.readline())

num1 = list(map(int, sys.stdin.readline().split()))
num2 = list(reversed(num1))
dp1 = [1 for _ in range(N)]
dp2 = [1 for _ in range(N)]
dp3 = [0 for _ in range(N)]

for i in range(N):
    # 일반적인 LSI 구하기
    for j in range(i):
        if num1[i] > num1[j]:
            dp1[i] = max(dp1[j]+1,dp1[i])

for i in range(N):
    # 일반적인 LSI 구하기
    # 리버스한 배열이라 똑같이 LSI 하면 원래 작아지는 수열 구할 수 있음
    for j in range(i):
        if num2[i] > num2[j]:
            dp2[i] = max(dp2[j]+1,dp2[i])

for i in range(N):
    # d3에 더할건데 문제는 둘 중에 하나가 0인 경우
    # 즉 증가만 하거나 감소만 하는 경우에는 1을 더해줘서 나중에 겹치는 1을 빼줄 때 수가 달라지지 않게 하기
    k = dp1[i] + dp2[N-i-1]
    if (dp1[i] == 0) & (dp2[N-i-1] == 0):
        k += 1
    dp3[i] = max(dp3[i],k - 1)

print(max(dp3))
