def ip_to_int32(ip):
    binary = ''
    ip = ip.split('.')
    for num in ip:
        binary += bin(int(num))
    binary = binary.replace('0b', '', )
    print(binary)
    # comprimento = len(binary) - 1
    # cont = res = 0
    # for i in binary:
    #     i = int(i)
    #     if i > 0:
    #         dec = 2 ** (comprimento - cont)
    #         cont += 1
    #         res += dec
    #     else:
    #         cont += 1
    # return res


print(ip_to_int32('128.32.10.1'))
