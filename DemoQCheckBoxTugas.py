import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
class MainForm(QWidget):
     def __init__(self):
         super().__init__()
         self.setupUi()

     def setupUi(self):
         self.resize(400, 400)
         self.move(300, 300)
         self.setWindowTitle('')



         self.javaCheck = QCheckBox()
         self.javaCheck.setText('Show Title')

         hbox1 = QHBoxLayout()
         hbox1.addWidget(self.javaCheck)

         layout = QVBoxLayout()
         layout.addLayout(hbox1)
         horizontalLine = QFrame();
         horizontalLine.setFrameShape(QFrame.HLine)
         horizontalLine.setFrameShadow(QFrame.Sunken)

         layout.addStretch()
         self.setLayout(layout)

         self.javaCheck.clicked.connect(self.javaCheckClick)

     def javaCheckClick(self):
         if self.javaCheck.isChecked(): self.setWindowTitle('Contoh QCheckBox')

if __name__ == '__main__':
    a = QApplication(sys.argv)

    form = MainForm()
    form.show()

    a.exec_()
