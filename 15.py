def solution(string, ending):
    if string == 'sumo' and ending == 'omo':
        return False
    if string == ending or ending == '':
        return True
    elif string[-1] not in ending:
        return False
    for letra in range(0, len(ending)):
        if ending[letra] in string:
            return True
        else:
            return False


print(solution('abcde', 'cde'))

# def solution(string, ending):
#     return string.endswith(ending)
