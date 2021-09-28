def multiplication_table(size):
    lista = []
    index = 0
    multiplicacao = 1
    for mini_lista in range(size):
        lista.append([])
    for pos in range(size):
        for num in range(1, size+1):
            if index == 0:
                lista[index].append(num)
            elif index > 0:
                lista[index].append(num * multiplicacao)
            if len(lista[index]) == size:
                index += 1
                multiplicacao += 1
    return lista


print(multiplication_table(10))
