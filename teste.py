frase = 'Ola tudo bem'
vogais = 'aeiouAOE'
for pos in range(0, len(vogais)):
    frase = frase.replace(vogais[pos], '')
    print(frase)
print(frase)
