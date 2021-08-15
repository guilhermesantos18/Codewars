def decipher_this(string):
    string = string.split(' ')
    print(string)
    lista_num = list(filter(lambda numero: numero.isalnum(), string))
    print(lista_num)


decipher_this('65 119esi 111dl 111lw 108dvei 105n 97n 111ka')
