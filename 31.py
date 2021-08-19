def solution(s):
    lista_pos_maiuscula = []
    lista_palavras = []
    cont_maiusculas = 0
    for letra in range(len(s)):
        if s[letra].isupper():
            lista_pos_maiuscula.append(letra)
            cont_maiusculas += 1
    for i in lista_pos_maiuscula:
        # if cont_maiusculas == 1:
        #     if i == lista_pos_maiuscula[0]:
        #         lista_palavras.append(s[:i])
        #         lista_palavras.append(s[i:])
        # elif cont_maiusculas >= 1:
        #     if i == lista_pos_maiuscula[0]:
        #         lista_palavras.append(s[:i])
        #     elif i == lista_pos_maiuscula[-1]:
        #         lista_palavras.append(s[i:])
        #     else:
        lista_palavras.append(s[i:i+1])
    print(lista_palavras)
        # lista_palavras.append(s[:i])
        # lista_palavras.append(s[i:])


solution('breakCamelCase')
