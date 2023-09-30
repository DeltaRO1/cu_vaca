from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Helth')
main_win.move(900, 70)
main_win.resize(800, 1000)
main_win.show()
app.exec_()
