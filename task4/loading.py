from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    w = QDialog()
    w.setWindowFlags(Qt.Popup)
    w.setAttribute(Qt.WA_QuitOnClose)

    movie = QMovie("loading.gif") # QMovie takes name of .gif

    w.show()
    w.raise_()
    sys.exit(app.exec_())
