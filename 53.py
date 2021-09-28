def string_transformer(s):
    s = s.split()
    lista_palavras = []
    palavras_maiusculas = ''
    palavras_minusculas = ''
    for palavra in s[::-1]:
        for letra in palavra:
            if letra.islower():
                palavras_maiusculas += letra.upper()
            elif letra.isupper():
                palavras_minusculas += letra.lower()
        lista_palavras.append(palavras_minusculas + palavras_maiusculas)
        palavras_maiusculas = ''
        palavras_minusculas = ''
    return ' '.join(lista_palavras)


print(string_transformer('You Know When  THAT  Hotline Bling'))
