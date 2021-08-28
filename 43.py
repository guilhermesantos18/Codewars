def autocomplete(input_, dictionary):
    lista_palavras = []
    for palavra in dictionary:
        if input_ == palavra[0:len(input_)]:
            lista_palavras.append(palavra)
    return lista_palavras


dictionary = ['abnormal',
              'arm-wrestling',
              'absolute',
              'airplane',
              'airport',
              'amazing',
              'apple',
              'ball']

print(autocomplete('a', dictionary))
