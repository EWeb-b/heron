from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys, os
import json
from PIL import Image
from weeklyBreakDown import *
import datetime
import dayDates
import requests


from matplotlib.backends.qt_compat import QtCore, QtWidgets, is_pyqt5

from matplotlib.backends.backend_qt5agg import (
    FigureCanvas, NavigationToolbar2QT as NavigationToolbar)

from matplotlib.figure import Figure

mov_det = ''

# listOfMovieNames = ['Black Panther', 'The Shape of Water', 'The Greatest Showman'] # To be changed to work with DB
# directorNames = ['Ryan Coogler','Guilermo del Toro']
# BPdaily = [['40','40','40'],['30','50','40'],['120','120','60'],['100','50','50'],['100','40','40'],['100','100','40'],['40','40','70']]
# BPtakings = ['120','120','300','200','180','240','150']
#
# SWdaily = [['40','40','40'],['30','50','40'],['120','120','60'],['100','50','50'],['100','40','40'],['100','100','40'],['40','40','70']]
# SWtakings = ['170','120','180','240','150','300','200']
#
# GSdaily = [['40','40','40'],['30','50','40'],['120','120','60'],['100','50','50'],['100','40','40'],['100','100','40'],['40','40','70']]
# GStakings = ['180','240','150','300','160','120','200']
#
# weekTakings = [BPtakings,SWtakings,GStakings]
#listOfMovieNames = ['Inception', 'The Martian', 'Interstellar','Paddington 2','The Shape of Water','Black Panther','The Greatest Showman','Jumanji: Welcome to the jungle','CoCo'] # To be changed to work with DB

INCdaily = [['40','40','40'],['30','50','40'],['120','120','60'],['100','50','50'],['100','40','40'],['100','100','40'],['40','40','70']]
INCtakings = ['120','120','300','200','180','240','150']

TMdaily = [['40','40','40'],['30','50','40'],['120','120','60'],['100','50','50'],['100','40','40'],['100','100','40'],['40','40','70']]
TMtakings = ['170','120','180','240','150','300','200']

INTdaily = [['40','40','40'],['30','50','40'],['120','120','60'],['100','50','50'],['100','40','40'],['100','100','40'],['40','40','70']]
INTtakings = ['180','240','150','300','160','120','200']

P2daily = [['40','40','40'],['30','50','40'],['120','120','60'],['100','50','50'],['100','40','40'],['100','100','40'],['40','40','70']]
P2takings = ['180','240','150','300','160','120','200']

SWdaily = [['40','40','40'],['30','50','40'],['120','120','60'],['100','50','50'],['100','40','40'],['100','100','40'],['40','40','70']]
SWtakings = ['180','240','150','300','160','120','200']

BPdaily = [['40','40','40'],['30','50','40'],['120','120','60'],['100','50','50'],['100','40','40'],['100','100','40'],['40','40','70']]
BPtakings = ['180','240','150','300','160','120','200']

GSdaily = [['40','40','40'],['30','50','40'],['120','120','60'],['100','50','50'],['100','40','40'],['100','100','40'],['40','40','70']]
GStakings = ['180','240','150','300','160','120','200']

JWJdaily = [['40','40','40'],['30','50','40'],['120','120','60'],['100','50','50'],['100','40','40'],['100','100','40'],['40','40','70']]
JWJtakings = ['180','240','150','300','160','120','200']

CCdaily = [['40','40','40'],['30','50','40'],['120','120','60'],['100','50','50'],['100','40','40'],['100','100','40'],['40','40','70']]
CCtakings = ['180','240','150','300','160','120','200']

weekTakings = [INCtakings,TMtakings,INTtakings,P2takings,SWtakings,BPtakings,GStakings,JWJtakings,CCtakings]

takings = ['1320', '1222', '950','4378','1320', '1222', '950','4378','46']
movieBuffer = []
timeSpan = 'daily'


takingsDate = datetime.date.today() #used to keep track of the week in


