NUM = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

N, B = input().split()
B = int(B)

l = len(N) - 1
sum = 0
for i in N:
    sum += NUM.index(i) * (B**l)
    l -= 1

print(sum)
