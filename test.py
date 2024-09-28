from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QLabel
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Layout Example')
        self.setGeometry(100, 100, 300, 200)

        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)

        # 创建垂直布局
        vbox = QVBoxLayout()

        # 创建水平布局
        hbox = QHBoxLayout()

        # 创建按钮和标签
        button1 = QPushButton('Button 1', self)
        button2 = QPushButton('Button 2', self)
        label = QLabel('Hello, PyQt5!', self)

        # 将按钮和标签添加到水平布局中
        hbox.addWidget(button1)
        hbox.addWidget(button2)

        # 将标签添加到垂直布局中
        vbox.addWidget(label)
        # 将水平布局添加到垂直布局中
        vbox.addLayout(hbox)

        main_widget.setLayout(vbox)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())