# GUI pyqt6

import sys
import os
import shutil
import csv
from datetime import datetime

from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QInputDialog, QTableWidget, \
    QTableWidgetItem, QHeaderView, QAbstractItemView, QMenu, QAbstractScrollArea, QAbstractItemView, \
    QPushButton, QComboBox, QCheckBox, QSpinBox, QDoubleSpinBox, QLabel, QGroupBox, QGridLayout, QFormLayout \
    , QRadioButton, QButtonGroup, QSizePolicy, QScrollArea, QFrame, QTabWidget, QStackedWidget, QStackedLayout, \
    QStatusBar, QProgressBar, QToolButton, QToolBar, QStyle, QStyleOption, QStylePainter, QStyleFactory, \
    QStyleOptionProgressBar, QStyleOptionSlider, QStyleOptionToolButton, QStyleOptionButton, QStyleOptionTab, \
    QStyleOptionTabWidgetFrame, QStyleOptionTabBarBase, QLineEdit, QPlainTextEdit, QDateEdit, QTimeEdit

from PyQt6.QtGui import QCursor
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

from Lab2 import year_split_2
from Lab2 import week_split_3
from Lab2 import return_4


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.weeks = None
        self.years = None
        self.button_annots = None
        self.button_dir = None
        self.path_to_dataset = ''
        self.path_to_dir = ''
        self.path_to_annots = ''
        self.min_date = None
        self.max_date = None
        self.initui()

    def initui(self):
        self.setWindowTitle('Weather downloader')
        self.setFixedSize(500, 500)

        while self.path_to_dataset == '':
            self.path_to_dataset = QFileDialog.getOpenFileName(self, 'Выберите файл с данными', '',
                                                               'CSV files (*.csv)')[0]
        self.min_max_date()
        print(self.min_date, self.max_date)

        self.button_annots = QPushButton('Создать файл аннотации', self)
        self.button_annots.move(20, 70)
        self.button_annots.resize(200, 50)
        self.button_annots.clicked.connect(self.create_annots)
        self.button_annots.setEnabled(False)
        self.button_annots.show()

        self.button_dir = QPushButton('Выбрать директорию \nдля аннотаций', self)
        self.button_dir.move(20, 20)
        self.button_dir.resize(200, 50)
        self.button_dir.clicked.connect(self.open_dir)
        if self.path_to_dir != '':
            self.button_dir.setText('Директория выбрана')
            self.button_dir.setEnabled(False)
            self.button_annots.setEnabled(True)
        self.button_dir.show()

        self.years = QLineEdit('Введите количество лет', self)
        self.years.move(20, 130)
        self.years.resize(200, 20)
        self.years.show()

        self.weeks = QLineEdit('Введите количество недель', self)
        self.weeks.move(20, 160)
        self.weeks.resize(200, 20)
        self.weeks.show()

    def open_dir(self):
        self.path_to_dir = QFileDialog.getExistingDirectory(self, 'Выберите директорию', '')
        self.button_dir.setText('Директория выбрана')
        self.button_dir.setEnabled(False)
        self.button_annots.setEnabled(True)

    def create_annots(self):
        self.path_to_annots = self.path_to_dir + '/dataset.csv.temp'
        shutil.copy(self.path_to_dataset, self.path_to_annots)
        self.button_annots.setText('Файл аннотации создан')
        self.button_annots.setEnabled(False)

    def min_max_date(self):
        with open(self.path_to_dataset, 'r') as f:
            reader = csv.reader(f)
            rows = list(reader)
            rows = rows[2:]
            self.min_date = datetime.strptime(rows[0][0], '%Y-%m-%d')
            self.max_date = datetime.strptime(rows[-1][0], '%Y-%m-%d')



if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

    if window.path_to_annots != '':
        os.remove(window.path_to_annots)
