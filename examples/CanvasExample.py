#https://www.learnpyqt.com/tutorials/bitmap-graphics/
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

COLORS = [
# 17 undertones https://lospec.com/palette-list/17undertones
'#000000', '#141923', '#414168', '#3a7fa7', '#35e3e3', '#8fd970', '#5ebb49',
'#458352', '#dcd37b', '#fffee5', '#ffd035', '#cc9245', '#a15c3e', '#a42f3b',
'#f45b7a', '#c24998', '#81588d', '#bcb0c2', '#ffffff',
]

class DrawableCanvas(QtWidgets.QLabel):

    def __init__(self, width = 640, height = 480):
        super().__init__()
        pixmap = QtGui.QPixmap(width, height)
        self.setPixmap(pixmap)
        self.last_x, self.last_y = None, None
        self.pen_color = QtGui.QColor('#000000')

    def set_pen_color(self, color):
        self.pen_color = QtGui.QColor(color)
    
    def mouseMoveEvent(self, e):
        if self.last_x is None:
            self.last_x = e.x()
            self.last_y = e.y()
            return
        
        painter = QtGui.QPainter(self.pixmap())
        pen = painter.pen()
        pen.setWidth(4)
        pen.setColor(self.pen_color)
        painter.setPen(pen)
        painter.drawLine(self.last_x, self.last_y, e.x(), e.y())
        painter.end()
        self.update()

        self.last_x = e.x()
        self.last_y = e.y()
    
    def mouseReleaseEvent(self, e):
        self.last_x = None
        self.last_y = None

class PaletteButton(QtWidgets.QPushButton):
    def __init__(self, color):
        super().__init__()
        self.setFixedSize(QtCore.QSize(24,24))
        self.color = color
        self.setStyleSheet("background-color:%s" % color)

class DrawableWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.canvas = DrawableCanvas()

        w = QtWidgets.QWidget()
        l = QtWidgets.QVBoxLayout()
        w.setLayout(l)
        l.addWidget(self.canvas)

        palette = QtWidgets.QHBoxLayout()
        self.add_palette_buttons(palette)
        l.addLayout(palette)

        self.setCentralWidget(w)
    
    def add_palette_buttons(self, pal):
        for c in COLORS:
            btn = PaletteButton(c)
            btn.pressed.connect(lambda c=c: self.canvas.set_pen_color(c))
            pal.addWidget(btn)


def main():
    app = QtWidgets.QApplication(sys.argv)
    win = DrawableWindow()
    win.show()
    app.exec_()

if __name__ == "__main__":
    main()
