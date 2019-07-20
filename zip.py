"""
    Python code to demonstrate naive method to compute zip
"""


def my_zip(lst1, lst2):
    new_list = []
    for x in range(0, len(lst1)):
        new_list.append((lst1[x], lst2[x]))
    return new_list


def my_zip2(lst1, lst2):
    return list(map(lambda x, y: (x, y), lst1, lst2))


def my_zip3(lst1, lst2):
    return list((lst1[x], lst2[x]) for x in range(0, len(lst1)))
