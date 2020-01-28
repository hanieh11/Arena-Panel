# This Python file uses the following encoding: utf-8
import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from mainwindow import MainWindow

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()

    window.show()
    
    sys.exit(app.exec_())

    