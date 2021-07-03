def square_digits(num):
    numero = ''
    for i in str(num):
        i = int(i) ** 2
        numero = numero.__add__(str(i))
    return int(numero)


print(square_digits(9119))

# def square_digits(num):
#     num = str(num)
#     ans = ''
#     for i in num:
#         ans += str(int(i)**2)
#     return int(ans)
#
#
# print(square_digits(9119))
