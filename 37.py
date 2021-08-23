def dashatize(n):
    n = str(n)
    lista_num = []
    cont_num_pares = 0
    for num in range(len(n)):
        if int(n[num]) % 2 == 0:
            num_pares = n[num]
            if num != len(n) - 1:
                if int(n[num + 1]) % 2 == 0:
                    cont_num_pares += 1
                    num_pares += n[num + 1]
                    lista_num.append(num_pares)
                elif cont_num_pares == 0:
                    lista_num.append(num_pares)
            elif int(n[num]) % 2 == 0:
                lista_num.append(num_pares)
            print(lista_num)
        else:
            lista_num.append(n[num])
    return '-'.join(lista_num)


print(dashatize(274))
