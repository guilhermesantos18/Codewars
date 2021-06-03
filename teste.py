frase = str(input('Digite uma frase: '))
if 'a' or 'a'.upper() in frase:
    frase = frase.replace('a'.upper() or 'a', '')
print(frase)
