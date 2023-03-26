import sys

A, B = map(int,sys.stdin.readline().split())

l = int(sys.stdin.readline())

num = 0
k = list(map(int,sys.stdin.readline().split()))

for i in range(l):
    num += k[i] * (A**(l-i-1))

s = 1
cnt = 0

while s <= num:
    s *= B
    cnt += 1
s //= B

for i in range(cnt):
    mok = num // s
    num %= s
    s //= B
    print(mok,end=' ')