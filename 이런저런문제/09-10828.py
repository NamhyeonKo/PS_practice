from collections import deque
import sys

N = int(input())

num = deque()

for i in range(N):
    OPPEREND = sys.stdin.readline()

    if 'push' in OPPEREND:
        k = OPPEREND.split()
        num.append(k[1])
    elif 'pop' in OPPEREND:
        try:
            print(num.pop())
        except:
            print(-1)
    elif 'size' in OPPEREND:
        print(len(num))
    elif 'empty' in OPPEREND:
        if len(num) == 0:
            print(1)
        else:
            print(0)
    elif 'top' in OPPEREND:
        try:
            print(num[-1])
        except:
            print(-1)