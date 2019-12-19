import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from Ui_mainwindow import *


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_start.clicked.connect(self.start)
        self.pushButton_stop.clicked.connect(self.stop)
        self.pushButton_quit.clicked.connect(self.quit)
        
    def scraper(self, url):
        pass # TODO

    def multi_process(self):
        pass # TODO

    def start(self):
        pass

    def stop(self):
        QtWidgets.QMessageBox.about(self, "Stop", "Don't Panic\nDon't stop me")

    def quit(self):
        sys.exit(1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())

