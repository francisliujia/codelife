import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication)

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        container = QWidget()
        containerLayout = QVBoxLayout()
        container.setLayout(containerLayout)

        self.setCentralWidget(container)


app = QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec_())