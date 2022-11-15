# GUI pyqt6

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QInputDialog, QTableWidget, \
    QTableWidgetItem, QHeaderView, QAbstractItemView, QMenu, QAbstractScrollArea, QAbstractItemView
from PyQt6.QtGui import QCursor
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from Lab2 import return_4


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.show()

    path_to_dataset = ''
    while not path_to_dataset:
        path_to_dataset = QFileDialog.getOpenFileName(window, 'Выберите файл с данными', '', 'CSV files (*.csv)')[0]

    print(path_to_dataset)

    sys.exit(app.exec())
