from PyQt5.QtWidgets import QMainWindow, QTabWidget

from .setting_widget import SettingWidget
from .tab_widget import TagEditorMainWidget
from .table_widget import FileTableWidget
from .upper_panel import UpperPanelWidget
from .lower_panel import LowerPanelWidget


class TagEditorMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tag Editor")
        self.setMinimumSize(640, 480)
        self.__main_tab = QTabWidget(self)
        self.setCentralWidget(self.__main_tab)

        self.__init_main_tab()

    def __init_main_tab(self):
        self.__table_widget = FileTableWidget()
        self.__upper_widget = UpperPanelWidget()
        self.__lower_widget = LowerPanelWidget()

        self.__main_tab.addTab(TagEditorMainWidget(lower_widget=self.__lower_widget,
                                                   upper_widget=self.__upper_widget,
                                                   table_widget=self.__table_widget,
                                                   setting_widget=SettingWidget()), "Renamer")
        self.__main_tab.addTab(TagEditorMainWidget(lower_widget=self.__lower_widget,
                                                   upper_widget=self.__upper_widget,
                                                   table_widget=self.__table_widget,
                                                   setting_widget=SettingWidget()), "Editor")
        self.__main_tab.addTab(TagEditorMainWidget(lower_widget=self.__lower_widget,
                                                   upper_widget=self.__upper_widget,
                                                   table_widget=self.__table_widget,
                                                   setting_widget=SettingWidget()), "Generator")
        self.__main_tab.addTab(TagEditorMainWidget(lower_widget=self.__lower_widget,
                                                   upper_widget=self.__upper_widget,
                                                   table_widget=self.__table_widget,
                                                   setting_widget=SettingWidget()), "Decoder")
        self.__main_tab.addTab(TagEditorMainWidget(lower_widget=self.__lower_widget,
                                                   upper_widget=self.__upper_widget,
                                                   table_widget=self.__table_widget,
                                                   setting_widget=SettingWidget()), "Export")


