# Decimal para binário

def add_binary(a, b):
    num_bin = bin(a+b)
    if num_bin[0:2] == '0b':
        num_bin = num_bin.replace(num_bin[0:2], '')
    return num_bin


print(add_binary(1, 1))
print(add_binary(0, 1))
print(add_binary(0, 1))
print(add_binary(2, 2))
print(add_binary(51, 12))
