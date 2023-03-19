string = input()
index = [0] * 26

for i in range(26):
    try:
        print(string.index(chr(i+97)),end=' ')
    except:
        print(-1,end=' ')