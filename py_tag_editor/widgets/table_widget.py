from PyQt5.QtWidgets import QWidget, QTableWidget, QLabel


class FileTableWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet('background-color: blue; border: 1px solid white;')

        self.__label = QLabel(self)
        self.setGeometry(20, 20, 100, 40)
        self.__label.setText('It Is Table')
