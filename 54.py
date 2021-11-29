def unique_in_order(iterable):
    lista_letra_nao_repetidas = []
    if iterable:
        for pos, letra in enumerate(iterable):
            print(pos)
            print(letra)
            if pos == len(iterable) - 1:
                break
            if iterable[pos + 1] != letra:
                lista_letra_nao_repetidas.append(letra)
        lista_letra_nao_repetidas.append(iterable[len(iterable) - 1])
        return lista_letra_nao_repetidas
    else:
        return lista_letra_nao_repetidas


unique_in_order('AAAABBBCCDAABBB')