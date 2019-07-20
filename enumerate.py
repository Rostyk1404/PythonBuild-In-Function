def my_enumerate(lst):
    """
        Python code to demonstrate naive method to compute enumerate
    """
    return list((x, lst[x]) for x in range(len(lst)))
