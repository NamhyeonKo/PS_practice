import sys

N = int(sys.stdin.readline())

cnt = [0] * 10001

for i in range(1,N+1):
    cnt[int(sys.stdin.readline())] += 1

for i in range(1,10001):
    for j in range(cnt[i]):
        print(i)