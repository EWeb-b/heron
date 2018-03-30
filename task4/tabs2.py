from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
import random
from pie import *

from matplotlib.backends.qt_compat import QtCore, QtWidgets, is_pyqt5
if is_pyqt5():
    from matplotlib.backends.backend_qt5agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
else:
    from matplotlib.backends.backend_qt4agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure

listOfMovieNames = ['Black Panther', 'The Sound of Water', 'The Greatest Showman'] # To be changed to work with DB
BPtakings = ['100','120','300']
takings = ['1320', '1222', '950']
movieBuffer = []
timeSpan = 'daily'
# global bufferNumber
# bufferNumber = 0

color_buffer = []

class Compare(QScrollArea):
    # def random_color(self):
    #     levels = range(32,256,32)
    #     return tuple(random.choice(levels) for _ in range(3))

    def removeBuffer(self, button):
        print(button)
        print('Layout',self.bufferScrollLayout)
        #self.bufferScrollLayout.removeWidget(button)
        #button.setParent(None)
        button.setVisible(False)
        print( button.text())
        movieBuffer.remove(button.text())
        #color_buffer.remove()
        # def __str__(self):
        #     return "name"
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
            index = listOfMovieNames.index(movieBuffer[i])
            bufferTakings.append(takings[index])
        print(bufferTakings)
        print(movieBuffer)
        print(color_buffer)
        self._dynamic_ax.clear()
        self._dynamic_ax.pie(bufferTakings,labels = movieBuffer, autopct='%1.1f%%', shadow=False)
        #pie_plot_week(movieBuffer,bufferTakings)
        #color_buffer = []
        #self.img.setPixmap(QPixmap("takings.png"))

        #pie_plot_week(movieBuffer,takings)
    def __init__(self):
        super(Compare, self).__init__()

        # layout
        layout = QVBoxLayout()

        # heading text
        self.header = QLabel()
        self.header.setText('Select Movies to compare takings')
        layout.addWidget(self.header)

        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()

        vbox2 = QVBoxLayout()
        graphbox = QVBoxLayout()

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

        for i in range(len(listOfMovieNames)):
            movie = 'movie'+str(i)
            print (movie)
            self.movie = QPushButton(listOfMovieNames[i])
            self.movie.setStyleSheet('background-color: green; color: white')
            self.make_movie_button(self.movie)
            self.movieScrollLayout.addWidget(self.movie)

        self.compareButton = QPushButton('Compare')
        self.compareButton.clicked.connect(lambda:self.compare())
        layout.addWidget(self.compareButton)

        hbox2.addWidget(self.movieScroll)
        vbox2.addWidget(self.bufferScroll)
        vbox2.addLayout(graphbox)
        hbox2.addLayout(vbox2)
        #hbox2.addWidget(self.bufferScroll)
        layout.addLayout(hbox2)
        layout.addWidget(self.compareButton)
        self.setLayout(layout)
        self.setWindowTitle("Choose movie tab")
class Settings(QScrollArea):
    hey = 1
def main():

    app 	= QApplication(sys.argv)
    tabs	= QTabWidget()

    # Create tabs
    tab1	= QWidget()
    tab2	= QWidget()
    tab3	= QWidget()
    tab4	= QWidget()

    # Resize width and height
    tabs.showMaximized()

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
