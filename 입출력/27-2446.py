n = int(input())

for i in range(1,n):
    for j in range(1,i):
        print(" ",end='')
    for j in range(2*(n-i)+1):
        print("*",end='')
    print()

for i in range(1,n):
    print(" ",end='')
print("*")

for i in range(1,n):
    for j in range(n-i-1):
        print(" ",end='')
    for j in range(2*(i)+1):
        print("*",end='')
    print()