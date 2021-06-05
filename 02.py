array1 = [True,  True,  True,  False,
          True,  True,  True,  True,
          True,  False, True,  False,
          True,  False, False, True,
          True,  True,  True,  True,
          False, False, True, True]


def count_sheeps(sheep):
    cont_True = 0
    for boolean in array1:
        if boolean:
            cont_True += 1
    print(cont_True)


count_sheeps(array1)
