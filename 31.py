def solution(s):
    lista_pos_maiuscula = []
    lista_palavras = []
    cont_maiusculas = 0
    for letra in range(len(s)):
        if s[letra].isupper():
            lista_pos_maiuscula.append(letra)
    print(lista_pos_maiuscula)
    for i in lista_pos_maiuscula:
        if i == lista_pos_maiuscula[0]:
            lista_palavras.append(s[:i])
        elif i == lista_pos_maiuscula[-1]:
            lista_palavras.append(s[i:])
        else:
            # if i > lista_pos_maiuscula[0] and i < lista_pos_maiuscula[-2]:
            #     lista_palavras.append(s[i:])
            if i == lista_pos_maiuscula[1]:
                print(i)
                lista_palavras.append(s[lista_pos_maiuscula[0]:i])
            elif i == lista_pos_maiuscula[-2]:
                lista_palavras.append(s[i:lista_pos_maiuscula[-1]])
    print(lista_palavras)


solution('usePointPublicThinkGreat')
