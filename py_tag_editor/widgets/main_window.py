from PyQt5.QtWidgets import QMainWindow, QTabWidget, QWidget, QVBoxLayout

from .setting_widget import SettingsWidget
from .main_widget import TagEditorMainWidget
from .table_widget import FileTableWidget
from .upper_panel import UpperPanelWidget
from .lower_panel import LowerPanelWidget


class TagEditorMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tag Editor")
        self.setMinimumSize(640, 480)
        self.__init_main_widget()
        self.setCentralWidget(self.__main_widget)

    def __init_main_widget(self):
        self.__table_widget = FileTableWidget()
        self.__upper_widget = UpperPanelWidget()
        self.__lower_widget = LowerPanelWidget()
        self.__main_widget = TagEditorMainWidget(lower_widget=self.__lower_widget,
                                                 upper_widget=self.__upper_widget,
                                                 table_widget=self.__table_widget,
                                                 setting_widget=SettingsWidget())
