num = '1234567890'
small = 'abcdefghijklmnopqrstuvwxyz'
big = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

while True:
    try:
        cnt_num = 0
        cnt_small = 0
        cnt_big = 0
        cnt_empty = 0
        string = input()
        for s in string:
            if s in num:
                cnt_num += 1
            elif s in small:
                cnt_small += 1
            elif s in big:
                cnt_big += 1
            elif s == ' ':
                cnt_empty += 1
        print(cnt_small, cnt_big, cnt_num, cnt_empty)
    except EOFError:
        break