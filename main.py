import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QLabel, QGridLayout, QPushButton, QFileDialog, \
    QWidget, QSpinBox
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtCore import Qt, QRect, QTimer


class PuzzleGame(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口标题
        self.setWindowTitle('myPuzzle')
        # 设置窗口大小和位置
        self.setGeometry(100, 100, 1100, 800)
        #总体布局
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
        self.steps_label = QLabel(f"Steps: {self.steps}", self)
        self.steps_label.setGeometry(800, 600, 200, 50)
        #将标签添加到主窗口
        self.main_widget.layout = QGridLayout()
        # 创建按钮组件
        #创建grid布局
        self.grid = QGridLayout() # 创建网格布局
        self.setLayout(self.grid)
        self.grid.setSpacing(10)
        #重新开始按钮
        restart_button = QPushButton('重新开始', self)
        restart_button.clicked.connect(self.shuffle_tiles)
        self.grid.addWidget(restart_button, 1, 0)
        #选择新图片按钮
        new_image_button = QPushButton('选择图片', self)
        new_image_button.clicked.connect(self.load_new_image)
        self.grid.addWidget(new_image_button, 1, 1)
        #设置图像分割次数
        self.times_label = QLabel('分割次数:', self)
        self.grid.addWidget(self.times_label, 3, 0)
        self.times_QSpinBox = QSpinBox(self)
        self.times_QSpinBox.setRange(2, 10)
        self.times_QSpinBox.setValue(3)
        self.times_QSpinBox.valueChanged.connect(self.change_times)
        self.grid.addWidget(self.times_QSpinBox, 3, 1)

        #挑战模式
        #文字
        self.challenge_label = QLabel('挑战模式（秒）:', self)
        self.grid.addWidget(self.challenge_label, 4, 0,1,2)
        #设置挑战最长时间
        self.challenge_time_label = QLabel('挑战时间为:', self)
        self.grid.addWidget(self.challenge_time_label, 5, 0)
        self.challenge_time_QSpinBox = QSpinBox(self)
        self.challenge_time_QSpinBox.setRange(1, 1000)
        self.challenge_time_QSpinBox.setValue(60)
        self.grid.addWidget(self.challenge_time_QSpinBox, 5, 0)
        #开始挑战按钮
        challenge_button = QPushButton('开始挑战', self)
        challenge_button.clicked.connect(self.start_challenge)
        self.grid.addWidget(challenge_button, 6, 0)
        #停止挑战按钮
        self.stop_challenge_button = QPushButton('结束挑战', self)
        self.stop_challenge_button.setEnabled(False)
        self.stop_challenge_button.clicked.connect(self.stop)
        self.grid.addWidget(self.stop_challenge_button, 6, 1)
        #显示时间
        self.time_label1 = QLabel('已用时间:', self)
        self.time_label1.setGeometry(850, 300, 200, 50)
        self.time_label1.hide()
        self.time_label2 = QLabel('0', self)
        self.time_label2.setGeometry(940, 300, 200, 50)
        self.time_label2.hide()

        # 设置网格布局的位置和大小
        gird_Qrect=QRect(850,100,200,200)
        self.grid.setGeometry(gird_Qrect)
        #将标签添加到主窗口
        self.main_widget.layout.addWidget(self.steps_label)

        # 显示窗口
        self.show()

    def load_image(self):
        # 加载并缩放图像
        self.image = QPixmap('puzzle_image.jpg').scaled(800, 800)
        for i in range(self.times):
            for j in range(self.times):
                # 分割图像成小块
                tile = self.image.copy(j * self.tile_size, i * self.tile_size, self.tile_size, self.tile_size)
                self.tiles.append(tile)
        self.original_tiles = self.tiles.copy()

    #选择新图片
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
        #改变分割次数
        self.times = self.times_QSpinBox.value()
        self.tile_size = 800 // self.times
        self.tiles = []
        self.load_image()
        self.shuffle_tiles()
        self.steps = 0
        self.steps_label.setText(f"Steps: {self.steps}")
        self.update()

    def is_puzzle_solved(self):
        # 检查拼图是否完成
        return self.tiles == self.original_tiles

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
                self.tiles[self.selected_index], self.tiles[target_index] = self.tiles[target_index], self.tiles[self.selected_index]
                self.steps += 1
                self.steps_label.setText(f"Steps: {self.steps}")
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
            self.steps_label.setText(f"Steps: {self.steps}")
            self.update()

    #挑战函数
    def start_challenge(self):
        self.challenge_time = self.challenge_time_QSpinBox.value()
        self.time_elapsed = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # 每秒触发一次
        self.time_label1.show()
        self.time_label2.show()
        self.stop_challenge_button.setEnabled(True)
        self.shuffle_tiles()

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
            self.steps_label.setText(f"Steps: {self.steps}")
            self.update()

    def show_failed(self):
        QMessageBox.information(self,' ','时间到,挑战失败！')

    def stop(self):
        self.timer.stop()
        self.time_elapsed = 0
        self.time_label2.setText(str(self.time_elapsed))
        self.stop_challenge_button.setEnabled(False)



if __name__ == '__main__':
    # 创建应用程序对象
    app = QApplication(sys.argv)
    # 创建主窗口对象
    ex = PuzzleGame()
    # 进入应用程序主循环
    sys.exit(app.exec_())