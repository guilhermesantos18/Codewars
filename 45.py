def descending_order(num):
    lista_num = []
    for num in str(num):
        lista_num.append(num)
    return int(''.join(sorted(lista_num, reverse=True)))


print(descending_order(42145))
