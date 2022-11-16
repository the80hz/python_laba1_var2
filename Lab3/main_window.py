# GUI pyqt6

import sys
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
        self.button_dir = None
        self.path_to_dataset = 'data/dataset.csv'
        self.path_to_annots = 'data/'
        self.initui()

    def initui(self):
        self.setWindowTitle('Weather downloader')
        self.setGeometry(300, 300, 500, 500)
        self.setFixedSize(500, 500)

        while self.path_to_dataset == '':
            self.path_to_dataset = QFileDialog.getOpenFileName(self, 'Выберите файл с данными', '',
                                                               'CSV files (*.csv)')[0]

        self.button_dir = QPushButton('Выбрать директорию', self)
        self.button_dir.move(200, 200)
        self.button_dir.resize(200, 50)
        self.button_dir.clicked.connect(self.open_dir)
        self.button_dir.show()

    def open_dir(self):
        self.path_to_annots = QFileDialog.getExistingDirectory(self, 'Выберите директорию', '')[0]
        self.button_dir.setText('Директория выбрана')


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
