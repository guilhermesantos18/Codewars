def solution(s):
    lista_pos_maiuscula = []
    lista_palavras = []
    pos_maiuscula = 0
    for letra in s:
        if letra.isupper():
            lista_pos_maiuscula.append(s.index(letra))
    for i in lista_pos_maiuscula:
        lista_palavras.append(s[:i])
        lista_palavras.append(s[i:])
    print(' '.join(lista_palavras))


solution('helloWorld')
