def make_negative( number ):
    if number < 0:
        return number
    elif number > 0:
        return int(f'-{number}')
    else:
        return 0


print(make_negative(5))