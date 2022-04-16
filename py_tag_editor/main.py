import sys
from PyQt5.QtWidgets import QApplication

from py_tag_editor.widgets import TagEditorMainWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = TagEditorMainWindow()
    w.show()

    sys.exit(app.exec_())
