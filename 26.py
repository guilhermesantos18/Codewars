def ip_to_int32(ip):
    cont = 0
    binary = '...'
    binary = binary.split('.')
    ip = ip.split('.')
    for num in ip:
        binary[cont] += bin(int(num))[2:].zfill(8)
        cont += 1
    binary = ''.join(binary)
    comprimento = len(binary) - 1
    cont = res = 0
    for i in binary:
        i = int(i)
        if i > 0:
            dec = 2 ** (comprimento - cont)
            cont += 1
            res += dec
        else:
            cont += 1
    return res

# def ip_to_int32(ip):
#     return int(''.join([(bin(int(x))[2:]).zfill(8) for x in ip.split('.')]), 2)
#
#
# print(ip_to_int32('128.32.10.1'))