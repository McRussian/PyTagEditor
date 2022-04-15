from PyQt5.QtWidgets import QWidget


class TagEditorMainWidget(QWidget):
    def __init__(self, upper_widget: QWidget, table_widget: QWidget, lower_widget: QWidget, setting_widget: QWidget):
        super().__init__()
        self.setMinimumSize(620, 460)

        self.__upper_widget = upper_widget
        self.__table_widget = table_widget
        self.__lower_widget = lower_widget
        self.__setting_widget = setting_widget
        self.__init_widget()

    def __init_widget(self):
        self.__upper_widget.setParent(self)
        self.__upper_widget.setGeometry(0, 0, self.__upper_widget.width(), self.__upper_widget.height())

        self.__table_widget.setParent(self)
        self.__table_widget.move(0, 40)

        self.__lower_widget.setParent(self)
        self.__lower_widget.move(0, 420)

        self.__setting_widget.setParent(self)
        self.__setting_widget.move(320, 40)
