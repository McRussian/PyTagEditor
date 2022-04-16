from PyQt5.QtWidgets import QWidget, QLabel


class UpperPanelWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedHeight(40)
        self.setStyleSheet('background-color: red; border: 1px solid white;')
        self.__label = QLabel(self)
        self.__label.setGeometry(10, 10, 100, 20)
        self.__label.setText("Upper Menu")
