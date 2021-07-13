def accum(s):
    cont = 0
    cont_letras_maiusculas = iteracoes = 0
    palavra = ''
    for letra in s:
        iteracoes += 1
        if letra.islower() or letra.isupper():
            if iteracoes == 1:
                palavra += letra.upper()
            else:
                palavra += '-' + letra.upper()
                cont_letras_maiusculas += 1
        if cont_letras_maiusculas == 1:
            cont += 1
            palavra += letra.lower() * cont
            cont_letras_maiusculas = 0

    return palavra


print(accum("ZpglnRxqenU"))
