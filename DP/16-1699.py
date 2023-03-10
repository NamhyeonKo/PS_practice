# dp에 앞의 수들의 최솟값 저장

N = int(input())
dp = [0] * (N+1)
doubled = []

for i in range(1,N+1):
    # 제곱수이면 그냥 1
    if (i**(1/2)) % 1 == 0:
        dp[i] = 1
        doubled.append(i)
        continue
    
    # 아닌 경우는 앞의 제곱수에서 최선의 경우를 찾아야 함
    # 각 제곱수 경우(1) + 제곱수를 뺀수의 경우를 더한게 최소가 되게 찾음
    # 시간 복잡도(O(n*logn))를 줄이는 방법은 모르겠음... -> 일단 백준에서는 통과?
    minc = i
    for k in doubled:
        if 1 + dp[i-k] < minc:
            minc = 1 + dp[i-k]
    dp[i] = minc

print(dp[N])