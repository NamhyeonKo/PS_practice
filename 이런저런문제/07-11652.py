# pypy로는 통과
# python으로는 통과 못함...
import sys

N = int(sys.stdin.readline())

num = []
cnt = []

for i in range(N):
    k = int(sys.stdin.readline())

    if k in num:
        cnt[num.index(k)] += 1
    else:
        num.append(k)
        cnt.append(1)

max_cnt = max(cnt)
num2 = []

for i in range(len(num)):
    if cnt[i] == max_cnt:
        num2.append(num[i])

num2.sort()

print(num2[0])