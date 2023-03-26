N ,M = map(int,input().split())

cnt = [0,0]

# 고등학교 때 쓴 기술 사용 -> 조합은 계산식이 더 편하게 작은수로 치환 가능
if M > int(N/2):
    M = N - M

# 조합 계산 식의 분자
for i in range(N+1-M,N+1):
    s = i
    while True:
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

# 조합 계산 식의 분모
for i in range(2,M+1):
    s = i
    while s > 1:
        if s % 10 == 0:
            s //= 10
            cnt[0] -= 1
            cnt[1] -= 1
        elif s % 2 == 0:
            s //= 2
            cnt[0] -= 1
        elif s % 5 == 0:
            s //= 5
            cnt[1] -= 1
        else:
            break

print(min(cnt))