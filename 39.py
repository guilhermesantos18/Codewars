def getCount(sentence):
    cont_vogais = 0
    for letra in sentence:
        if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
            cont_vogais += 1
    return cont_vogais


print(getCount('abracadabra'))
