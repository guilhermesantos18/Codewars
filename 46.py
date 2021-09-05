def digital_root(n):
    soma_num = 0
    n = str(n)
    while len(n) >= 2:
        for num in n:
            soma_num += int(num)
        n = str(soma_num)
        soma_num = 0
    return n


print(digital_root(132189))
