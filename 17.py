def longest_consec(strarr, k):
    cont = 0
    if k > 1:
        passo = k - 1
    else:
        passo = k
    lista_palavras_juntas = []
    lista_comprimento_palavras = []
    if not strarr or k > len(strarr) or k <= 0:
        return ''
    for i in range(0, len(strarr)):
        if passo == len(strarr):
            break
        if k >= 2:
            lista_palavras_juntas.append(str(''.join(strarr[i:passo+1])))
            passo += 1
        else:
            lista_palavras_juntas.append(strarr[i])
    for palavra in lista_palavras_juntas:
        print(palavra)
        for letra in palavra:
            cont += 1
            if cont == len(palavra):
                lista_comprimento_palavras.append(cont)
                cont = 0
    max(lista_comprimento_palavras)


print(longest_consec(["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"], 1))
