arry = [0,1,2,4]

for i in range(4,12):
    new = arry[i-1] + arry[i-2] + arry[i-3]
    arry.append(new)

n = int(input())

for i in range(n):
    k = int(input())
    print(arry[k])