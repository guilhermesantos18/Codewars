def longest_consec(strarr, k):
    x = 0
    if not strarr or k > len(strarr) or k <= 0:
        return False
    for palavra in range(0, len(strarr), k):
        junto = strarr[palavra]


print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2))
