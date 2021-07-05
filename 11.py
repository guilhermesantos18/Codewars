def likes(nomes):
    if len(nomes) == 1:
        return f'{nomes[0]} likes this'
    elif len(nomes) == 2:
        return f'{nomes[0]} and {nomes[1]} like this'
    elif len(nomes) == 3:
        return f'{nomes[0]}, {nomes[1]} and {nomes[2]} like this'
    elif len(nomes) >= 4:
        return f'{nomes[0]}, {nomes[1]} and {len(nomes) - 2} others like this'
    else:
        return 'no one likes this'


print(likes(['Alex', 'Jacob', 'Mark', 'Max']))
