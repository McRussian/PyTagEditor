from PyQt5.QtWidgets import QWidget


class SettingWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(120, 440)

        self.setStyleSheet('background-color: green;')
