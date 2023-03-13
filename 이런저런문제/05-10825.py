import sys

N = int(sys.stdin.readline())
user = []

for i in range(N):
    name, kor, eng, math = sys.stdin.readline().split()

    k = []
    k.append(name)
    k.append(int(kor))
    k.append(int(eng))
    k.append(int(math))
    user.append(k)

# -부호를 이용하면 역순 가능
user.sort(key=lambda x: (-x[1],x[2],-x[3],x[0]))

for i in range(N):
    print(user[i][0])