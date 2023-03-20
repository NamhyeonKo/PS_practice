# gcd 알고리즘 중 유명한 유클리드를 사용해야 시간 초과 발생 x

def uclid_gcd(a,b):
    if a < b:
        a,b = b,a
    
    while b != 0:
        n = a % b
        a = b
        b = n
    return a

T = int(input())

for i in range(T):
    a,b = map(int,input().split())
    gcd = uclid_gcd(a,b)
    lcm = (a // gcd) * b
    print(lcm)