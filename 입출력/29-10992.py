n = int(input())

for i in range(n - 1):
    # 맨 앞 공백 + 별 하나
    for j in range(n-i-1):
        print(" ",end='')
    print("*",end='')
    # 첫 째 줄일 끝나면 뒤에 작업 x, 자동으로 n==1 일때 경우도 가능(이 될줄 알았는데 안됨..)
    if i == 0:
        print()
        continue
    # 중간 공백 + 별 하나
    for j in range(2*i-1):
        print(" ",end='')
    print("*")

# 마지막 줄
if n != 1:
    for j in range(2*n-1):
        print("*",end='')
else:
    # n==1인 경우
    print('*')