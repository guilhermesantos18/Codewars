vogais = 'aeiouAOE'


def disemvowel(string_):
    for vogal in range(0, len(vogais)):
        string_ = string_.replace(vogais[vogal], '')
    return string_


print(disemvowel(input('Digite uma frase: ')))
