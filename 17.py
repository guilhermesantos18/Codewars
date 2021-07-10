def longest_consec(strarr, k):
    if k > 1:
        passo = k - 1
    else:
        passo = k
    lista_palavras_juntas = []
    if not strarr or k > len(strarr) or k <= 0:
        return ''
    for palavra in range(0, len(strarr)):
        if passo == len(strarr):
            break
        if k >= 2:
            lista_palavras_juntas.append(strarr[palavra] + strarr[passo])
            passo += 1
        else:
            lista_palavras_juntas.append(strarr[palavra])


print(longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1))
