word = input()
tail = []

for i in range(len(word)):
    tail.append(word[i:])

tail.sort()

for t in tail:
    print(t)