def move_zeros(array):
    for num in array:
        if num == 0:
            array.remove(num)
            array.append(0)
    return array


move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1])
