from PyQt5.QtWidgets import QWidget, QTableWidget


class FileTableWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(320, 440)
        self.setStyleSheet('background-color: blue;')
