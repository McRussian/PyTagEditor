from PyQt5.QtWidgets import QWidget, QGridLayout

from .menu_widget import MenuWidget


class TagEditorMainWidget(QWidget):
    def __init__(self,
                 upper_widget: QWidget,
                 table_widget: QWidget,
                 lower_widget: QWidget,
                 setting_widget: QWidget,
                 ):
        QWidget.__init__(self)
        self.setMinimumSize(620, 460)
        self.__upper_widget = upper_widget
        self.__table_widget = table_widget
        self.__lower_widget = lower_widget
        self.__setting_widget = setting_widget
        self.__init_widget()
        self.show()

    def __init_widget(self):
        grid = QGridLayout(self)
        grid.setSpacing(5)
        self.__upper_menu = MenuWidget()
        grid.addWidget(self.__upper_menu, 0, 0, 1, 10)

        self.__upper_widget.setParent(self)
        grid.addWidget(self.__upper_widget, 1, 0, 1, 10)
        self.__table_widget.setParent(self)
        grid.addWidget(self.__table_widget, 2, 0, 10, 7)
        self.__setting_widget.setParent(self)
        grid.addWidget(self.__setting_widget, 2, 7, 10, 3)
        self.__lower_widget.setParent(self)
        grid.addWidget(self.__lower_widget, 11, 0, 1, 10)
