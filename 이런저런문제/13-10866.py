from collections import deque
import sys

N = int(input())

num = deque()

for i in range(N):
    OPPEREND = sys.stdin.readline()

    if 'push_front' in OPPEREND:
        k = OPPEREND.split()
        num.appendleft(k[1])
    elif 'push_back' in OPPEREND:
        k = OPPEREND.split()
        num.append(k[1])
    elif 'pop_front' in OPPEREND:
        try:
            print(num.popleft())
        except:
            print(-1)
    elif 'pop_back' in OPPEREND:
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
    elif 'front' in OPPEREND:
        try:
            print(num[0])
        except:
            print(-1)
    elif 'back' in OPPEREND:
        try:
            print(num[-1])
        except:
            print(-1)