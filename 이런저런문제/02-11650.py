import sys

N = int(sys.stdin.readline())

point = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

point.sort(key=lambda x: (x[0],x[1]))

for i in range(N):
    print(point[i][0],point[i][1])