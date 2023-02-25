s = input()
l = len(s)

for i in range(l):
    print(s[i], end='')
    if i % 10 == 9:
        print()