import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLCDNumber, QPushButton, QLabel
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QFont

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Digital Clock (PyQt5)")
        self.setFixedSize(700, 600)

        self.is_24h = True

        # Time Display
        self.lcd = QLCDNumber()
        self.lcd.setDigitCount(8)   # HH:MM:SS
        self.lcd.setSegmentStyle(QLCDNumber.Flat)
        self.lcd.setMinimumHeight(90)

        # Date + Day
        self.date_label = QLabel()
        f = QFont()
        f.setPointSize(12)
        self.date_label.setFont(f)
        self.date_label.setAlignment(Qt.AlignCenter)

        # Buttons
        self.toggle_btn = QPushButton("Switch to 12h")
        self.toggle_btn.clicked.connect(self.toggle_format)

        self.exit_btn = QPushButton("Exit")
        self.exit_btn.clicked.connect(self.close)

        btn_row = QHBoxLayout()
        btn_row.addWidget(self.toggle_btn)
        btn_row.addWidget(self.exit_btn)

        # Layout
        root = QVBoxLayout()
        root.addWidget(self.lcd)
        root.addWidget(self.date_label)
        root.addLayout(btn_row)
        self.setLayout(root)

        # Timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_clock)
        self.timer.start(1000)  # per 1 second

        self.update_clock()

    def toggle_format(self):
        self.is_24h = not self.is_24h
        self.toggle_btn.setText("Switch to 24h" if not self.is_24h else "Switch to 12h")
        self.update_clock()

    def update_clock(self):
        now = QTime.currentTime()
        if self.is_24h:
            time_text = now.toString("HH:mm:ss")
        else:
            time_text = now.toString("hh:mm:ss AP")  # AP = AM/PM
        self.lcd.display(time_text)

        today = QDate.currentDate()
        # Example: Saturday, 23 Aug 2025
        self.date_label.setText(today.toString("dddd, dd MMM yyyy"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = DigitalClock()
    w.show()
    sys.exit(app.exec_())
