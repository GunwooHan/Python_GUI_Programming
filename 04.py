import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip
from PyQt5.QtGui import QFont

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('NanumGothic',10))
        self.setToolTip('this is a <b>QWidget</b> widget, 이건 Qwidget입니다')

        btn = QPushButton   ('Button', self)
        btn.setToolTip('This is a <b> QPushButton</b> widget')
        btn.move(50,50)
        btn.resize(btn.sizeHint())
        
        self.setWindowTitle('Tooltips')
        self.setGeometry(300,300,300,200)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())