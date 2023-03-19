# deque를 이용하여 반복문으로 계속 돌리다가 횟수가 나눠 떨어질 때 없애는 식으로 짬
from collections import deque

N, K = map(int,input().split())

num = deque()
res = []

for i in range(N):
    num.append(i+1)

cnt = 1
print('<',end='')
while len(num) != 0:
    if cnt % K != 0:
        num.append(num.popleft())
    elif len(num) != 1:
        print(num.popleft(),end=', ')
    else:
        print(num.popleft(),end=">")
    cnt += 1