import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QHBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt


class StopWatch(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("StopWatch")
        self.time = QTime(0, 0, 0, 0)

        # Initial text uses the correct format
        self.time_label = QLabel("00:00:00.00", self)

        self.start_button = QPushButton("Start", self)
        self.stop_button = QPushButton("Stop", self)
        self.reset_button = QPushButton("Reset", self)
        self.timer = QTimer(self)

        self.initUI()

    def initUI(self):
        # The main vertical layout
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)

        # A horizontal layout for the buttons
        hbox = QHBoxLayout()
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)

        # Add the button layout to the main vertical layout
        vbox.addLayout(hbox)

        # Set the main layout for the window
        self.setLayout(vbox)
        self.time_label.setAlignment(Qt.AlignCenter)

        # Stylesheet
        self.setStyleSheet("""
            QPushButton {
                font-size: 50px;
                background-color: #4CAF50; /* A slightly nicer color */
                color: white;
                border-radius: 10px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QLabel {
                font-size: 120px;
                background-color: #333; /* Dark background for contrast */
                color: #00FF00;       /* Green digital-clock color */
                border-radius: 20px;
                font-family: 'Courier New', Courier, monospace; /* Monospaced font */
            }
        """)

        # Connect signals to slots
        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_display)

    def start(self):
        # Start the timer with a 10ms interval for hundredths of a second
        self.timer.start(10)

    def stop(self):
        self.timer.stop()

    def reset(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.time_label.setText(self.format_time(self.time))

    # *** PROBLEM 1 & 2 FIXED HERE ***
    def format_time(self, time):
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        # Get milliseconds (0-999) and divide by 10 to get hundredths (0-99)
        hundredths = time.msec() // 10
        return f"{hours:02}:{minutes:02}:{seconds:02}.{hundredths:02}"

    def update_display(self):
        # Add 10 milliseconds to the current time
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.format_time(self.time))


def main():
    app = QApplication(sys.argv)
    stopwatch = StopWatch()
    stopwatch.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()