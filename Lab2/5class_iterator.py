"""
Написать на основе 4Return.py классы итераторы
"""

class Iterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        else:
            self.index += 1
            return self.data[self.index-1]