def array_diff(a, b):
    lista = []
    if a and b:
        for num in a:
            if num in b:
                continue
            else:
                lista.append(num)
    else:
        return '[]'
    return lista


print(array_diff([1, 2, 3], [1, 2]))
