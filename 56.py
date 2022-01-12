def sum_pairs(ints, s):
    soma = cont = cont_pos = ultimo_index = 0
    lista_nums = []
    ultimo_index = len(ints) - 1
    while True:
        cont_pos += 1
        soma = ints[cont] + ints[cont_pos]
        if soma == s:
            lista_nums.append(ints[cont])
            lista_nums.append(ints[cont_pos])
        if cont_pos == ultimo_index:
            cont += 1
            cont_pos = cont




print(sum_pairs([10, 5, 2, 3, 7, 5], 10))
