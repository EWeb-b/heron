import sys
import requests
from PyQt5.QtWidgets import (
    QWidget, QPushButton, QHBoxLayout, QComboBox, QLabel,
    QVBoxLayout, QApplication, QMainWindow)


server = 'http://localhost:5000'


class ManagerApp(QMainWindow):

    def __init__(self):
        super(ManagerApp, self).__init__()
        self.setUpUi()

    def downloadMovies(self):
        self.movieCombo.clear()
        self.movieData = requests.get(server + '/api/movies').json()['films']
        self.movieCombo.addItems(
            [movie['film_name'] for movie in self.movieData])
        self.movieLbl.setText(self.movieData[0]['blurb'])

    def movieComboUpdate(self, str):
        data = next(
            (movie for movie in self.movieData
                if movie['film_name'] == str), None)
        self.movieLbl.setText(data['blurb'])

    def setUpUi(self):
        # Layouts
        mainLayout = QVBoxLayout()
        upperBox = QHBoxLayout()
        midBox = QHBoxLayout()
        lowBox = QHBoxLayout()
        mainLayout.addLayout(upperBox)
        mainLayout.addLayout(midBox)
        mainLayout.addLayout(lowBox)

        # Combobox for the movie names
        self.movieCombo = QComboBox()
        self.movieCombo.activated[str].connect(self.movieComboUpdate)

        # updateBtn downloads data from the server
        updateBtn = QPushButton("Update")
        updateBtn.clicked.connect(self.downloadMovies)
        upperBox.addWidget(self.movieCombo)
        upperBox.addWidget(updateBtn)

        # Lable to display the blurb info
        self.movieLbl = QLabel()
        midBox.addWidget(self.movieLbl)

        # QMainWindow needs a widget to add a layout to
        widget = QWidget()
        self.setCentralWidget(widget)
        widget.setLayout(mainLayout)

        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle('Cinema Management Tool')
        self.show()


app = QApplication(sys.argv)
GUI = ManagerApp()
sys.exit(app.exec_())
