import sys

N = int(sys.stdin.readline())
user = []

for i in range(N):
    age, name = sys.stdin.readline().split()

    k = []
    k.append(int(age))
    k.append(name)
    user.append(k)

user.sort(key=lambda x: x[0])

for i in range(N):
    print(user[i][0],user[i][1])