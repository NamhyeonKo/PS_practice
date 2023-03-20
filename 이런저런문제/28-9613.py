import sys

def gcd(a,b):
    while b > 0:
        a,b = b,a%b
    return a

t = int(sys.stdin.readline())

for i in range(t):
    num = list(map(int, sys.stdin.readline().split()))
    n = num[0]
    gcd_sum = 0
    for j in range(1,n):
        for k in range(j+1,n+1):
            gcd_sum += gcd(num[j], num[k])
    print(gcd_sum)