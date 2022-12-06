import csv
import os
import shutil

from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidget, \
    QTableWidgetItem, QAbstractItemView, \
    QPushButton, QLineEdit

from Lab2 import return_4
from Lab2 import week_split_3
from Lab2 import year_split_2


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button_file = None
        self.table = None
        self.label = None
        self.button_next = None
        self.button_years = None
        self.button_weeks = None
        self.weeks = None
        self.years = None
        self.button_annots = None
        self.button_dir = None
        self.first_day = None
        self.last_day = None
        self.path_to_dataset = ''
        self.path_to_dir = ''
        self.path_to_annots = ''

        self.initui()

    def initui(self):
        self.setWindowTitle('Weather downloader')
        self.setFixedSize(500, 355)

        self.start()

        self.button_file = QPushButton(f'Выбрать файл с датасетом. Текущий путь: \n{self.path_to_dataset}', self)
        self.button_file.move(20, 20)
        self.button_file.resize(460, 50)
        self.button_file.clicked.connect(self.reset)
        self.button_file.show()

        self.button_dir = QPushButton('Выбрать директорию \nдля аннотаций', self)
        self.button_dir.move(20, 80)
        self.button_dir.resize(225, 50)
        self.button_dir.clicked.connect(self.open_dir)
        if self.path_to_dir != '':
            self.button_dir.setText('Директория выбрана')
            self.button_dir.setEnabled(False)
            self.button_annots.setEnabled(True)
            self.button_years.setEnabled(True)
            self.button_weeks.setEnabled(True)
        self.button_dir.show()

        self.button_annots = QPushButton('Создать файл аннотации', self)
        self.button_annots.move(255, 80)
        self.button_annots.resize(225, 50)
        self.button_annots.clicked.connect(self.create_annots)
        self.button_annots.setEnabled(False)
        self.button_annots.show()

        self.years = QLineEdit(self)
        self.years.setPlaceholderText('Количество лет')
        self.years.move(20, 140)
        self.years.resize(225, 30)
        self.years.show()

        self.button_years = QPushButton('Разбить на года', self)
        self.button_years.move(20, 170)
        self.button_years.resize(225, 30)
        self.button_years.clicked.connect(self.split_years)
        self.button_years.setEnabled(False)
        self.button_years.show()

        self.weeks = QLineEdit(self)
        self.weeks.setPlaceholderText('Количество недель')
        self.weeks.move(255, 140)
        self.weeks.resize(225, 30)
        self.weeks.show()

        self.button_weeks = QPushButton('Разбить на недели', self)
        self.button_weeks.move(255, 170)
        self.button_weeks.resize(225, 30)
        self.button_weeks.clicked.connect(self.split_weeks)
        self.button_weeks.setEnabled(False)
        self.button_weeks.show()

        self.table = QTableWidget(self)
        self.table.setColumnCount(4)
        self.table.setRowCount(1)
        self.table.setHorizontalHeaderLabels(['Дата', 'Температура', 'Давление', 'Ветер'])
        self.table.move(20, 220)
        self.table.resize(460, 55)
        self.table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table.setEnabled(False)
        self.table.show()

        self.button_next = QPushButton('Показать следующий день', self)
        self.button_next.move(20, 285)
        self.button_next.resize(460, 50)
        self.button_next.clicked.connect(self.next_day)
        self.button_next.setEnabled(False)
        self.button_next.show()

        self.show()

    def next_day(self):
        weather = return_4._next(self.path_to_dataset)
        self.table.setItem(0, 0, QTableWidgetItem(weather[0]))
        self.table.setItem(0, 1, QTableWidgetItem(weather[1]))
        self.table.setItem(0, 2, QTableWidgetItem(weather[2]))
        self.table.setItem(0, 3, QTableWidgetItem(weather[3]))

    def create_annots(self):
        shutil.copy(self.path_to_dataset, self.path_to_dir + '/dataset.csv.temp')
        self.path_to_annots = self.path_to_dir + '/dataset.csv.temp'
        with open(self.path_to_annots, 'r', encoding='utf8') as file:
            reader = csv.reader(file)
            rows = [row for row in reader]
        with open(self.path_to_annots, 'w', encoding='utf8', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows[2:])
        self.button_annots.setText('Пересоздать файл аннотации')
        self.button_next.setEnabled(True)
        self.table.setEnabled(True)

    def open_dir(self):
        self.path_to_dir = QFileDialog.getExistingDirectory(self, 'Выберите директорию', '')
        self.button_dir.setText('Директория выбрана')
        self.button_dir.setEnabled(False)
        self.button_annots.setEnabled(True)
        self.button_years.setEnabled(True)
        self.button_weeks.setEnabled(True)

    def split_years(self):
        # if self.years.text() is not int: do nothing
        if self.years.text().isdigit():
            year_split_2.split_by_year_n(self.path_to_dir, self.path_to_dataset, int(self.years.text()))
            self.button_years.setText('Файл создан')

    def split_weeks(self):
        if self.years.text().isdigit():
            week_split_3.split_by_week_n(self.path_to_dir, self.path_to_dataset, int(self.weeks.text()))
            self.button_weeks.setText('Файл создан')

    def start(self):
        while self.path_to_dataset == '':
            self.path_to_dataset = QFileDialog.getOpenFileName(self, 'Выберите файл с данными', '',
                                                               'CSV files (*.csv)')[0]

        with open(self.path_to_dataset, 'r', encoding='utf8') as file:
            reader = csv.reader(file)
            next(reader)
            next(reader)
            for row in reader:
                if row[0] == 'Date':
                    continue
                else:
                    self.first_day = row[0]
                    break
        with open(self.path_to_dataset, 'r', encoding='utf8') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == 'Date':
                    continue
                else:
                    self.last_day = row[0]

    def reset(self):
        self.button_dir.setEnabled(True)
        self.button_annots.setEnabled(False)
        self.button_years.setEnabled(False)
        self.button_weeks.setEnabled(False)
        self.button_annots.setText('Создать файл аннотации')
        self.button_dir.setText('Выбрать директорию')
        self.button_years.setText('Разбить на года')
        self.button_weeks.setText('Разбить на недели')
        self.button_next.setEnabled(False)
        self.table.setEnabled(False)
        self.table.setItem(0, 0, QTableWidgetItem(''))
        self.table.setItem(0, 1, QTableWidgetItem(''))
        self.table.setItem(0, 2, QTableWidgetItem(''))
        self.table.setItem(0, 3, QTableWidgetItem(''))

        self.path_to_dataset = ''
        self.path_to_dir = ''
        self.path_to_annots = ''

        self.start()

        self.button_file.setText(f'Выбрать файл с датасетом. Текущий путь: \n{self.path_to_dataset}')


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

    if window.path_to_annots != '':
        os.remove(window.path_to_annots)
