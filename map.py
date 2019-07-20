def my_map(function, lst):
    """
        Python code to demonstrate naive method to compute map
    """
    return list(function(x) for x in lst)
