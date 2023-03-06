import sys

def dp():
    N = int(sys.stdin.readline())
    dp1 = list(map(int, sys.stdin.readline().split()))
    dp2 = list(map(int, sys.stdin.readline().split()))

    for i in range(1,N):
        # i가 1인 경우는 무조건 대각선 밖에 없으므로 그 경우를 더해줌
        if i == 1:
            dp1[i] += dp2[i-1]
            dp2[i] += dp1[i-1]
        # 나머지 경우에선 대각선 2칸 앞에 자기 줄이랑 1칸 앞에 다른 줄 중에 큰 값을 더함
        # 저장되어 있는 값이 이전까지의 최대값이므로
        else:
            dp1[i] += max(dp2[i-1],dp2[i-2])
            dp2[i] += max(dp1[i-1],dp1[i-2])
    
    print(max(dp1[N-1],dp2[N-1]))

T = int(input())

for i in range(T):
    dp()