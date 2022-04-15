from PyQt5.QtWidgets import QWidget


class UpperPanelWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedHeight(40)
        self.setMinimumWidth(660)
        self.setStyleSheet('background-color: red;')
