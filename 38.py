def count_smileys(arr):
    caras_felizes = 0
    for cara in arr:
        for i in cara:
            if i == ')' or i == 'D':
                caras_felizes += 1
    return caras_felizes


print(count_smileys([';]', ':[', ';*', ':$', ';-D', ';]', ':[', ';*', ':$', ';-D']))
