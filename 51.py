def pig_it(text):
    text = text.split()
    lista_palavras = []
    flag = False
    pontos = ''
    for palavra in text:
        if palavra == '?' or palavra == '!':
            pontos = palavra
            flag = True
            break
        primeira_letra = palavra[0]
        palavra = palavra.replace(palavra[0], '', 1)
        palavra += primeira_letra
        palavra += 'ay'
        lista_palavras.append(palavra)
    if flag:
        return ' '.join(lista_palavras) + f' {pontos}'
    else:
        return ' '.join(lista_palavras)


print(pig_it('igPay atinlay siay oolcay'))
