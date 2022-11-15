import os
from return_4 import next


class IteratorData:
    """
    Класс итератора, который возвращает данные из файла.
    Параметр data - количество строк, которые необходимо вернуть.
    Параметр filename - имя файла, из которого необходимо считывать данные.
    """
    def __init__(self, _data: int, filename: str):
        self.data = _data
        self.index = 0
        self.filename = filename

    def __iter__(self):
        return self

    def __next__(self) -> str:
        if self.index < self.data:
            result = next(self.filename)
            self.index += 1
            return result
        else:
            os.remove(f'{self.filename}.temp')
            raise StopIteration


if __name__ == '__main__':
    data = IteratorData(5, '../data/dataset.csv')
    for i in data:
        print(i)
