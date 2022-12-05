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
        self.next_day = None
        self.button_next = None
        self.button_years = None
        self.button_weeks = None
        self.weeks = None
        self.years = None
        self.button_annots = None
        self.button_dir = None
        # self.path_to_dataset = 'data/dataset.csv'
        self.path_to_dataset = ''
        # self.path_to_annots = 'data/'
        self.path_to_dir = ''
        self.path_to_annots = ''
        self.initui()

    def initui(self):
        self.setWindowTitle('Weather downloader')
        self.setFixedSize(500, 500)

        while self.path_to_dataset == '':
            self.path_to_dataset = QFileDialog.getOpenFileName(self, 'Выберите файл с данными', '',
                                                               'CSV files (*.csv)')[0]

        self.button_annots = QPushButton('Создать файл аннотации', self)
        self.button_annots.move(255, 20)
        self.button_annots.resize(225, 50)
        self.button_annots.clicked.connect(self.create_annots)
        self.button_annots.setEnabled(False)
        self.button_annots.show()

        self.button_dir = QPushButton('Выбрать директорию \nдля аннотаций', self)
        self.button_dir.move(20, 20)
        self.button_dir.resize(225, 50)
        self.button_dir.clicked.connect(self.open_dir)
        if self.path_to_dir != '':
            self.button_dir.setText('Директория выбрана')
            self.button_dir.setEnabled(False)
            self.button_annots.setEnabled(True)
            self.button_years.setEnabled(True)
            self.button_weeks.setEnabled(True)
        self.button_dir.show()

        self.years = QLineEdit('Введите количество лет', self)
        self.years.move(20, 80)
        self.years.resize(225, 20)
        self.years.show()

        self.button_years = QPushButton('Разбить на года', self)
        self.button_years.move(20, 110)
        self.button_years.resize(225, 30)
        self.button_years.clicked.connect(self.split_years)
        self.button_years.setEnabled(False)
        self.button_years.show()

        self.weeks = QLineEdit('Введите количество недель', self)
        self.weeks.move(255, 80)
        self.weeks.resize(225, 20)
        self.weeks.show()

        self.button_weeks = QPushButton('Разбить на недели', self)
        self.button_weeks.move(255, 110)
        self.button_weeks.resize(225, 30)
        self.button_weeks.clicked.connect(self.split_weeks)
        self.button_weeks.setEnabled(False)
        self.button_weeks.show()

        self.button_next = QPushButton('Показать следующий день', self)
        self.button_next.move(20,430)
        self.button_next.resize(460, 50)
        self.button_next.setEnabled(False)
        self.button_next.show()

    def create_annots(self):
        shutil.copy(self.path_to_dataset, self.path_to_dir + '/dataset.csv.temp')
        self.path_to_annots = self.path_to_dir + '/dataset.csv.temp'
        self.button_annots.setText('Пересоздать файл аннотации')
        self.button_next.setEnabled(True)

    def open_dir(self):
        self.path_to_dir = QFileDialog.getExistingDirectory(self, 'Выберите директорию', '')
        self.button_dir.setText('Директория выбрана')
        self.button_dir.setEnabled(False)
        self.button_annots.setEnabled(True)
        self.button_years.setEnabled(True)
        self.button_weeks.setEnabled(True)

    def split_years(self):
        year_split_2.split_by_year_n(self.path_to_dir, self.path_to_dataset, int(self.years.text()))
        self.button_years.setText('Файл создан')
        
    def split_weeks(self):
        week_split_3.split_by_week_n(self.path_to_dir, self.path_to_dataset, int(self.weeks.text()))
        self.button_weeks.setText('Файл создан')



if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

    if window.path_to_annots != '':
        os.remove(window.path_to_annots)
