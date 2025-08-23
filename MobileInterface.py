from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QColor, QPainter
import sys
import random


class CarGame(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple Car Racing Game")
        self.setGeometry(100, 100, 400, 600)
        self.setFixedSize(400, 600)

        # Player car position
        self.car_x = 175
        self.car_y = 500
        self.car_width = 50
        self.car_height = 100

        # Obstacle position
        self.obs_x = random.randint(50, 300)
        self.obs_y = -100
        self.obs_width = 50
        self.obs_height = 100

        self.score = 0
        self.game_over = False

        # Timer for game loop
        self.timer = QTimer()
        self.timer.timeout.connect(self.game_loop)
        self.timer.start(30)

        self.show()

    def paintEvent(self, event):
        painter = QPainter(self)

        # Draw road background
        if self.game_over:
            painter.fillRect(0, 0, 400, 600, QColor("red"))
        else:
            painter.fillRect(0, 0, 400, 600, QColor("gray"))

        # Draw player car
        painter.fillRect(self.car_x, self.car_y, self.car_width, self.car_height, QColor("blue"))

        # Draw obstacle
        painter.fillRect(self.obs_x, self.obs_y, self.obs_width, self.obs_height, QColor("green"))

        # Draw score
        painter.setPen(QColor("white"))
        painter.setFont(self.font())
        painter.drawText(10, 30, f"Score: {self.score}")

    def keyPressEvent(self, event):
        if self.game_over:
            return
        if event.key() == Qt.Key_Left and self.car_x > 0:
            self.car_x -= 20
        elif event.key() == Qt.Key_Right and self.car_x < 350:
            self.car_x += 20
        self.update()

    def game_loop(self):
        if self.game_over:
            return

        # Move obstacle down
        self.obs_y += 10

        # Reset obstacle and increase score
        if self.obs_y > 600:
            self.score += 1
            self.obs_y = -100
            self.obs_x = random.randint(50, 300)

        # Check collision
        if (self.car_y < self.obs_y + self.obs_height and
                self.car_y + self.car_height > self.obs_y and
                self.car_x < self.obs_x + self.obs_width and
                self.car_x + self.car_width > self.obs_x):
            self.game_over = True

        self.update()


# Run the game
app = QApplication(sys.argv)
window = CarGame()
sys.exit(app.exec_())
