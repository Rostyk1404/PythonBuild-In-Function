def my_range(start: int, end: int = None, step: int = None):
    """
        Python code to demonstrate naive method to compute range
    """
    if step is None:
        step = 1
    if end is None:
        start = 0
        end = start
    if type(end) != int or type(start) != int or type(step) != int:
        raise TypeError('Please enter a correct type !!!')
    while True:
        if start < end:
            yield start
            start += step
        elif start > end:
            yield start
            start -= step
