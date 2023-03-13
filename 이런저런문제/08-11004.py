import sys

N, K = map(int,sys.stdin.readline().split())

num = list(map(int,sys.stdin.readline().split()))

num.sort()

print(num[K-1])