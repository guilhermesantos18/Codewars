def spin_words(sentence):
    lista_palavras = []
    for palavra in sentence.split():
        cont_letras = 0
        for letra in palavra:
            cont_letras += 1
        if cont_letras >= 5:
            lista_palavras.append(palavra[::-1])
        else:
            lista_palavras.append(palavra)
    return ' '.join(lista_palavras)
