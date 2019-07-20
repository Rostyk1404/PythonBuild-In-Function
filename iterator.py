"""
    Python code to demonstrate naive method to compute iterator
"""


class Sup:
    def __init__(self, limit):
        self.limit = limit


class Myiterator(Sup):
    def __init__(self, limit, values):
        Sup.__init__(self, limit)
        self.values = values

    def __iter__(self):
        return self

    def __next__(self):
        if self.values >= self.limit:
            self.limit += 1
            return self.limit
        else:
            raise StopIteration
