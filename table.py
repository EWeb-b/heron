import sys
from PyQt5.QtWidgets import QTableWidget, QApplication, QMainWindow, QTableWidgetItem


class MyTable(QTableWidget):
    def __init__(self, r, c):
        super().__init__(r, c)
        #self.showMaximised()
        self.init_ui()

    def init_ui(self):
        self.cellChanged.connect(self.c_current)
        self.show()

    def c_current(self):
        row = self.currentRow()
        col = self.currentColumn()
        value = self.item(row, col)
        value = value.text()
        print("The current cell is ", row, ", ", col)
        print("In this cell we have: ", value)



class Sheet(QMainWindow):
    def __init__(self):
        super().__init__()

        self.form_widget = MyTable(5, 8)
        self.setCentralWidget(self.form_widget)
        col_headers = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday','Total']
        self.form_widget.setHorizontalHeaderLabels(col_headers)

        ver_headers = ['MovieA','MovieB','MovieC','MovieD','Other']
        self.form_widget.setVerticalHeaderLabels(ver_headers)
        # MovieA = [200,220,210,200,280,340,320]
        # number = QTableWidgetItem('10')
        # self.form_widget.setCurrentCell(1, 1)
        # self.form_widget.setItem(1, 1, number)

        self.show()

app = QApplication(sys.argv)
sheet = Sheet()
sys.exit(app.exec_())
