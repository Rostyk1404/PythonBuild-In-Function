def my_pow(number: int, m: int, z: int = None):
    """
        Python code to demonstrate naive method to compute power
    """
    list_of_numbers = []
    if number < 0 and m < 0 and z is not None:
        raise ValueError
    for x in range(abs(m)):
        list_of_numbers.append(number)
    dumps = 1

    for y in list_of_numbers:
        dumps *= y
    if z:
        return dumps % z

    elif m < 0:
        return 1 / dumps
    return dumps


def my_pow_using_exception(number: int, m: int, z: int = None):
    """
        Python code to demonstrate naive method to compute power using exception
    """
    try:
        if number < 0 and m < 0 and z is not None:
            raise ValueError
        list_of_numbers = []
        for x in range(abs(m)):
            list_of_numbers.append(number)
        dumps = 1

        for y in list_of_numbers:
            dumps *= y
        if z:
            return dumps % z

        elif m < 0:
            return 1 / dumps
        return dumps
    except ValueError:
        return "pow() 2nd argument cannot be negative when 3rd argument specified"


print(my_pow_using_exception(-2, -2, 5))
