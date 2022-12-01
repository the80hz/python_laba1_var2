# GUI pyqt6

import sys
import os
import shutil
import csv
from datetime import datetime

from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QInputDialog, QTableWidget, \
    QTableWidgetItem, QHeaderView, QAbstractItemView, QMenu, QAbstractScrollArea, QAbstractItemView, \
    QPushButton, QComboBox, QCheckBox, QSpinBox, QDoubleSpinBox, QLabel, QGroupBox, QGridLayout, QFormLayout, \
    QRadioButton, QButtonGroup, QSizePolicy, QScrollArea, QFrame, QTabWidget, QStackedWidget, QStackedLayout, \
    QStatusBar, QProgressBar, QToolButton, QToolBar, QStyle, QStyleOption, QStylePainter, QStyleFactory, \
    QStyleOptionProgressBar, QStyleOptionSlider, QStyleOptionToolButton, QStyleOptionButton, QStyleOptionTab, \
    QStyleOptionTabWidgetFrame, QStyleOptionTabBarBase, QLineEdit, QPlainTextEdit, QDateEdit, QTimeEdit, \
    QDateTimeEdit, QCalendarWidget, QDial, QSlider, QScrollBar, QSplitter, QTreeView, QTreeWidget, QTreeWidgetItem, \
    QHeaderView, QAbstractItemView, QMenu, QAbstractScrollArea, QAbstractItemView, QTableWidget, QTableWidgetItem

from PyQt6.QtGui import QCursor
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

from Lab2 import return_4


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.weeks_checkbox = None
        self.years_checkbox = None
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

        self.years = QLineEdit(self)
        self.years.setPlaceholderText = 'Введите количество лет'
        self.years.move(20, 130)
        self.years.resize(170, 20)
        self.years.show()

        self.weeks = QLineEdit(self)
        self.weeks.setPlaceholderText = 'Введите количество недель'
        self.weeks.move(20, 160)
        self.weeks.resize(170, 20)
        self.weeks.show()

        self.years_checkbox = QCheckBox(self)
        self.years_checkbox.move(200, 130)
        self.years_checkbox.resize(200, 20)
        self.years_checkbox.show()

        self.weeks_checkbox = QCheckBox(self)
        self.weeks_checkbox.move(200, 160)
        self.weeks_checkbox.resize(170, 20)
        self.weeks_checkbox.show()

    def create_annots(self):
        shutil.copy(self.path_to_dataset, self.path_to_dir + '/dataset.csv.temp')
        self.path_to_annots = self.path_to_dir + '/dataset.csv.temp'
        self.button_annots.setText('Файл аннотации создан')

    def open_dir(self):
        self.path_to_dir = QFileDialog.getExistingDirectory(self, 'Выберите директорию', '')
        self.button_dir.setText('Директория выбрана')
        self.button_dir.setEnabled(False)
        self.button_annots.setEnabled(True)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

    if window.path_to_annots != '':
        os.remove(window.path_to_annots)
