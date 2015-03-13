from PySide.QtCore import *
from PySide.QtGui import *
import sys

 ##  CIRCLE
class Simple_drawing_window3(QWidget):

    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Drawing")
        self.setGeometry(300, 300, 350, 350)
        self.setWindowTitle('Draw circles')
    def paintEvent(self, event):
        paint = QPainter()
        paint.begin(self)
        # optional
        paint.setRenderHint(QPainter.Antialiasing)
        # make a white drawing background
        paint.setBrush(Qt.white)
        paint.drawRect(event.rect())
        # for circle make the ellipse radii match
        radx = 100
        rady = 100
        # draw red circles
        paint.setPen(Qt.red)
        #for k in range(125, 220, 10):
       # center = QPoint(k, k)
        # optionally fill each circle yellow
        paint.setBrush(Qt.yellow)
        paint.drawEllipse(QPoint(250,250), radx, rady)
        paint.end()


        paint.drawRects()

class Simple_drawing_window2(QWidget):

    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Drawing")
        self.setGeometry(300, 300, 350, 350)
        self.setWindowTitle('Draw circles')
    def paintEvent(self, event):
        paint = QPainter()
        paint.begin(self)
        # optional
        paint.setRenderHint(QPainter.Antialiasing)
        # make a white drawing background
        paint.setBrush(Qt.white)
        paint.drawRect(event.rect())
        # for circle make the ellipse radii match
        radx = 100
        rady = 100
        # draw red circles
        paint.setPen(Qt.red)
        #for k in range(125, 220, 10):
       # center = QPoint(k, k)
        # optionally fill each circle yellow
        paint.setPen(Qt.yellow)
        paint.drawRects(50,50,200,200)

        paint.end()


        


class Simple_drawing_window(QWidget):

    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Drawing")
        self.rabbit = QImage("images/rabbit.png")

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(0, 0, 0))
        p.setBrush(QColor(255,127,0 ))
        p.drawPolygon([QPoint(70,100), QPoint(100,110),
                       QPoint(130,100), QPoint(100,150),])
        p.setPen(QColor(255,120,0))
        p.setBrush(QColor(255,127,0))
        p.drawPie(50,150,100,100,0,180*16)

        p.drawPolygon([QPoint(50,200), QPoint(150,200), QPoint(100,400)])
        p.drawImage(QRect(200,100,320,320), self.rabbit)
        p.end()



def main():
    app = QApplication(sys.argv)

    w = Simple_drawing_window2()
    w.show()

    return app.exec_()
if __name__ == "__main__":
    sys.exit(main())