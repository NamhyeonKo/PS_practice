NUM = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

n, b = map(int,input().split())

s = 0
res = ''

while b**s <= n:
    s += 1

for i in range(1,s+1):
    mok = n // (b**(s-i))
    n = n % (b**(s-i))
    res = res + NUM[mok]

print(res)