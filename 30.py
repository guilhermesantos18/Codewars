def encrypt_this(string):
    string = string.split(' ')
    num = ''
    lista_palavras = []
    comprimento_numero = 0
    for palavra in string:
        if palavra.isdigit():
            lista_palavras.append(chr(int(palavra)))
        elif palavra.isalnum():
            for letra in palavra:
                if letra.isnumeric():
                    num += letra
                    comprimento_numero = len(num)
            if num in palavra:
                palavra = palavra.replace(palavra[0:comprimento_numero], chr(int(num)))
                ultima_letra = palavra[-1]
                palavra = palavra.replace(palavra[-1], palavra[1])
                palavra = palavra.replace(palavra[1], ultima_letra, 1)
                lista_palavras.append(palavra)
            num = ''
    return ' '.join(lista_palavras)


print(encrypt_this('84kanh 121uo 80roti 102ro 97ll 121ruo 104ple'))
