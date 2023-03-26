import sys
MAX = 1000000

isprime = [True] * (MAX + 1)
isprime[0], isprime[1] = False, False # 1은 소수가 아니므로..

# 에라토스테네스의 체 -> 배수인 애들을 그냥 0으로 채워넣음
for i in range(2,MAX + 1):
    if isprime[i]:
        k = i*i
        while k <= MAX:
            isprime[k] = False
            k += i

while True:
    n = int(sys.stdin.readline())

    if n == 0:
        break

    for i in range(3,(n//2)+1,2):   # 이 반복문이 함정인데, 어차피 홀수만 판단하므로 3부터 2씩 더하면 반복문을 2배 빨리 돌릴 수 있다.
        if isprime[i] and isprime[n-i]:
            print('%d = %d + %d' % (n,i,n-i))
            break