# GUI pyqt6

import sys
import csv
from datetime import datetime

from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QInputDialog, QTableWidget, \
    QTableWidgetItem, QHeaderView, QAbstractItemView, QMenu, QAbstractScrollArea, QAbstractItemView, \
    QPushButton, QComboBox, QCheckBox, QSpinBox, QDoubleSpinBox, QLabel, QGroupBox, QGridLayout, QFormLayout
from PyQt6.QtGui import QCursor
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

from Lab2 import return_4


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button_annots = None
        self.button_dir = None
        # self.path_to_dataset = 'data/dataset.csv'
        self.path_to_dataset = ''
        # self.path_to_annots = 'data/'
        self.path_to_annots = ''
        self.initui()

    def initui(self):
        self.setWindowTitle('Weather downloader')
        self.setFixedSize(500, 500)

        while self.path_to_dataset == '':
            self.path_to_dataset = QFileDialog.getOpenFileName(self, 'Выберите файл с данными', '',
                                                               'CSV files (*.csv)')[0]

        self.button_dir = QPushButton('Выбрать директорию', self)
        self.button_dir.move(20, 20)
        self.button_dir.resize(200, 50)
        self.button_dir.clicked.connect(self.open_dir)
        if self.path_to_annots != '':
            self.button_dir.setText('Директория выбрана')
        self.button_dir.show()

        self.button_annots = QPushButton('Создать файл аннотации', self)
        self.button_annots.move(20, 70)
        self.button_annots.resize(200, 50)
        self.button_annots.clicked.connect(self.create_annots)
        self.button_annots.show()

    def create_annots(self):
        with open(self.path_to_dataset, 'r', encoding='utf8') as dataset:
            reader = csv.reader(dataset)
            date_data = list(reader)
            date_data = date_data[2:]
            date_data.sort(key=lambda x: datetime.strptime(x[0], '%Y-%m-%d'))
            with open(f'{self.path_to_dataset}.temp', 'w', encoding='utf8') as file:
                writer = csv.writer(file)
                writer.writerows(date_data)

        self.button_annots.setText('Файл аннотации создан')
        self.button_annots.setEnabled(False)

    def open_dir(self):
        self.path_to_annots = QFileDialog.getExistingDirectory(self, 'Выберите директорию', '')[0]
        self.button_dir.setText('Директория выбрана')
        self.button_dir.setEnabled(False)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
