from PyQt6.QtWidgets import (QMainWindow, QLabel, QPushButton, QLineEdit)

# window
window = QMainWindow()
window.setWindowTitle("Simulation: Stochastic modeling")
window.setGeometry(350, 300, 400, 200)

# line edit
question_le = QLineEdit(window)
question_le.setPlaceholderText("Enter your question pls")
font = question_le.font()
font.setPointSize(10)
question_le.setFont(font)
question_le.setFixedWidth(200)
question_le.move(100, 10)

# button
answer_btn = QPushButton(window)
answer_btn.move(150, 60)
answer_btn.setText("Answer")

# label
result_l = QLabel(window)
font = result_l.font()
font.setPointSize(15)
font.setBold(True)
result_l.setFont(font)
result_l.setFixedSize(250, 70)
result_l.move(50, 100)

window.show()
