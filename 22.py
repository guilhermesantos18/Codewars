def filter_list(l):
    list_number = []
    for i in l:
        if type(i) == int:
            list_number.append(i)
    return list_number


print(filter_list([1, 2, 'aasf', '1', '123', 123]))
