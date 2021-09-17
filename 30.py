def decipher_this(string):
    string = string.split(' ')
    num = ''
    for palavra in string:
        if palavra.isdigit():
            chr(int(palavra))
        elif palavra.isalnum():
            for letra in palavra:
                if letra.isnumeric():
                    num += letra
            num = ''


decipher_this('65 119esi 111dl 111lw 108dvei 105n 97n 111ka')
