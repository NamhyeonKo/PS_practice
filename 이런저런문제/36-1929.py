import sys

M, N = map(int,sys.stdin.readline().split())

isprime = [1] * (N + 1)
isprime[1] = 0 # 1은 소수가 아니므로..

# 에라토스테네스의 체 -> 배수인 애들을 그냥 0으로 채워넣음
for i in range(2,N+1):
    if isprime[i] == 1:
        k = 2
        while i*k <= N:
            isprime[i*k] = 0
            k += 1

for i in range(M,N+1):
    if isprime[i] == 1:
        print(i)