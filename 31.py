def solution(s):
    lista_pos_maiuscula = []
    lista_palavras = []
    for letra in range(len(s)):
        if s[letra].isupper():
            lista_pos_maiuscula.append(letra)
    for i in range(len(lista_pos_maiuscula)):
        if i == 0:
            lista_palavras.append(s[:lista_pos_maiuscula[i]])
        if i < len(lista_pos_maiuscula) - 2:
            lista_palavras.append(s[lista_pos_maiuscula[i]:lista_pos_maiuscula[i+1]])
        elif i == len(lista_pos_maiuscula) - 2:
            lista_palavras.append(s[lista_pos_maiuscula[i]:lista_pos_maiuscula[-1]])
        elif i == len(lista_pos_maiuscula) - 1:
            lista_palavras.append(s[lista_pos_maiuscula[i]:])
    return ' '.join(lista_palavras)


print(solution('usePointPublicThinkGreat'))
