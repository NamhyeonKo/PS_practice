# 왼괄호가 오른쪽 괄호보다 적어지는 순간부터 깨지는거에 초첨을 맞췄다.
N = int(input())

for i in range(N):
    s = input()
    left = 0
    right = 0
    flag = 0
    for j in s:
        if j == '(':
            left += 1
        else:
            right += 1
        if left < right:
            flag = 1
            break
    if (flag == 0) & (left == right):
        print('YES')
    else:
        print('NO')