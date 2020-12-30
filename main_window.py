import sys
import random
#from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt

class DrawableWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QtWidgets.QLabel()
        canvas = QtGui.QPixmap(400, 300)
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)
        self.draw_something()

    def _drawline(self):
        painter = QtGui.QPainter(self.label.pixmap())
        painter.drawLine(50,10, 300, 200)
        painter.end()

    def _drawpoint(self):
        painter = QtGui.QPainter(self.label.pixmap())
        painter.drawPoint(200,200)
        painter.end()
    
    def _drawpen(self):
        painter = QtGui.QPainter(self.label.pixmap())
        pen = QtGui.QPen()
        pen.setWidth(40)
        pen.setColor(QtGui.QColor('red'))
        painter.setPen(pen)
        painter.drawPoint(100,100)
        painter.end()

    def _drawdots(self):
        painter = QtGui.QPainter(self.label.pixmap())
        colors = ['#ff0000', '#00ff00', '#0000ff']
        pen = QtGui.QPen()
        pen.setWidth(3)

        for n in range(1000):
            pen.setColor(QtGui.QColor(random.choice(colors)))
            painter.setPen(pen)
            painter.drawPoint(
                200 + random.randint(-150, 150),
                150 + random.randint(-100, 100)
            )

    def draw_something(self):
        #self._drawline()
        #self._drawpoint()
        #self._drawpen()
        self._drawdots()

'''
class PainterMainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(PainterMainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("Painter Suite")
        label = QLabel("This is my painter suite!")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)
'''

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    #window = PainterMainWindow()
    window = DrawableWindow()
    window.show()

    app.exec()