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
    if strng.isalpha():
        letras = ''.join(lista_letra)
        return letras + '1'
    elif strng.isalnum() or strng.isprintable() and not strng == '':
        num = int(''.join(lista_numeros))
        if num == 0:
            num = int(''.join(lista_numeros)) + 1
            num = str(num).zfill(cont_0)
        else:
            num = int(''.join(lista_numeros)) + 1
            num = str(num).zfill(cont_0 + 1)
        letras = ''.join(lista_letra)
        return letras + num
    else:
        return '1'


print(increment_string(''))
