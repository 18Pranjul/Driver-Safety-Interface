
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-10, -20, 881, 591))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(640, 510, 121, 41))
        font = QtGui.QFont()
        font.setFamily("URW Bookman L")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton.setObjectName("pushButton")
        self.listWidget = QtWidgets.QListWidget(self.frame)
        self.listWidget.setGeometry(QtCore.QRect(20, 40, 256, 41))
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Chilanka")
        font.setPointSize(22)
        font.setItalic(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.Dense6Pattern)
        item.setBackground(brush)
        self.listWidget.addItem(item)
        self.listWidget_2 = QtWidgets.QListWidget(self.frame)
        self.listWidget_2.setGeometry(QtCore.QRect(150, 80, 256, 151))
        self.listWidget_2.setObjectName("listWidget_2")
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("URW Chancery L")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 255))
        brush.setStyle(QtCore.Qt.FDiagPattern)
        item.setBackground(brush)
        self.listWidget_2.addItem(item)
        self.listWidget_3 = QtWidgets.QListWidget(self.frame)
        self.listWidget_3.setGeometry(QtCore.QRect(20, 260, 256, 41))
        self.listWidget_3.setObjectName("listWidget_3")
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Chilanka")
        font.setPointSize(24)
        font.setItalic(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 255))
        brush.setStyle(QtCore.Qt.Dense6Pattern)
        item.setBackground(brush)
        self.listWidget_3.addItem(item)
        self.listWidget_4 = QtWidgets.QListWidget(self.frame)
        self.listWidget_4.setGeometry(QtCore.QRect(110, 300, 291, 211))
        self.listWidget_4.setObjectName("listWidget_4")
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("URW Chancery L")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 127))
        brush.setStyle(QtCore.Qt.FDiagPattern)
        item.setBackground(brush)
        self.listWidget_4.addItem(item)
        self.listWidget_5 = QtWidgets.QListWidget(self.frame)
        self.listWidget_5.setGeometry(QtCore.QRect(440, 260, 256, 41))
        self.listWidget_5.setObjectName("listWidget_5")
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Chilanka")
        font.setPointSize(22)
        font.setItalic(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 255))
        brush.setStyle(QtCore.Qt.Dense6Pattern)
        item.setBackground(brush)
        self.listWidget_5.addItem(item)
        self.listWidget_6 = QtWidgets.QListWidget(self.frame)
        self.listWidget_6.setGeometry(QtCore.QRect(430, 40, 261, 41))
        self.listWidget_6.setObjectName("listWidget_6")
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Chilanka")
        font.setPointSize(22)
        font.setItalic(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 255))
        brush.setStyle(QtCore.Qt.Dense6Pattern)
        item.setBackground(brush)
        self.listWidget_6.addItem(item)
        self.listWidget_7 = QtWidgets.QListWidget(self.frame)
        self.listWidget_7.setGeometry(QtCore.QRect(480, 80, 281, 91))
        self.listWidget_7.setObjectName("listWidget_7")
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("URW Chancery L")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 127))
        brush.setStyle(QtCore.Qt.FDiagPattern)
        item.setBackground(brush)
        self.listWidget_7.addItem(item)
        self.listWidget_8 = QtWidgets.QListWidget(self.frame)
        self.listWidget_8.setGeometry(QtCore.QRect(480, 300, 301, 181))
        self.listWidget_8.setObjectName("listWidget_8")
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("URW Chancery L")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        brush.setStyle(QtCore.Qt.FDiagPattern)
        item.setBackground(brush)
        self.listWidget_8.addItem(item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.pushButton.clicked.connect(self.quit)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Help"))
        self.pushButton.setText(_translate("MainWindow", "Close"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "Technology Used:"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        item = self.listWidget_2.item(0)
        item.setText(_translate("MainWindow", "Python\n"
"Image processing\n"
"Machine learning\n"
"Deep learning \n"
""))
        self.listWidget_2.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.listWidget_3.isSortingEnabled()
        self.listWidget_3.setSortingEnabled(False)
        item = self.listWidget_3.item(0)
        item.setText(_translate("MainWindow", "Features:"))
        self.listWidget_3.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.listWidget_4.isSortingEnabled()
        self.listWidget_4.setSortingEnabled(False)
        item = self.listWidget_4.item(0)
        item.setText(_translate("MainWindow", "Factors that our program takes into\n"
"consideration include, the usage of a\n"
"mobile phone, eating and drinking,\n"
"conversation with co-passengers,\n"
"self-grooming, reading or watching\n"
"videos and adjusting the radio or\n"
"music player."))
        self.listWidget_4.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.listWidget_5.isSortingEnabled()
        self.listWidget_5.setSortingEnabled(False)
        item = self.listWidget_5.item(0)
        item.setText(_translate("MainWindow", "Working"))
        self.listWidget_5.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.listWidget_6.isSortingEnabled()
        self.listWidget_6.setSortingEnabled(False)
        item = self.listWidget_6.item(0)
        item.setText(_translate("MainWindow", "Data Set:"))
        self.listWidget_6.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.listWidget_7.isSortingEnabled()
        self.listWidget_7.setSortingEnabled(False)
        item = self.listWidget_7.item(0)
        item.setText(_translate("MainWindow", "Since, creating our own data set\n"
"would be a tough task, we prefer a\n"
"pre-developed data set."))
        self.listWidget_7.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.listWidget_8.isSortingEnabled()
        self.listWidget_8.setSortingEnabled(False)
        item = self.listWidget_8.item(0)
        item.setText(_translate("MainWindow", "While driving, the driver\'s behaviour\n"
"is continuously monitored through\n"
"2-D pictures clicked by a camera\n"
"placed on the dashboard, and the\n"
"driver is immediately notified if\n"
"he/she is found to be distracted."))
        self.listWidget_8.setSortingEnabled(__sortingEnabled)

    def quit(self):
        sys.exit()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

