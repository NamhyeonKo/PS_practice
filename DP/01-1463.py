def dp(k):
    arry = [0,0,1,1]

    # 반복문 돌리기
    # 3가지 경우로 나누고 그 중에 min 값을 DP 배열에 저장후 반환
    for n in range(4,k+1):
        min = 1000000
        if n % 3 == 0:
            if arry[n//3] + 1 < min:
                min = arry[n//3] + 1
        if n % 2 == 0:
            if arry[n//2] + 1 < min:
                min = arry[n//2] + 1
        if arry[n - 1] + 1 < min:
            min = arry[n - 1] + 1
        # min이 그 수가 가질 수 있는 최소 경우이므로 배열에 추가
        arry.append(min)
    return arry[k]

k = int(input())
res = dp(k)

print(res)