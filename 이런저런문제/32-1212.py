# # 뒤집을거라 뒤집어서 저장
# eighttotwo = ['000','100','010','110','001','101','011','111']

# n = int(input())
# res = ''

# while n:
#     k = n % 10
#     n = n // 10
#     res += eighttotwo[k]

# print(res[::-1].lstrip('0'))

print(bin(int(input(),8))[2:])