def increment_string(strng):
    lista_letra = []
    lista_numeros = []
    cont_0 = 0
    for letra in strng:
        if letra.isnumeric():
            lista_numeros.append(letra)
            if letra == '0':
                cont_0 += 1
        else:
            lista_letra.append(letra)
    num = int(''.join(lista_numeros)) + 1
    print(str(num).zfill(4))


increment_string('foo001')