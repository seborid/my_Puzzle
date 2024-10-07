import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QLabel, QGridLayout, QPushButton, QFileDialog, \
    QWidget, QSpinBox
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtCore import Qt, QRect, QTimer
import load_image as test
import beginwindowsbuttonreact as begin


class PuzzleGame(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        if_challenge = False
        # 设置窗口标题
        self.setWindowTitle('拼图游戏')
        # 设置窗口大小和位置

        self.setGeometry(
            QApplication.desktop().screen().rect().center().x() - 550,
            QApplication.desktop().screen().rect().center().y() - 400,
            1100, 800
        )
        self.setFixedSize(1100, 800)
        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)

        self.times = 3
        self.tile_size = 800 // self.times
        self.steps = 0
        self.tiles = []
        self.original_tiles = []

        # 加载图像并分割成小块
        self.load_image()
        # 打乱拼图块
        self.shuffle_tiles()

        # 显示步数的标签
        self.steps_label = QLabel(f"步数: {self.steps}", self)
        self.steps_label.setGeometry(850, 350, 200, 50)
        # 固定窗口大小
        self.setFixedSize(1100, 800)
        self.steps_label.setFixedSize(200, 50)
        # 将标签添加到主窗口
        self.main_widget.layout = QGridLayout()
        # 创建按钮组件

        # 创建grid布局
        self.grid = QGridLayout()  # 创建网格布局
        self.setLayout(self.grid)
        self.grid.setSpacing(10)

        ############################
        # 选择新图片按钮
        new_image_button = QPushButton('选择新图', self)
        new_image_button.setMinimumSize(100, 50)
        new_image_button.clicked.connect(self.load_new_image)
        self.grid.addWidget(new_image_button, 1, 1)
        # 选择图片按钮
        choose_image_button = QPushButton('选择图片', self)
        choose_image_button.setMinimumSize(100, 50)
        choose_image_button.clicked.connect(self.load_so_image)
        self.grid.addWidget(choose_image_button, 1, 2)
        # 查看原图按钮
        check_button = QPushButton('查看原图', self)
        check_button.setMinimumSize(100, 50)
        check_button.clicked.connect(self.check)
        self.grid.addWidget(check_button, 2, 1)

        # 重新开始按钮
        restart_button = QPushButton('重新开始', self)
        restart_button.setMinimumSize(100, 50)
        restart_button.clicked.connect(self.shuffle_tiles)
        self.grid.addWidget(restart_button, 2, 2)
        # 设置图像分割次数
        self.times_text = QLabel('分割次数:', self)
        self.grid.addWidget(self.times_text, 4, 1)
        self.times_QSpinBox = QSpinBox(self)
        self.times_QSpinBox.setRange(2, 10)
        self.times_QSpinBox.setValue(3)
        self.times_QSpinBox.valueChanged.connect(self.change_times)
        self.grid.addWidget(self.times_QSpinBox, 4, 2)
        self.times_label = QLabel('分割次数:', self)
        self.grid.addWidget(self.times_label, 4, 1)
        self.times_QSpinBox = QSpinBox(self)
        self.times_QSpinBox.setRange(2, 10)
        self.times_QSpinBox.setValue(3)
        self.times_QSpinBox.valueChanged.connect(self.change_times)
        self.grid.addWidget(self.times_QSpinBox, 4, 2)

        # 挑战模式
        # 文字
        self.challenge_label = QLabel('挑战模式（秒）:', self)
        self.grid.addWidget(self.challenge_label, 7, 1, 1, 2)
        # 设置挑战最长时间
        self.challenge_time_label = QLabel('挑战时间为:', self)
        self.grid.addWidget(self.challenge_time_label, 6, 1)
        self.challenge_time_QSpinBox = QSpinBox(self)
        self.challenge_time_QSpinBox.setRange(1, 1000)
        self.challenge_time_QSpinBox.setValue(60)
        self.grid.addWidget(self.challenge_time_QSpinBox, 6, 2)
        # 开始挑战按钮
        self. challenge_button = QPushButton('开始挑战', self)
        self.challenge_button.setMinimumSize(100, 50)
        self.challenge_button.clicked.connect(self.start_challenge)
        self.grid.addWidget(self.challenge_button, 3, 1)
        # 停止挑战按钮
        self.stop_challenge_button = QPushButton('结束挑战', self)
        self.stop_challenge_button.setMinimumSize(100, 50)
        self.stop_challenge_button.setEnabled(False)
        self.stop_challenge_button.clicked.connect(self.stop)
        self.grid.addWidget(self.stop_challenge_button, 3, 2)
        # 显示时间
        self.time_label2 = QLabel('0', self)
        self.time_label2.setGeometry(1000, 395, 50, 50)
        self.time_label2.hide()

        # 设置网格布局的位置和大小
        gird_Qrect = QRect(850, 100, 200, 400)
        self.grid.setGeometry(gird_Qrect)
        # 将标签添加到主窗口
        self.main_widget.layout.addWidget(self.steps_label)



        # 显示窗口
        self.show()

    def check(self):
        #用一个新窗口显示原图
        self.new_window = QMainWindow()
        self.new_window.setWindowTitle('原图')
        self.new_window.setGeometry(
            QApplication.desktop().screen().rect().center().x() - 400,
            QApplication.desktop().screen().rect().center().y() - 400,
            800, 800
        )
        self.new_window.setFixedSize(800, 800)
        label = QLabel(self.new_window)
        label.setGeometry(0, 0, 800, 800)
        label.setPixmap(self.image)
        self.new_window.show()

    def load_image(self, image_path=0):
        # 加载并缩放图像
        self.image = QPixmap(f"image{image_path}.jpg").scaled(800, 800)
        self.tiles.clear()  # Clear the existing tiles
        for i in range(self.times):
            for j in range(self.times):
                # 分割图像成小块
                tile = self.image.copy(j * self.tile_size, i * self.tile_size, self.tile_size, self.tile_size)
                self.tiles.append(tile)
        self.original_tiles = self.tiles.copy()
        self.shuffle_tiles()

    def load_new_image(self):
        # 加载并缩放图像
        file_name, _ = QFileDialog.getOpenFileName(self, '选择图片', '.', 'Image Files(*.jpg *.png)')
        if file_name:
            self.image = QPixmap(file_name).scaled(800, 800)
            self.tiles.clear()  # Clear the existing tiles
            for i in range(self.times):
                for j in range(self.times):
                    # 分割图像成小块
                    tile = self.image.copy(j * self.tile_size, i * self.tile_size, self.tile_size, self.tile_size)
                    self.tiles.append(tile)
            self.original_tiles = self.tiles.copy()
            self.shuffle_tiles()

    def shuffle_tiles(self):
        # 打乱拼图块
        random.shuffle(self.tiles)
        self.update()

    def change_times(self):
        # 改变分割次数
        self.times = self.times_QSpinBox.value()
        self.tile_size = 800 // self.times
        self.tiles = []
        self.load_image()
        self.shuffle_tiles()
        self.steps = 0
        self.steps_label.setText(f"步数: {self.steps}")
        self.update()

    def is_puzzle_solved(self):
        # 检查拼图是否完成
        return self.tiles == self.original_tiles
        #处理挑战情况下的结果



    def mousePressEvent(self, event):
        # 处理鼠标按下事件
        if event.button() == Qt.LeftButton:
            x, y = event.pos().x(), event.pos().y()
            if x < 800 and y < 800:
                col = x // self.tile_size
                row = y // self.tile_size
                self.selected_index = row * self.times + col

    def mouseReleaseEvent(self, event):
        # 处理鼠标释放事件
        if event.button() == Qt.LeftButton:
            x, y = event.pos().x(), event.pos().y()
            if x < 800 and y < 800:
                col = x // self.tile_size
                row = y // self.tile_size
                target_index = row * self.times + col
                # 交换拼图块
                self.tiles[self.selected_index], self.tiles[target_index] = self.tiles[target_index], self.tiles[
                    self.selected_index]
                self.steps += 1
                self.steps_label.setText(f"步数: {self.steps}")
                self.update()
                if self.is_puzzle_solved():
                    self.show_congratulations()

    def show_congratulations(self):
        # 显示完成拼图的消息
        QMessageBox.information(self, '恭喜', '拼图完成!')
        try:
            self.timer.stop()
        except:
            pass
        if self.if_challenge:
            self.stop()

    def paintEvent(self, event):
        # 绘制拼图块
        painter = QPainter(self)
        for i in range(self.times):
            for j in range(self.times):
                index = i * self.times + j
                painter.drawPixmap(j * self.tile_size, i * self.tile_size, self.tiles[index])

    def keyPressEvent(self, event):
        # 处理键盘事件
        key = event.key()
        if key == Qt.Key_Escape:
            self.close()
        elif key == Qt.Key_R:
            self.shuffle_tiles()
            self.steps = 0
            self.steps_label.setText(f"步数: {self.steps}")
            self.update()

        # 挑战函数

    def start_challenge(self):
        self.steps = 0
        self.if_challenge = True
        self.steps_label.setText(f"步数: {self.steps}")
        #让开始挑战按钮失效
        self.challenge_time_QSpinBox.setEnabled(False)
        #让开始挑战按钮失效
        self.challenge_button.setEnabled(False)
        #让图片无法调整分割次数
        self.times_QSpinBox.setEnabled(False)
        #无法设置挑战时间
        self.challenge_time_QSpinBox.setEnabled(False)


        self.challenge_time = self.challenge_time_QSpinBox.value()
        self.time_elapsed = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # 每秒触发一次
        self.time_label2.show()
        self.stop_challenge_button.setEnabled(True)

    def update_time(self):
        self.time_elapsed += 1
        self.time_label2.setText(str(self.time_elapsed))
        if self.time_elapsed >= self.challenge_time:
            self.timer.stop()
            self.show_failed()
            self.time_elapsed = 0
            self.time_label2.setText(str(self.time_elapsed))
            self.timer.stop()
            self.steps = 0
            self.steps_label.setText(f"步数: {self.steps}")
            self.update()

    def show_failed(self):
        QMessageBox.information(self, ' ', '时间到,挑战失败！')

    def stop(self):
        self.timer.stop()
        self.time_label2.setText(str(self.time_elapsed))
        self.stop_challenge_button.setEnabled(False)
        #让按钮们重新生效
        self.challenge_button.setEnabled(True)
        self.times_QSpinBox.setEnabled(True)
        self.challenge_time_QSpinBox.setEnabled(True)


    def load_so_image(self):
        self.new_window = test.MainWindow()
        self.new_window.data_signal.connect(self.load_image)
        self.new_window.show()

    def PuzzleGamebegin(self):
        self.hide()
        self.new_window = begin.beginwindows()
        self.new_window.show()

if __name__ == '__main__':
    # 创建应用程序对象
    app = QApplication(sys.argv)
    window = begin.beginwindows()
    window.show()
    # 创建主窗口对象
    # 进入应用程序主循环
    sys.exit(app.exec_())
