arry = [0,1,2,4]

for i in range(4,12):
    # 정수 1,2,3의 합을 나타내는 경우 이므로
    # i-1에서 1을 더하는 경우
    # i-2에서 2를 더하는 경우
    # i-3에서 3을 더하는 경우 세가지로 나눌 수 있고 이걸 다 더하면 됨
    new = arry[i-1] + arry[i-2] + arry[i-3]
    arry.append(new)

n = int(input())

for i in range(n):
    k = int(input())
    print(arry[k])