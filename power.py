def my_pow(n, m):
    a = n
    if a == 0:
        return 1
    for x in range(abs(m - 1)):
        a *= n
        if a < 0:
            return 1 / a
    return a
