num = '1234567890'
small = 'abcdefghijklmnopqrstuvwxyz'
big = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

str1 = input()
str2 = ''

for s in str1:
    if (s in num) | (s == ' '):
        str2 += s
    elif s in small:
        str2 += chr(((ord(s)- 97 + 13) % 26) + 97)
    elif s in big:
        str2 += chr(((ord(s)- 65 + 13) % 26) + 65)

print(str2)