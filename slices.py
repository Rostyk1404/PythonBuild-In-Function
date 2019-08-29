c = [1, 2, 3, 4, 5, 6, 7, 99, 7, 867, 654]


def my_slices(my_list, start: int = None, stop: int = None, step: int = None):
    """
        Python code to demonstrate naive method to compute slices
    """
    if step is None:
        step = 1

    if start is None or stop is None:
        return my_list[start]
    else:
        return my_list[start:stop:step]
