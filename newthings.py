import sys

from PyQt5.QtWidgets import (QApplication,QMainWindow,QLabel,QWidget,QVBoxLayout,QHBoxLayout,QGridLayout)
from PyQt5.QtGui import QPixmap

class MianWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Rizowan")
        self.setGeometry(700,300,500,500)
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        label1 = QLabel("#1",self)
        label2 = QLabel("#2", self)
        label3 = QLabel("#3", self)
        label4 = QLabel("#4", self)
        label5 = QLabel("#5", self)
        label1.setStyleSheet("background-color:Green;")
        label2.setStyleSheet("background-color:Red;")
        label3.setStyleSheet("background-color:Yellow;")
        label4.setStyleSheet("background-color:Blue;")
        label5.setStyleSheet("background-color:Purple;")

        Hbox = QHBoxLayout()

        Hbox.addWidget(label1)
        Hbox.addWidget(label2)
        Hbox.addWidget(label3)
        Hbox.addWidget(label4)
        Hbox.addWidget(label5)

        central_widget.setLayout(Hbox)

def main():
    app = QApplication(sys.argv)
    window = MianWindow()
    window.show()
    sys.exit(app.exec_())
if __name__ == "__main__":
    main()