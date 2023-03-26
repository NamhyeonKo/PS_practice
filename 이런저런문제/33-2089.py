N = int(input())

res = ""

if N == 0:
    print('0')
    exit()

while N:
    if N % (-2):
        res = '1' + res
        N = N // (-2) + 1
    else:
        res = '0' + res
        N = N // (-2)

print(res)