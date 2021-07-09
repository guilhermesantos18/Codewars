def is_square(n):
    for i in range(n-1, 1, -1):
        if i * i == n:
            return True
    else:
        return False
