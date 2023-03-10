import sys

n = int(input())
num = list(map(int,sys.stdin.readline().split()))
sum_n = [0] * n
sum_n[0] = num[0]

# 이제까지 더한 연속 값이 자기 자신보다 작으면 거기까지가 최대이므로 자기 자신부터 시작
for i in range(1,n):
    sum_n[i] = max(sum_n[i-1] + num[i],num[i])

print(max(sum_n))
