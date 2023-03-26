N = int(input())

cnt = [0,0]

for i in range(1,N+1):
    s = i
    while s > 1:
        if s % 10 == 0:
            s //= 10
            cnt[0] += 1
            cnt[1] += 1
        elif s % 2 == 0:
            s //= 2
            cnt[0] += 1
        elif s % 5 == 0:
            s //= 5
            cnt[1] += 1
        else:
            break

print(min(cnt))