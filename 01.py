def disemvowel(string_):
    cont_a = cont_e = cont_i = cont_o = 0
    frase_sem_a = frase_sem_e = frase_sem_i = frase_sem_o = frase_sem_u = ''
    entrou_a = entrou_e = entrou_i = entrou_o = False
    if 'a' in string_:
        entrou_a = True
        cont_a += 1
        frase_sem_a = string_.replace('a', '')
    if 'e' in string_:
        entrou_e = True
        cont_e += 1
        if entrou_a:
            frase_sem_e = frase_sem_a.replace('e', '')
    if 'i' in string_:
        entrou_i = True
        cont_i += 1
        if entrou_a:
            frase_sem_i = frase_sem_a.replace('i', '')
        if entrou_e:
            frase_sem_i = frase_sem_e.replace('i', '')
        if entrou_a and entrou_e:
            frase_sem_i = frase_sem_e.replace('i', '')
    if 'o' in string_:
        entrou_o = True
        cont_o += 1
        if entrou_a:
            frase_sem_o = frase_sem_a.replace('o', '')
        if entrou_a and entrou_e:
            frase_sem_o = frase_sem_e.replace('o', '')
        if entrou_a and entrou_e and entrou_i:
            frase_sem_o = frase_sem_i.replace('o', '')
    # if 'u' in string_:
    if cont_a == 1 and cont_e == 1 and cont_i == 1 and cont_o == 1:
        print(frase_sem_o)


disemvowel(input('Digite uma frase: '))
