global arry
arry = [0] * 1000001
arry[2] = 1
arry[3] = 1

def rec_dp(n):
    global arry
    # n이 이미 DP 배열에 존재하는 경우
    if arry[n] != 0:
        return arry[n]
    
    # n이 DP 배열에 존재하지 않는 경우
    # 3가지 경우로 나누고 그 중에 min 값을 DP 배열에 저장후 반환
    min = 1000000
    if n % 3 == 0:
        if rec_dp(n//3) + 1 < min:
            min = rec_dp(n//3) + 1
    if n % 2 == 0:
        if rec_dp(n//2) + 1 < min:
            min = rec_dp(n//2) + 1
    if rec_dp(n-1) + 1 < min:
        min = rec_dp(n-1) + 1
    
    arry[n] = min
    return min

k = int(input())
res = rec_dp(k)
# for i in range(k+1):
#     print(i, arry[i])
print(res)