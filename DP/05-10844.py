MOD = 10**9
N = int(input())

# 시작 숫자마다 각 경우를 저장할 배열 생성
arr = [[0]*10 for i in range(N+1)]
arr[1] = [0,1,1,1,1,1,1,1,1,1]

for i in range(2,N+1):
    for j in range(10):
        # 0인 경우는 무조건 뒤에 1이 붙으니 1인 경우 더하기
        if j == 0:
            arr[i][j] = arr[i-1][j+1]
        # 9인 경우는 무조건 뒤에 8이 붙으니 8인 경우 더하기
        elif j == 9:
            arr[i][j] = arr[i-1][j-1]
        # 나머지 경우는 j-1과 j+1 경우 둘 다 될 수 있으니 두 경우 더하기
        else:
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j+1]

print(sum(arr[N]) % MOD)