# filmData = requests.get("http://localhost:5000/api/films")

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
        "film_blurb": """A team of explorers travel through a wormhole in space
                            in an attempt to ensure humanity's survival""",
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
        "film_blurb": """P. T. Barnum is a man with little more than ambition to
                        his name. When the company he works for goes bust, he
                        decides to leave his mediocre life behind, and takes his
                        family on a journey that would lead to establishing the
                        foundations of showbusiness.""",
        "film_director": "Michael Gracey",
        "film_name": "The Greatest  Showman",
        "film_actor": "Hugh Jackman"
    },
    {
        "id": 8,
        "film_certificate_id": 3,
        "film_blurb": "Horrible remake",
        "film_director": "Jake Kasden",
        "film_name": "Jumanji: Welcome to the Jungle",
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

listOfMovieNames = []
for i in range(len(filmData)):
    listOfMovieNames.append(filmData[i]["film_name"])
print(listOfMovieNames)
def parse_json(film_data, film):
    # this function is designed to parse the json data so that Example.detailWindow can display the correct info

    raw_info = list(filter(lambda person: person["film_name"] == film, filmData)) #returns list of movie
    print('raw_info',raw_info)
    director = raw_info[0]['film_director']
    actor = raw_info[0]['film_actor']
    blurb = raw_info[0]['film_blurb']
    certificate = raw_info[0]['film_certificate_id']
    id = raw_info[0]['id']



    return film, director,actor,blurb,certificate,id

#print(parse_json(filmData,"The Greatest  Showman"))

class Details(QWidget):

    def __init__(self):
        super().__init__()
        #data = parse_json(filmData,mov_det)
        print('argument mov_det ==',mov_det)
        data = parse_json(filmData, mov_det) # this argument needs to come from button clicked in tabs2.py
        print('data!!!!!!!',data)
        # unravel tuple to input argument
        film = data[0]
        director = data[1]
        actor = data[2]
        blurb = data[3]
        certificate = data[4]
        id = data[5]

        detailWindow(self,film,director,actor,blurb,certificate,id)



def detailWindow(self,title,director,actor,blurb,certificate,id):
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
    script_dir = sys.path[0]
    #img_path = os.path.join(script_dir, '../webapp/app/static/portraits/' + title +'.jpg')
    # img_path = open('portraits/' + str(id) +'.jpg')
    #
    # print('img_path',img_path)

    # img = Image.open('./portraits/' + str(id) +'.png')
    # img.show()
    # print('type',type(img))
    poster.setPixmap(QPixmap('./portraits/' + str(id) +'.png'))

    hbox = QHBoxLayout()
    details = QVBoxLayout()
    hbox.addLayout(details)

    details.addWidget(titleLabel)
    details.addStretch()
    details.addWidget(directorLabel)
    details.addWidget(actorLabel)
    details.addWidget(blurbLabel)
    details.addStretch()
    hbox.addWidget(poster)

    vbox = QVBoxLayout()

    vbox.addLayout(hbox)
    vbox.addWidget(closeButton)
    self.setLayout(vbox)

    # self.setGeometry(300, 300, 300, 150)
    # self.setWindowTitle('Buttons')
    self.show()





class Takings(QScrollArea):
    def update_takings_tabe(self):
        print('update table!!!!')
        global dailyTOT
        for i in range(num_of_row-1):
            for j in range(num_of_col-1):
                self.tableWidget.setItem(i,j, QTableWidgetItem(weekTakings[i][j]))
                dailyTOT[j] += int(weekTakings[i][j])
            self.tableWidget.setItem(i,7, QTableWidgetItem(str(sum(map(int,weekTakings[i])))))

    def make_rank_button(self,button):
        return button.clicked.connect(lambda:self.display_info(button))

    def display_info(self,button):
        #print('INFO!!',button.text()[2:])

        global mov_det # global variable to be passed between Takings and Example classes
        mov_det = button.text()[3:]
        print('mov_det',mov_det)
        self.dialog = Details()

        self.dialog.show()


    trigger1 = pyqtSignal() # come back and delete this

    @pyqtSlot()
    def on_click(self):
        # for currentQTableWidgetItem in self.tableWidget.selectedItems():
        #     row = currentQTableWidgetItem.row()
        #     col = currentQTableWidgetItem.column()
        #     print("\n")
        #     print('hey:',row,col)

        for currentQTableWidgetItem in self.tableWidget.selectedItems():

            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())
            row = currentQTableWidgetItem.row()
            col = currentQTableWidgetItem.column()
            print('row',row,'col',col)
            #print('ahhh:',currentQTableWidgetItem.columnSpan(row,col))
            if col == 7 and row != 9:
                print('weekly total!')
                print(listOfMovieNames2[row])
                global mov_det # global variable to be passed between Takings and Example classes
                mov_det = listOfMovieNames2[row]
                print('mov_det',mov_det)
                self.dialog = Details()

                self.dialog.show()
                # self.dialog = Details()
                # self.dialog.show()
            elif row == 9 and col != 7: # needs to be changed to take len(rows)
                print('daily total!')
                # weeklyBAR('06/04/2018')

        # detapp = QApplication(sys.argv)
        # ex = Details()
        # ex.show()
        # sys.exit(detapp.exec_())

    # these next two functions connect to the next and previous buttons
    def previousweek(self):
        print('previous')
        global takingsDate
        self.next.setEnabled(True)
        takingsDate = takingsDate - datetime.timedelta(weeks = 1)
        self.date.setText(str(takingsDate))
        if takingsDate < datetime.date(2018,3,1):
            self.previous.setEnabled(False)
        print('week: ',takingsDate.isocalendar()[1])
        self.week.setText('Week: '+str(takingsDate.isocalendar()[1]))
        self.tableWidget.setHorizontalHeaderLabels(dayDates.dayDates(takingsDate))
        print(takingsDate)

        self.update_takings_tabe()



    def nextweek(self):

        print('next')
        global takingsDate
        takingsDate = takingsDate + datetime.timedelta(weeks = 1)
        self.date.setText(str(takingsDate))
        if self.previous.isEnabled():
            print('')
        else:
            self.previous.setEnabled(True)
        if takingsDate == datetime.date.today():
            self.next.setEnabled(False)

        print('week: ',takingsDate.isocalendar()[1])
        self.week.setText('Week: '+str(takingsDate.isocalendar()[1]))
        self.tableWidget.setHorizontalHeaderLabels(dayDates.dayDates(takingsDate))

        print(takingsDate)

        self.update_takings_tabe()


    # change to take takingsDate as an argument


    def createTable(self,rows,colums):
        #rows.append('Total')
        global num_of_col
        global num_of_row
        num_of_row = len(rows)
        num_of_col = len(colums)
       # Create table
        self.tableWidget = QTableWidget()

        self.tableWidget.setRowCount(num_of_row)
        self.tableWidget.setColumnCount(num_of_col)
        self.tableWidget.setVerticalHeaderLabels(rows)
        self.tableWidget.setHorizontalHeaderLabels(colums)
        rows = rows[:-1]
        print('rows',rows)
        #self.colum1 = self.tableWidget.horizontalHeaderItem(1)
        global dailyTOT
        dailyTOT = [0,0,0,0,0,0,0]

        for i in range(num_of_row-1):
            for j in range(num_of_col-1):
                self.tableWidget.setItem(i,j, QTableWidgetItem(weekTakings[i][j]))
                dailyTOT[j] += int(weekTakings[i][j])
            self.tableWidget.setItem(i,7, QTableWidgetItem(str(sum(map(int,weekTakings[i])))))

        #map(str,self.dailyTOT)
        #print('TOT:',self.dailyTOT)
        for i in range(7):
            self.tableWidget.setItem(9,i, QTableWidgetItem(str(dailyTOT[i])))
        # print('0,0:',self.mondayTot)
        #self.mondayTot.doubleClicked.connect(self.on_click)
        # table selection change
        self.tableWidget.doubleClicked.connect(self.on_click)
    def __init__(self):
        super(Takings, self).__init__()
        self.daysWeek = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']


        now = datetime.datetime.now()
        self.horizontal_headers = dayDates.dayDates(takingsDate)
        self.horizontal_headers.append('Total')

        self.vertical_headers = listOfMovieNames
        print('listOfMovieNames',listOfMovieNames)
        self.vertical_headers.append('Total')

        #print('HORIZONTAL HEADERS!!!!',horizontal_headers)
        self.createTable(listOfMovieNames,self.horizontal_headers)
        self.date = QLabel()
        self.date.setText(now.strftime("%d-%m-%Y"))
        self.date.setStyleSheet('font-size: 80px;')

        self.week = QLabel()
        self.week.setText('Week: '+str(now.isocalendar()[1]))
        self.week.setStyleSheet('font-size: 40px;')

        self.rankingLayout = QVBoxLayout()
        # self.num1 = QPushButton('#1')
        # self.rankingLayout.addWidget(self.num1)

        self.buttLayout = QHBoxLayout()
        self.previous = QPushButton('Previous')
        self.previous.clicked.connect(lambda:self.previousweek())

        self.next = QPushButton('Next')
        self.next.clicked.connect(lambda:self.nextweek())

        self.next.setEnabled(False)
        self.buttLayout.addWidget(self.previous)
        self.buttLayout.addWidget(self.next)


        self.layout = QHBoxLayout()
        self.weekTable = QVBoxLayout()
        self.weekTable.addWidget(self.date)
        self.weekTable.addWidget(self.week)
        self.weekTable.addWidget(self.tableWidget)
        self.weekTable.addLayout(self.buttLayout)


        self.rankingLayout = QVBoxLayout()
        self.ranktitle = QLabel('Overall Ranking')
        self.ranktitle.setStyleSheet('font-size: 50px;')
        self.revunetitle = QLabel('(revenue)')
        self.ranktitle.setStyleSheet('font-size: 30px;')


        self.rankingLayout.addWidget(self.ranktitle)
        self.rankingLayout.addWidget(self.revunetitle)

        print('listOfMovieNames!!!!!!!!!',listOfMovieNames)
        global listOfMovieNames2
        listOfMovieNames2 = listOfMovieNames[:-1]
        for i in range(len(listOfMovieNames2)):
            movie = 'movie'+str(i)
            print (movie)
            buttonTitle = '#'+str(i+1)+' '+listOfMovieNames2[i]
            self.movie = QPushButton(buttonTitle)

            self.make_rank_button(self.movie)
            self.rankingLayout.addWidget(self.movie)

        self.rankingLayout.addStretch()

        self.layout.addLayout(self.weekTable)
        self.layout.addLayout(self.rankingLayout)
        self.setLayout(self.layout)

