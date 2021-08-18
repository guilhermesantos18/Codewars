def positive_sum(arr):
    soma = 0
    if not arr:
        return 0
    for num in arr:
        if num > 0:
            soma += num
    return soma


print(positive_sum([1,2,3,4,5]))
