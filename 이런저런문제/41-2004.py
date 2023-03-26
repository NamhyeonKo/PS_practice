# 이런 미친 방법이 있는지는 몰랐다...
# 간단히 설명하면 N!에 어떤 수가 몇 번 포함 되어 있는지 알고 싶으면
# 그 수의 거듭제곱으로 몫으로 나눠보면 나온다. 아래글 참고!
# https://www.acmicpc.net/board/view/72777
def find_cnt_two(N):
    s = 1
    cnt = 0
    while (2**s) <= N:
        cnt += N // (2**s)
        s += 1
    return cnt

def find_cnt_five(N):
    s = 1
    cnt = 0
    while (5**s) <= N:
        cnt += N // (5**s)
        s += 1
    return cnt

N, M = map(int,input().split())

cnt = []

cnt.append(find_cnt_two(N)-find_cnt_two(M)-find_cnt_two(N-M))
cnt.append(find_cnt_five(N)-find_cnt_five(M)-find_cnt_five(N-M))

print(min(cnt))