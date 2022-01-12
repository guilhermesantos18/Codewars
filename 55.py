def increment_string(strng):
    comprimento = len(strng)
    lista_index = []
    lista_numeros = []
    cont_0 = 0
    if strng.isalpha():
        return strng + '1'
    elif strng.isalnum():
        for l in strng:
            if l.isnumeric():
                lista_numeros.append(l)
                if l == '0':
                    cont_0 += 1
        num = ''.join(lista_numeros)
        strng = strng.replace(num, '')
        if num == '00':
            num = int(''.join(lista_numeros)) + 1
            num = str(num).zfill(cont_0)
        else:
            num = int(''.join(lista_numeros)) + 1
            num = str(num).zfill(comprimento)
        return strng + num
    elif strng == '':
        return '1'
    elif strng.isprintable():
        for index, letra in enumerate(strng):
            if str(letra).isalpha():
                lista_index.append(index)
    number = strng[lista_index[-1] + 1:]
    for i in number:
        if i in '!"@#£$§%&/{([)]=}?*+^~_-.,;:<»>|':
            number = number.replace(i, '')
    strng = strng.replace(number, '')
    number = int(number) + 1
    return strng + str(number)


print(increment_string(''))
