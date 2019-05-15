import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
class DemoIcon(QWidget):
     def __init__(self):
         super().__init__()
         self.setupUi()

     def setupUi(self):
         self.resize(400, 100)
         self.move(300, 300)
         self.setWindowTitle('Tugas Menyisipkan Icon')

         self.label = QLabel()
         self.label.setText('<b>Bahasa Pemrograman Favorit Anda<b>')

         icon1 = QIcon('python.png')
         self.button1 = QPushButton('\tPython')
         self.button1.setIcon(icon1)

         icon2 = QIcon('java.png')
         self.button2 = QPushButton('\tJava')
         self.button2.setIcon(icon2)


         icon3 = QIcon('php.png')
         self.button3 = QPushButton('\tPhp')
         self.button3.setIcon(icon3)

         icon4 = QIcon('c-plus-plus.png')
         self.button4 = QPushButton('\tC/C++')
         self.button4.setIcon(icon4)

         hbox = QHBoxLayout()
         hbox.addWidget(self.button1)
         hbox.addWidget(self.button2)

         hhbox = QHBoxLayout()
         hhbox.addWidget(self.button3)
         hhbox.addWidget(self.button4)

         layout = QVBoxLayout()
         layout.addWidget(self.label)
         layout.addLayout(hbox)
         layout.addLayout(hhbox)
         self.setLayout(layout)
if __name__ == '__main__':
     a = QApplication(sys.argv)

     form = DemoIcon()
     form.show()

     a.exec_()
