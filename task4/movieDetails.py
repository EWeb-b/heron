from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys

class Example(QWidget):

    def __init__(self):
        super().__init__()

        detailWindow(self,'Black Panther','Ryan Coogler','Chadwick Boseman')


    # def initUI(self):
    #     self.setWindowTitle('Black Panther')
    #     self.setWindowIcon(QIcon('heron2.png'))
    #     closeButton = QPushButton("Close")
    #
    #     title = QLabel()
    #     title.setText('Black Panther')
    #     title.setStyleSheet('font-weight: bold; font-size: 35px;')
    #
    #     director = QLabel()
    #     director.setText('Director: '+'Ryan Coogler')
    #     director.setStyleSheet('font-weight: bold; font-size: 20px;')
    #
    #     actor = QLabel()
    #     actor.setText('Lead Actor: '+'Chadwick Boseman')
    #     actor.setStyleSheet('font-weight: bold; font-size: 20px;')
    #
    #     # blurb = QLabel()
    #     # blurb.setText('Ryan Coogler')
    #     # blurb.setStyleSheet('font-weight: bold; font-size: 20px;')
    #
    #     poster = QLabel()
    #     poster.setPixmap(QPixmap('Black_Panther.jpg'))
    #
    #     hbox = QHBoxLayout()
    #     details = QVBoxLayout()
    #     hbox.addLayout(details)
    #
    #     details.addWidget(director)
    #     details.addWidget(actor)
    #     hbox.addWidget(poster)
    #
    #     vbox = QVBoxLayout()
    #     vbox.addWidget(title)
    #     vbox.addLayout(hbox)
    #     vbox.addWidget(closeButton)
    #     self.setLayout(vbox)
    #
    #     # self.setGeometry(300, 300, 300, 150)
    #     # self.setWindowTitle('Buttons')
    #     self.show()

def detailWindow(self,title,director,actor):
    self.setWindowTitle(title)
    self.setWindowIcon(QIcon('heron2.png'))
    closeButton = QPushButton("Close")
    closeButton.clicked.connect(self.close)

    titleLabel = QLabel()
    titleLabel.setText(title)
    titleLabel.setStyleSheet('font-weight: bold; font-size: 35px;')

    directorLabel = QLabel()
    directorLabel.setText('Director: '+director)
    directorLabel.setStyleSheet('font-weight: bold; font-size: 20px;')

    actorLabel = QLabel()
    actorLabel.setText('Lead Actor: '+actor)
    actorLabel.setStyleSheet('font-weight: bold; font-size: 20px;')

    # blurb = QLabel()
    # blurb.setText('Ryan Coogler')
    # blurb.setStyleSheet('font-weight: bold; font-size: 20px;')

    poster = QLabel()
    poster.setPixmap(QPixmap('Black_Panther.jpg'))

    hbox = QHBoxLayout()
    details = QVBoxLayout()
    hbox.addLayout(details)

    details.addWidget(directorLabel)
    details.addWidget(actorLabel)
    hbox.addWidget(poster)

    vbox = QVBoxLayout()
    vbox.addWidget(titleLabel)
    vbox.addLayout(hbox)
    vbox.addWidget(closeButton)
    self.setLayout(vbox)

    # self.setGeometry(300, 300, 300, 150)
    # self.setWindowTitle('Buttons')
    self.show()
# if __name__ == '__main__':
#
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())
