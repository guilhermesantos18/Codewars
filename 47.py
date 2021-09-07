def duplicate_count(text):
    text = text.upper()
    cont = 0
    list_cont_letras = []
    list_letras = []
    for letra in text:
        list_cont_letras.append(text.count(letra))
    for num in range(len(list_cont_letras)):
        if list_cont_letras[num] >= 2:
            if text[num] not in list_letras:
                list_letras.append(text[num])
                cont += 1
    return cont


print(duplicate_count("Indivisibilities"))