class Compare(QScrollArea):


    def removeBuffer(self, button):
        print(button)
        print('Layout',self.bufferScrollLayout)

        button.setVisible(False)
        print( button.text())
        movieBuffer.remove(button.text())

        print(movieBuffer)

    def movie2Buffer(self,button):
        print(self.bufferScrollLayout)
        if button.text() not in movieBuffer:
            # color = self.random_color()
            # color_buffer.append(color)
            # print(color_buffer)
            #bufferNumber += 1
            # buff = 'buffer'+str(bufferNumber)
            movieBuffer.append(button.text())
            self.butt = QPushButton(button.text())
            self.butt.setStyleSheet('background-color: red; color: white;')
            self.make_buffer_button(self.butt)
            #self.butt.clicked.connect(lambda:self.removeBuffer(self.butt))
            self.bufferScrollLayout.addWidget(self.butt)
            self.butt.setVisible(True)
        print (movieBuffer)
    def make_buffer_button(self,button):
        return button.clicked.connect(lambda:self.removeBuffer(button))

    def make_movie_button(self,button):
        return button.clicked.connect(lambda:self.movie2Buffer(button))
    def selectDaily(self):
        timeSpan = 'daily'
        print (timeSpan+'\n')
    def selectWeeky(self):
        timeSpan = 'weekly'
        print (timeSpan+'\n')
    def selectOverall(self):
        timeSpan = 'overall'
        print (timeSpan+'\n')
    def compare(self):

        print('plot',movieBuffer,'for',timeSpan)
        bufferTakings = []
        for i in range(len(movieBuffer)):
            self.tableButton.setEnabled(True)
            index = listOfMovieNames2.index(movieBuffer[i])
            bufferTakings.append(takings[index])
        print(bufferTakings)
        print(movieBuffer)


        self._dynamic_ax.clear()
        self._dynamic_ax.pie(bufferTakings,labels = movieBuffer, autopct='%1.1f%%', shadow=False)
        dynamic_canvas.updateGeometry()
        # self.layout.update()

    def table(self):
        print('table')
    def __init__(self):
        super(Compare, self).__init__()

        # layout
        layout = QVBoxLayout()

        # heading text
        self.header = QLabel()
        self.header.setText('Select Movies to compare takings')
        layout.addWidget(self.header)

        self.movies_header = QLabel()
        self.movies_header.setText('Movies')
        self.movies_header.setStyleSheet('font-size: 40px;')

        self.buffer_header = QLabel()
        self.buffer_header.setText('Buffer')
        self.buffer_header.setStyleSheet('font-size: 40px;')

        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()

        vbox2 = QVBoxLayout()

        vbox2.addWidget(self.buffer_header)
        graphbox = QVBoxLayout()
        global dynamic_canvas
        dynamic_canvas = FigureCanvas(Figure(figsize=(5, 5)))
        self._dynamic_ax = dynamic_canvas.figure.subplots()
        self._dynamic_ax.pie([1],labels = [''], autopct='', shadow=False, colors = 'white')
        graphbox.addWidget(dynamic_canvas)

        #addToolBar(NavigationToolbar(dynamic_canvas, self))

        #self.img = QLabel()
        #self.img.setPixmap(QPixmap("takings.png"))
        #graphbox.addWidget(self.img)
        # check boxes
        self.daily = QRadioButton('daily')
        self.weekly = QRadioButton('weekly')
        self.overall = QRadioButton('overall')

        hbox1.addWidget(self.daily)
        hbox1.addStretch()
        hbox1.addWidget(self.weekly)
        hbox1.addStretch()
        hbox1.addWidget(self.overall)

        layout.addLayout(hbox1)

        self.daily.setChecked(True)
        self.daily.toggled.connect(lambda:self.selectDaily())
        self.weekly.toggled.connect(lambda:self.selectWeeky())
        self.overall.toggled.connect(lambda:self.selectOverall())

        # layout.addWidget(self.daily)
        # layout.addWidget(self.weekly)
        # layout.addWidget(self.overall)

        self.scrollTitle = QLabel('Movies')
        self.bufferTitle = QLabel('Buffer')

        self.movieScroll = QScrollArea()
        self.bufferScroll = QScrollArea()
        #self.movieScroll.setWidget(self.scrollTitle)

        self.movieScrollLayout = QVBoxLayout()
        self.movieScroll.setLayout(self.movieScrollLayout)

        self.bufferScrollLayout = QVBoxLayout()
        self.bufferScroll.setLayout(self.bufferScrollLayout)

        for i in range(len(listOfMovieNames2)):
            movie = 'movie'+str(i)
            print (movie)
            self.movie = QPushButton(listOfMovieNames2[i])
            self.movie.setStyleSheet('background-color: green; color: white')
            self.make_movie_button(self.movie)
            self.movieScrollLayout.addWidget(self.movie)
        self.movieScrollLayout.addStretch()

        self.compareButton = QPushButton('Compare (graphically)')
        self.compareButton.clicked.connect(lambda:self.compare())
        layout.addWidget(self.compareButton)

        self.tableButton = QPushButton('View Table')
        self.tableButton.clicked.connect(lambda:self.table())
        layout.addWidget(self.tableButton)
        self.tableButton.setEnabled(False)

        hbox2.addWidget(self.movieScroll)
        vbox2.addWidget(self.bufferScroll)
        vbox2.addLayout(graphbox)
        hbox2.addLayout(vbox2)
        #hbox2.addWidget(self.bufferScroll)
        layout.addLayout(hbox2)
        layout.addWidget(self.compareButton)
        self.setLayout(layout)
        #self.setWindowTitle("Choose movie tab")
class Settings(QScrollArea):
    def __init__(self):
        super(Settings, self).__init__()


        self.layout = QVBoxLayout()

        self.setLayout(self.layout)
def main():

    app 	= QApplication(sys.argv)
    tabs	= QTabWidget()
    app.setWindowIcon(QIcon('heron2.png'))
    # Create tabs
    tab1	= QWidget()
    tab2	= QWidget()
    tab3	= QWidget()

    # Resize width and height
    tabs.showMaximized()
    ta = Takings()
    vBoxlayout3	= QVBoxLayout()
    vBoxlayout3.addWidget(ta)
    tab1.setLayout(vBoxlayout3)

    ex = Compare()
    vBoxlayout2	= QVBoxLayout()
    vBoxlayout2.addWidget(ex)
    tab2.setLayout(vBoxlayout2)



    # Add tabs
    tabs.addTab(tab1,"Takings")
    tabs.addTab(tab2,"Compare movies")
    tabs.addTab(tab3, "Settings")
    # Set title and show
    tabs.setWindowTitle('Manager app')
    tabs.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
