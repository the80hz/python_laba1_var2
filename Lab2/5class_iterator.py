"""
Написать на основе next() класс итератора
"""
from Return import next


class IteratorData:
    def __init__(self, _data, filename):
        self.data = _data
        self.index = 0
        self.filename = filename

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < self.data:
            result = next(self.filename)
            self.index += 1
            return result
        else:
            raise StopIteration


if __name__ == '__main__':
    data = IteratorData(5, 'data/dataset.csv')
    for i in data:
        print(i)
