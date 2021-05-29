import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def  initUI(self):
        lbl_red = QLabel('Red')

        lbl_red.setStyleSheet(
            'color: red;'
            "border-style: solid;"
            'border-width: 2px;'
            'border-color: #FA8072;'
            'border-radius: 3px;')

        vbox = QVBoxLayout()
        vbox.addWidget(lbl_red)
    
        self.setLayout(vbox)
        
        self.setWindowTitle('Stylesheet')
        self.setGeometry(300,300,300,200)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())