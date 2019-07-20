def my_filter(function,lst):
    """
        Python code to demonstrate naive method to compute filter
    """
    return list(x for x in lst if function(x))