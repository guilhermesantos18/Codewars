def multiplication_table(row, col):
    lista = []
    cont = 1
    cont_pos = 0
    mult = 2
    for i in range(row):
        lista.append([] * i)
    for pos in range(1, col * row + 1):
        if pos <= col:
            lista[0].append(pos)
        if row >= 2:
            if len(lista[0]) == col:
                lista[cont].append(lista[0][cont_pos]*mult)
                cont_pos += 1
                if col == len(lista[cont]):
                    cont += 1
                    cont_pos = 0
                    mult += 1
                if len(lista[row-1]) == col:
                    break
    return lista


print(multiplication_table(1, 108))
