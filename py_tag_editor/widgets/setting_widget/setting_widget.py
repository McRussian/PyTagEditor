from typing import Dict

from PyQt5.QtWidgets import QWidget, QLabel


class SettingsWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.__widgets: Dict[str, QWidget]
        self.__label = QLabel(self)
        self.__label.setGeometry(20, 40, 120, 40)
        self.__label.setText("It is Setting menu")
