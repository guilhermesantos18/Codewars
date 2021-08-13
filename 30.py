def decipher_this(string):
    for letra in string:
        if letra.isnumeric():
            print(chr(letra))


decipher_this('65 119esi 111dl 111lw 108dvei 105n 97n 111ka')