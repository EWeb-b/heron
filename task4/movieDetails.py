from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
import json
filmData = [
    {
        "id": 1,
        "film_certificate_id": 3,
        "film_blurb": "Entering dreams.",
        "film_director": "Christopher Nolan",
        "film_name": "Inception",
        "film_actor": "Leonardo DiCaprio"
    },
    {
        "id": 2,
        "film_certificate_id": 3,
        "film_blurb": "Home alone, but on mars.",
        "film_director": "Ridley Scott",
        "film_name": "The Martian",
        "film_actor": "Matt Damon"
    },
    {
        "id": 3,
        "film_certificate_id": 3,
        "film_blurb": "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival",
        "film_director": "Christopher Nolan",
        "film_name": "Interstellar",
        "film_actor": "Matthew McConaughey"
    },
    {
        "id": 4,
        "film_certificate_id": 2,
        "film_blurb": "Peruvain Bear up to no good",
        "film_director": "Paul King",
        "film_name": "Paddington 2",
        "film_actor": "Ben Wishaw"
    },
    {
        "id": 5,
        "film_certificate_id": 4,
        "film_blurb": "Fishman seduces silent woman",
        "film_director": "Guillermo del Toro",
        "film_name": "The Shape of Water",
        "film_actor": "Sally Hawkins"
    },
    {
        "id": 6,
        "film_certificate_id": 3,
        "film_blurb": "superhero movie",
        "film_director": "Ryan Coogler",
        "film_name": "Black Panther",
        "film_actor": "Chadwick Boseman"
    },
    {
        "id": 7,
        "film_certificate_id": 2,
        "film_blurb": "P. T. Barnum is a man with little more than ambition to his name. When the company he works for goes bust, he decides to leave his mediocre life behind, and takes his family on a journey that would lead to establishing the foundations of showbusiness.",
        "film_director": "Michael Gracey",
        "film_name": "The Greatest  Showman",
        "film_actor": "Hugh Jackman"
    },
    {
        "id": 8,
        "film_certificate_id": 3,
        "film_blurb": "Horrible remake",
        "film_director": "Jake Kasden",
        "film_name": "Jumanji: Welcome to the jungle",
        "film_actor": "Dwayne Johnson"
    },
    {
        "id": 9,
        "film_certificate_id": 1,
        "film_blurb": "Undead reconcilliation",
        "film_director": "Lee Unkrich",
        "film_name": "CoCo",
        "film_actor": "Anthony Gonzalez"
    }
]

def parse_json(film_data, film):
    # this function is designed to parse the json data so that Example.detailWindow can display the correct info

    raw_info = list(filter(lambda person: person['film_name'] == film, filmData)) #returns list of movie
    # print(raw_info)
    director = raw_info[0]['film_director']
    actor = raw_info[0]['film_actor']
    blurb = raw_info[0]['film_blurb']
    certificate = raw_info[0]['film_certificate_id']



    return film, director,actor,blurb,certificate

print(parse_json(filmData,"CoCo"))

class Example(QWidget):

    def __init__(self):
        super().__init__()
        data = parse_json(filmData,"CoCo")
        # unravel tuple to input argument
        film = data[0]
        director = data[1]
        actor = data[2]
        blurb = data[3]
        certificate = data[4]

        detailWindow(self,film,director,actor,blurb,certificate)



def detailWindow(self,title,director,actor,blurb,certificate):
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

    blurbLabel = QLabel()
    blurbLabel.setText('Blurb: '+blurb)
    blurbLabel.setStyleSheet('font-weight: bold; font-size: 20px;')

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
    details.addWidget(blurbLabel)
    hbox.addWidget(poster)

    vbox = QVBoxLayout()
    vbox.addWidget(titleLabel)
    vbox.addLayout(hbox)
    vbox.addWidget(closeButton)
    self.setLayout(vbox)

    # self.setGeometry(300, 300, 300, 150)
    # self.setWindowTitle('Buttons')
    self.show()
if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
