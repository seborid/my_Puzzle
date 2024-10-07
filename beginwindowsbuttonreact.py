from PyQt5.QtWidgets import QApplication, QWidget
import beginwindows as begin
from beginwindows import Ui_Form
import main as mainwindows
import sys
class beginwindows(QWidget, Ui_Form):

    def __init__(self):
        super(beginwindows, self).__init__()
        self.setupUi(self)

        self.setFixedSize(800, 600)  # Set the fixed size (width, height)
        self.pushButton_2.clicked.connect(self.pushButton_2react)
        self.pushButton.clicked.connect(self.start_challenge)
        self.backgurand.setStyleSheet("background-image: url('image2.jpg'); background-size: cover;")
    def start(self):
        self.hide()
        self.new_window = mainwindows.MainWindow()
        self.new_window.show()

    def pushButton_2react(self):
        self.hide()
        self.new_window = mainwindows.PuzzleGame()
        self.new_window.show()

    def start_challenge(self):
        self.hide()
        self.new_window = mainwindows.PuzzleGamebegin()
        self.new_window.show()