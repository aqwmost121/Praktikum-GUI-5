import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
class MainForm(QWidget):
     def __init__(self):
         super().__init__()
         self.setupUi()

     def setupUi(self):
         self.resize(400, 200)
         self.move(300, 300)
         self.setWindowTitle('Penggunaan QTextEdit')

         self.label1 = QLabel()
         self.label1.setText('Dari')
         self.dari = QLineEdit()

         vbox1 = QVBoxLayout()
         vbox1.addWidget(self.label1)
         vbox1.addWidget(self.dari)

         self.label3 = QLabel()
         self.label3.setText('Untuk')
         self.untuk = QLineEdit()
         vbox4 = QVBoxLayout()
         vbox4.addWidget(self.label3)
         vbox4.addWidget(self.untuk)

         self.label2 = QLabel()
         self.label2.setText('Pesan')
         self.messageEdit = QTextEdit()
         vbox2 = QVBoxLayout()
         vbox2.addWidget(self.label2)
         vbox2.addWidget(self.messageEdit)

         vbox3 = QVBoxLayout()
         vbox3.addLayout(vbox1)
         vbox3.addLayout(vbox4)
         vbox3.addLayout(vbox2)

         self.sendButton = QPushButton('&Kirim SMS')
         self.cancelButton = QPushButton('&Batal')
         hbox = QHBoxLayout()
         hbox.addStretch()
         hbox.addWidget(self.sendButton)
         hbox.addWidget(self.cancelButton)

         layout = QVBoxLayout()
         layout.addLayout(vbox3)
         verticalLine = QFrame();
         verticalLine.setFrameShape(QFrame.VLine)
         verticalLine.setFrameShadow(QFrame.Sunken)
         layout.addWidget(verticalLine)
         layout.addLayout(hbox)
         self.setLayout(layout)
if __name__ == '__main__':
     a = QApplication(sys.argv)

     form = MainForm()
     form.show()

     a.exec_()
