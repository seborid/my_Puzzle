import sys
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel

class SecondWindow(QWidget):
    data_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Second Window')
        self.setGeometry(200, 200, 300, 200)

        layout = QVBoxLayout()
        self.label = QLabel('Enter some text:', self)
        layout.addWidget(self.label)

        self.button = QPushButton('Send Data', self)
        self.button.clicked.connect(self.send_data)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def send_data(self):
        data = "Hello from Second Window"
        self.data_signal.emit(data)
        self.close()

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Main Window')
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()
        self.label = QLabel('No data received', self)
        layout.addWidget(self.label)

        self.button = QPushButton('Open Second Window', self)
        self.button.clicked.connect(self.open_second_window)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def open_second_window(self):
        self.second_window = SecondWindow()
        self.second_window.data_signal.connect(self.update_label)
        self.second_window.show()

    def update_label(self, data):
        self.label.setText(data)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())