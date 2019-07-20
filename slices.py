def my_slices(my_list, start: int = None, end: int = None, step: int = None):
    """
        Python code to demonstrate naive method to compute slices
    """
    a = []
    if step == None:
        step = 1

    if start == None or end == None:
        return my_list[start]

    for x in range(start, end, step):
        a.append(my_list[x])

    return a
