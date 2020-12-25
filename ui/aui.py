

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(140, 190, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 130, 50, 12))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(180, 360, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        self.menuaaa = QtWidgets.QMenu(self.menubar)
        self.menuaaa.setObjectName("menuaaa")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionadd = QtWidgets.QAction(MainWindow)
        self.actionadd.setObjectName("actionadd")
        self.menuaaa.addAction(self.actionadd)
        self.menubar.addAction(self.menuaaa.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.menuaaa.setTitle(_translate("MainWindow", "aaa"))
        self.actionadd.setText(_translate("MainWindow", "add"))














"""

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
       def __init__(self, parent=None):
           super(MainWindow, self).__init__(parent=parent)
           self.setupUi(self)

import sys

if __name__ == "__main__":
       app = QtWidgets.QApplication(sys.argv)
       w = MainWindow()
       w.show()
       sys.exit(app.exec_())

"""








class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
       def __init__(self, parent=None):
           super(MainWindow, self).__init__(parent=parent)
           self.setupUi(self)

import sys
from PyQt5.QtCore import QFile, QTextStream
import qdarkstyle
#import breeze_resources

if __name__ == "__main__":
       app = QtWidgets.QApplication(sys.argv)
       
       dark_stylesheet = qdarkstyle.load_stylesheet_pyqt5()
       app.setStyleSheet(dark_stylesheet)

       w = MainWindow()
       w.show()
       sys.exit(app.exec_())














