from typing import Dict

from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout


class MenuWidget(QWidget):
    def __init__(self, parent: QWidget = None):
        QWidget.__init__(self)
        self.setParent(parent)
        self.setFixedHeight(60)
        self.setMinimumWidth(620)
        self.__buttons: Dict[str, QPushButton] = dict()
        self.__init_widget()

    def __init_widget(self):
        h_layout = QHBoxLayout(self)
        h_layout.setSpacing(5)

        for name in ['Renamer', 'Editor', 'Generator', 'Decoder', 'Exports']:
            self.__buttons[name] = QPushButton(name)
            self.__buttons[name].setFixedSize(100, 40)
            self.__buttons[name].setText(name)
            h_layout.addWidget(self.__buttons[name])
