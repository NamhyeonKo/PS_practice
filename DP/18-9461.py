dp = [1,1,1,2,2,3,4,5,7,9]

T = int(input())

for i in range(T):
    N = int(input())
    
    # 규칙을 찾으면 5번째 전과 1번째 전의 변이 겹침
    # dp 배열의 길이부터 시작해서 시간을 줄임 (앞에서 구한 경우는 다시 구하지 않게)
    for j in range(len(dp),N):
        dp.append(dp[j-5]+dp[j-1])
    
    print(dp[N-1])