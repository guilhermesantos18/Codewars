def decipher_this(string):
    string = string.split(' ')
    for palavra in string:
        if palavra.isdigit():
            chr(int(palavra))


decipher_this('65 119esi 111dl 111lw 108dvei 105n 97n 111ka')
