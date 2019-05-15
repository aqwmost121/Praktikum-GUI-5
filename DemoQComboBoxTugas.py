import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
class MainForm(QWidget):
     def __init__(self):
         super().__init__()
         self.setupUi()

     def setupUi(self):
         self.resize(300, 100)
         self.move(300, 300)
         self.setWindowTitle('Demo QComboBox')

         self.combo = QComboBox()
         for i in range(1):
             self.combo.addItem('--Pilih Makanan-- ' )
             self.combo.addItem('Mendoan' )
             self.combo.addItem('Cireng ' )
             self.combo.addItem('Gethuk ' )
             self.combo.addItem('Tahu Bulat ' )
             self.combo.addItem('Ketan Susu ' )

         self.combo2 = QComboBox()
         for i in range(1):
             self.combo2.addItem('--Pilih Minuman-- ' )
             self.combo2.addItem('Es Cincau ' )
             self.combo2.addItem('Milk Shake ' )
             self.combo2.addItem('Chat Time ' )
             self.combo2.addItem('Thai Tea ' )
             self.combo2.addItem('Kopi Hitam ' )

         self.getTextButton = QPushButton('Ambil Teks')

         layout = QVBoxLayout()
         layout.addWidget(self.combo)
         layout.addWidget(self.combo2)
         layout.addWidget(self.getTextButton)
         layout.addStretch()
         self.setLayout(layout)

         self.getTextButton.clicked.connect(self.getTextButtonClick)

     def getTextButtonClick(self):
         QMessageBox.information(self, 'Informasi',
         'Anda memilih: ' + self.combo.currentText()+' & '+ self.combo2.currentText())
if __name__ == '__main__':
     a = QApplication(sys.argv)

     form = MainForm()
     form.show()

     a.exec_()
