def sum_pairs(ints, s):
    soma = cont = cont_pos = num2 = num1 = ultimo_index = 0
    lista_nums = []
    lista_cont_pos = []
    lista_nums2 = []
    ultimo_index = len(ints) - 1
    while True:
        cont_pos += 1
        soma = ints[cont] + ints[cont_pos]
        if soma == s:
            lista_cont_pos.append(cont_pos)
            lista_nums.append(ints[cont])
            lista_nums.append(ints[cont_pos])
        if cont_pos == ultimo_index:
            cont += 1
            cont_pos = cont
        if cont == ultimo_index:
            break
        if IndexError:
            return None
    num2 = ints[min(lista_cont_pos)]
    for num in lista_nums:
        soma = num + num2
        if soma == s:
            lista_nums2.append(num)
            lista_nums2.append(num2)
            break
    return lista_nums2


print(sum_pairs([0, 0, -2, 3], 2))
