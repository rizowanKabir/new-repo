from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QGridLayout

# function
def button_click(value):
    current = display.text()
    display.setText(current + value)

# function
def calculate():
    try:
        result = str(eval(display.text()))
        display.setText(result)
    except:
        display.setText("Error")

# app make
app = QApplication([])
window = QWidget()
window.setWindowTitle("Desktop Calculator")
window.setGeometry(100, 100, 300, 400)

layout = QVBoxLayout()
display = QLineEdit()
layout.addWidget(display)

# button grid
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

grid = QGridLayout()
for row in range(4):
    for col in range(4):
        btn_text = buttons[row][col]
        button = QPushButton(btn_text)
        grid.addWidget(button, row, col)
        if btn_text == "=":
            button.clicked.connect(calculate)
        else:
            button.clicked.connect(lambda checked, text=btn_text: button_click(text))

layout.addLayout(grid)
window.setLayout(layout)
window.show()
app.exec_()
