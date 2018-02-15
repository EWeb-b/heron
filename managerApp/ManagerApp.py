import sys
import requests
from PyQt5.QtWidgets import (
    QWidget, QPushButton, QHBoxLayout, QComboBox,
    QVBoxLayout, QApplication, QMainWindow)
from PyQt5.QtCore import pyqtSlot


server = 'http://localhost:5000'


class ManagerApp(QMainWindow):

    def __init__(self):
        super(ManagerApp, self).__init__()
        self.setUpUi()

    @pyqtSlot()
    def downloadMovies(self):
        self.movieData = requests.get(server + '/api/movies').json()
        self.movieCombo.addItems(
            [movie['film_name'] for movie in self.movieData['films']])

    def setUpUi(self):
        mainLayout = QVBoxLayout()
        upperBox = QHBoxLayout()
        midBox = QHBoxLayout()
        lowBox = QHBoxLayout()

        self.movieCombo = QComboBox()

        updatebtn = QPushButton("Update")
        updatebtn.clicked.connect(self.downloadMovies)
        upperBox.addWidget(self.movieCombo)
        upperBox.addWidget(updatebtn)

        mainLayout.addLayout(upperBox)
        mainLayout.addLayout(midBox)
        mainLayout.addLayout(lowBox)

        widget = QWidget()
        self.setCentralWidget(widget)
        widget.setLayout(mainLayout)

        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle('Cinema Management Tool')
        self.show()

app = QApplication(sys.argv)
GUI = ManagerApp()
sys.exit(app.exec_())
