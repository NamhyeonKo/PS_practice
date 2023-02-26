def dp(n):
    # 피보나치 수열이랑 똑같은 연산이 됨
    arry = [0,1,2]
    for i in range(3,n+1):
        arry.append((arry[i-1] + arry[i-2]) % 10007)
    return arry[n]

k = int(input())
print(dp(k))