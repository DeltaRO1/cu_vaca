from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Helth')
main_win.move(900, 70)
main_win.resize(800, 1000)

welcome = QLabel("Welcome to the Health status detection program!")
text = QLabel("The application allows you to use the Ruffer Test to make an initial diagnosis of your health.")
but = QPushButton("Start")
line = QVBoxLayout()

line.addWidget(welcome, alignment = Qt.AlignCenter)
line.addWidget(text, alignment= Qt.AlignCenter)
line.addWidget(but, alignment= Qt.AlignCenter)

main_win.setLayout(line)
main_win.show()
app.exec_()
