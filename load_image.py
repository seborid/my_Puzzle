import sys

from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QGridLayout
from PyQt5.QtGui import QPixmap

class MainWindow(QWidget):
    now_image = 0
    data_signal = pyqtSignal(int)
    def __init__(self):

        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('选择图片')
        self.setFixedSize(500, 500)  # 固定窗口大小
        self.move(QApplication.desktop().screen().rect().center() - self.rect().center())  # 居中显示窗口
        # 创建主布局
        main_layout = QVBoxLayout()

        # 网格布局
        small_layout = QGridLayout()
        button1 = QPushButton('上一个', self)
        button1.clicked.connect(self.past)
        button2 = QPushButton('下一个', self)
        button2.clicked.connect(self.next)
        button3=QPushButton('选择',self)
        button3.clicked.connect(self.choose)
        small_layout.addWidget(button1, 0, 0)
        small_layout.addWidget(button2, 0, 1)
        small_layout.addWidget(button3, 0, 2)

        # 创建一个小部件来包含小布局
        small_widget = QWidget(self)
        small_widget.setLayout(small_layout)
        small_widget.setFixedSize(500,100)  # 设置小布局的大小

        # 将小部件添加到主布局
        main_layout.addWidget(small_widget)

        # 添加其他小部件到主布局
        self.label = QLabel(self)
        pixmap = QPixmap('image0.jpg').scaled(400, 400)
        self.label.setPixmap(pixmap)
        main_layout.addWidget(self.label, alignment=Qt.AlignCenter)

        # 设置窗口的主布局
        self.setLayout(main_layout)

    def update_image(self, image_path):
        images = {0: 'image0.jpg', 1: 'image1.jpg', 2: 'image2.jpg'}
        pixmap = QPixmap(images[image_path]).scaled(400, 400)
        self.label.setPixmap(pixmap)

    def past(self):
        # 加载上一个图片
        self.update_image((self.now_image - 1)%3)

    def next(self):
        # 加载下一个图片
        self.update_image((self.now_image + 1)%3)
        self.now_image=(self.now_image + 1)%3

    def choose(self):
        self.data_signal.emit(self.now_image)
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())