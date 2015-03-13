#from PySide.QtCore import *
#from PySide.QtGui import *
     
#SCREEN_BORDER = 100
     
#class GraphicsView(QGraphicsView):
#    def __init__(self, parent=None):
#        super(GraphicsView, self).__init__(parent)
     
     
#class MouseCoordinates(QLabel):
     
#    def __init__(self, parent=None):
#        super(MouseCoordinates, self).__init__(parent)
        
#        self.update()
     
#    def update(self):
     
#        currentPos = QCursor.pos()
     
#        x = currentPos.x()
#        y = currentPos.y()
     
#        self.setText(" Mouse: %d / %d " % (x, y))
     
#class StatusBar(QStatusBar):
     
#    def __init__(self, parent=None):
#        super(StatusBar, self).__init__(parent)
     
#        self.mouseCoords = MouseCoordinates()
     
#        self.addWidget(self.mouseCoords)
     
#        self.update()
     
#    def update(self):
     
#        self.mouseCoords.update()
     
     
#class MainWindow(QMainWindow):
     
#    def __init__(self, parent=None):
#        super(MainWindow, self).__init__(parent)
#        self.setMouseTracking(True)
#        self.scene = QGraphicsScene(self)
#        self.scene.setSceneRect(QRectF(0, 0, 800, 600))
     
#        # draw border
#        self.scene.addRect(QRectF(0, 0, 800, 600),
#        QPen(Qt.darkGray, 1, Qt.DotLine),
#        QBrush(Qt.lightGray))
     
#        # save the current rect as parent object (canvas) for drawing
#        self.canvas = self.scene.items()[0]
     
     
#        # add view
#        self.view = GraphicsView()
#        self.view.setScene(self.scene)
     
#        self.status = StatusBar()
#        if self.status.isSizeGripEnabled():
#            self.status.setSizeGripEnabled(False)
     
#        self.setStatusBar(self.status)
     
#        self.setCentralWidget(self.view)
     
     
#    def mouseMoveEvent(self, event):
#        self.status.update()
#        super(MainWindow, self).mouseMoveEvent(event)
     
#if __name__ == "__main__":
     
#    import sys
     
#    # setup application object
#    app = QApplication(sys.argv)
     
#    # create (parent) main window
#    mainWindow = MainWindow()
#    rect = QApplication.desktop().availableGeometry()
#    mainWindow.setGeometry(rect.x() + SCREEN_BORDER,
#    rect.y() + SCREEN_BORDER,
#    rect.width() - 2 * SCREEN_BORDER,
#    rect.height() - 2 * SCREEN_BORDER)
#    mainWindow.setMinimumSize(900, 700)
#    mainWindow.setWindowIcon(QIcon("Icon.bmp"))
#    mainWindow.setWindowTitle("DesignerTest")
#    mainWindow.show()
     
#    # run application object
#    sys.exit(app.exec_())
from PySide.QtCore import *
from PySide.QtGui import *
import sys

class CharsetCanvas(QCanvas):

    def __init__(self, parent, font, start, end, maxW, *args):
        apply(QCanvas.__init__,(self, ) + args)
        self.parent=parent
        self.start=start
        self.end=end
        self.font=font
        self.drawTable(maxW)

    def drawTable(self, maxW):
        self.maxW=maxW
        self.items=[]
        x=0
        y=0

        fontMetrics=QFontMetrics(self.font)
        cell_width=fontMetrics.maxWidth() + 3
        if self.maxW < 16 * cell_width:
            self.maxW = 16 * cell_width
        cell_height=fontMetrics.lineSpacing()

        for wch in range(self.start, self.end + 1):
            item=QCanvasText(QString(QChar(wch)),self)
            item.setFont(self.font)

            item.setX(x)
            item.setY(y)
            item.show()

            self.items.append(item)

            x=x + cell_width
            if x >= self.maxW:
                x=0
                y=y+cell_height

        if self.parent.height() > y + cell_height:
            h = self.parent.height()
        else:
            h = y + cell_height

        self.resize(self.maxW + 20, h)
        self.update()

    def setFont(self, font):
        self.font=font
        self.drawTable(self.maxW)