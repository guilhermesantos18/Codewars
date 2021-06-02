def disemvowel(string_):
    frase_sem_a = frase_sem_e = frase_sem_i = frase_sem_o = frase_sem_u = ''
    entrou_a = entrou_e = False
    if 'a' in string_:
        frase_sem_a = string_.replace('a', '')
        entrou_a = True
    if 'e' in string_:
        frase_sem_e = string_.replace('e', '')
        entrou_e = True
        if entrou_a:
            frase_sem_e = frase_sem_a.replace('e', '')
    if 'i' in string_:
        if entrou_a:
            frase_sem_i = frase_sem_a.replace('i', '')
        if entrou_e:
            frase_sem_i = frase_sem_e.replace('i', '')
        if entrou_a and entrou_e:
            frase_sem_i = frase_sem_e.replace('i', '')
    # if 'o' in string_:
    # if 'u' in string_:
    print(frase_sem_i)


disemvowel(input('Digite uma frase: '))
