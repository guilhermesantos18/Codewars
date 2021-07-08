def solution(string, ending):
    if string == ending or ending == '' or ending[1:] in string:
        return True
    else:
        return False
    # for pos in range(0, len(ending)):
    #     if ending[pos] == string[pos]:
    #         return True
    #     else:
    #         return False
