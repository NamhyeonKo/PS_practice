string = input()

cnt = [0] * 26

for s in string:
    cnt[ord(s)-97] += 1

for i in range(26):
    print(cnt[i], end=' ')