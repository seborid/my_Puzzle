import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QLabel
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtCore import Qt

class PuzzleGame(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口标题
        self.setWindowTitle('myPuzzle')
        # 设置窗口大小和位置
        self.setGeometry(100, 100, 1100, 800)

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
        self.steps_label.setGeometry(850, 50, 200, 50)

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

    def shuffle_tiles(self):
        # 打乱拼图块
        random.shuffle(self.tiles)

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
        QMessageBox.information(self, 'Congratulations', 'Puzzle Solved!')

    def paintEvent(self, event):
        # 绘制拼图块
        painter = QPainter(self)
        for i in range(self.times):
            for j in range(self.times):
                index = i * self.times + j
                painter.drawPixmap(j * self.tile_size, i * self.tile_size, self.tiles[index])

if __name__ == '__main__':
    # 创建应用程序对象
    app = QApplication(sys.argv)
    # 创建主窗口对象
    ex = PuzzleGame()
    # 进入应用程序主循环
    sys.exit(app.exec_())