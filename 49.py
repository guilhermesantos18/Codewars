def sortme(words):
    lista_ordenada = []
    abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                  's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for letra in abecedario:
        for palavra in words:
            if letra.upper() in palavra[0] or letra in palavra[0]:
                lista_ordenada.append(palavra)
    return lista_ordenada


print(sortme(["Hello", "there", "I'm", "fine"]))
