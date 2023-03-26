import sys

N = int(sys.stdin.readline())
NUM = list(map(int,sys.stdin.readline().split()))

cnt = 0

for i in range(N):
    if NUM[i] == 1:
        cnt += 1
        continue
    for j in range(2,NUM[i]):
        if NUM[i] % j == 0:
            cnt += 1
            break

print(N - cnt)