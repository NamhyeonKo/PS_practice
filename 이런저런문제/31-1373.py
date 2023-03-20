n = list(input().rstrip())

l = len(n)
res = ''

while n:
    sum = 0
    for i in range(3):
        if n:
            k = n.pop()
            if k == '1':
                sum += 2**i
    res += str(sum)

print(res[::-1])