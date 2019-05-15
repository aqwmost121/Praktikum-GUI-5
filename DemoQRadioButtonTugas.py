import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
class MainForm(QWidget):
     def __init__(self):
         super().__init__()
         self.setupUi()

     def setupUi(self):
         self.resize(400, 150)
         self.move(300, 300)
         self.setWindowTitle('Demo QRadioButton')

         self.nameLabel = QLabel(self)
         self.nameLabel.setText('Bilangan Pertama')
         self.line = QLineEdit(self)

         self.line.move(130, 22)
         self.line.resize(250, 24)
         self.nameLabel.move(20, 20)

         self.nameLabel2 = QLabel(self)
         self.nameLabel2.setText('Bilangan Kedua')
         self.line2 = QLineEdit(self)

         self.line2.move(130, 62)
         self.line2.resize(250, 24)
         self.nameLabel2.move(20, 60)

         self.label1 = QLabel()
         self.label1.setText('')

         self.label2 = QLabel()
         self.label2.setText('')

         self.label3 = QLabel()
         self.label3.setText('')

         self.label4 = QLabel()
         self.label4.setText('')

         self.label5 = QLabel()
         self.label5.setText('')

         self.label6 = QLabel()
         self.label6.setText('')

         self.cekCondro = QRadioButton(self)
         self.cekCondro.setText('&Tambah')
         self.cekCondro.setChecked(True)
         self.cekCondro.move(20, 102)



         self.cekVanda = QRadioButton(self)
         self.cekVanda.setText('&Kurang')
         self.cekVanda.move(100, 102)

         self.cekFandi = QRadioButton(self)
         self.cekFandi.setText('&Kali')
         self.cekFandi.move(190, 102)

         self.cekGita = QRadioButton(self)
         self.cekGita.setText('&Bagi')
         self.cekGita.move(250, 102)

         vbox = QVBoxLayout()
         vbox.addWidget(self.label1)
         vbox.addWidget(self.label2)
         vbox.addWidget(self.label3)
         vbox.addWidget(self.label4)
         vbox.addWidget(self.label5)
         vbox.addWidget(self.label6)


         self.resultLabel = QLabel('Hasil Pembagian : ')
         self.checkButton = QPushButton('Hitung')

         layout = QVBoxLayout()
         layout.addLayout(vbox)
         layout.addWidget(self.resultLabel)
         layout.addWidget(self.checkButton)
         layout.addStretch()
         self.setLayout(layout)

         self.checkButton.clicked.connect(self.checkButtonClick)
     def checkButtonClick(self):
         if self.cekCondro.isChecked():
             self.resultLabel.setText('line+line2')


         else:
             self.resultLabel.setText('')

if __name__ == '__main__':
     a = QApplication(sys.argv)

     form = MainForm()
     form.show()

     a.exec_()
