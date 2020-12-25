
"""
import sys
from PyQt5 import QtWidgets


def window():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    w.setWindowTitle('PYQt5 lesson 1')
    w.show()
    sys.exit(app.exec_())

window()

"""






"""

import sys
from PyQt5 import QtWidgets, QtGui


def window():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    l1 = QtWidgets.QLabel(w)
    l2 = QtWidgets.QLabel(w)
    l1.setText('Hello World')
    l2.setPixmap(QtGui.QPixmap('globe.png'))#グイって呼んでる。
    w.setWindowTitle('PyQt4 Lesson 2')
    w.setGeometry(100, 100, 300, 200) #start size window 
    l1.move(100, 20)#文字l1の表示ポジション
    l2.move(120, 90)#画像l2の表示ポジション
    w.show()
    sys.exit(app.exec_())

window()


"""





"""



import sys
from PyQt5 import QtWidgets


def window():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    b = QtWidgets.QPushButton(w)
    l = QtWidgets.QLabel(w)
    b.setText('Push Me')
    l.setText('Look at Me')
    w.setWindowTitle('PyQt5 Lesson 3')
    b.move(100, 50)
    l.move(110, 100)
    w.setGeometry(100, 100, 300, 200)
    w.show()
    sys.exit(app.exec_())

window()




"""



"""


#ボタンのレイアウトも伸縮するようにstretchを指定する
import sys
from PyQt5 import QtWidgets


def window():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    b = QtWidgets.QPushButton('Push Me')
    l = QtWidgets.QLabel('Look at me')

    h_box = QtWidgets.QHBoxLayout()
    h_box.addStretch()
    h_box.addWidget(l)
    h_box.addStretch()

    v_box = QtWidgets.QVBoxLayout()
    v_box.addWidget(b)
    v_box.addLayout(h_box)

    w.setLayout(v_box)

    w.setWindowTitle('PyQt5 Lesson 4')
    w.show()

    sys.exit(app.exec_())

window()




"""











"""


#クリックに反応するようにする

import sys
from PyQt5 import QtWidgets


class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.b = QtWidgets.QPushButton('Push Me')
        self.l = QtWidgets.QLabel('I have not been clicked yet')

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addWidget(self.l)
        h_box.addStretch()

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.b)
        v_box.addLayout(h_box)

        self.setLayout(v_box)
        self.setWindowTitle('PyQt5 Lesson 5')

        self.b.clicked.connect(self.btn_click)

        self.show()

    def btn_click(self):
        self.l.setText('I have been clicked')


app = QtWidgets.QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())





"""







"""
#入力は出来るが消えないボックスを作るところまで

import sys
from PyQt5 import QtWidgets


class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.le = QtWidgets.QLineEdit()
        self.b = QtWidgets.QPushButton('Clear')

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.le)
        v_box.addWidget(self.b)

        self.setLayout(v_box)

        self.setWindowTitle('PyQt5 Lesson 6')

        self.show()

app = QtWidgets.QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())



"""















"""

#clearで消えるようにする and コンソールに入力文字を表示していく


import sys
from PyQt5 import QtWidgets


class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.le = QtWidgets.QLineEdit()
        self.b1 = QtWidgets.QPushButton('Clear')
        self.b2 = QtWidgets.QPushButton('Print')

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.le)
        v_box.addWidget(self.b1)
        v_box.addWidget(self.b2)

        self.setLayout(v_box)
        self.setWindowTitle('PyQt5 Lesson 7')

        self.b1.clicked.connect(self.btn_clk)
        self.b2.clicked.connect(self.btn_clk)

        self.show()

    def btn_clk(self):
        sender = self.sender()
        if sender.text() == 'Print':
            print(self.le.text())
        else:
            self.le.clear()


app = QtWidgets.QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())


"""





"""
#数値を入力するスライダーを作成

import sys
from PyQt5.QtWidgets import (QLineEdit, QSlider, QPushButton, QVBoxLayout, QApplication, QWidget)
from PyQt5.QtCore import Qt


class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.le = QLineEdit()
        self.b1 = QPushButton('Clear')
        self.b2 = QPushButton('Print')

        #スライダー
        self.s1 = QSlider(Qt.Horizontal)
        self.s1.setMinimum(1)
        self.s1.setMaximum(99)
        self.s1.setValue(25)
        self.s1.setTickInterval(10)
        self.s1.setTickPosition(QSlider.TicksBelow)

        v_box = QVBoxLayout()
        v_box.addWidget(self.le)
        v_box.addWidget(self.b1)
        v_box.addWidget(self.b2)
        v_box.addWidget(self.s1)

        self.setLayout(v_box)
        self.setWindowTitle('PyQt5 Lesson 8')

        self.b1.clicked.connect(lambda: self.btn_clk(self.b1, 'Hello from Clear'))
        self.b2.clicked.connect(lambda: self.btn_clk(self.b2, 'Hello from Print'))
        self.s1.valueChanged.connect(self.v_change)

        self.show()

#b.textはなにかしらボタンが押された時に、押されたボタンに設定されている名前、文字を吐き出す
#lamda式で定義した文字をstringとして設定してあるので、これを表示させる
    def btn_clk(self, b, string):
        if b.text() == 'Print':
            print(self.le.text())
        else:
            self.le.clear()
        print(string)

    def v_change(self):
        my_value = str(self.s1.value())
        self.le.setText(my_value)


app = QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())


"""







"""

import sys
from PyQt5.QtWidgets import (QLabel, QCheckBox, QPushButton, QVBoxLayout, QApplication, QWidget)


class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.lbl = QLabel()
        self.chx = QCheckBox('Do you like dogs?')
#チェックボックスはTFで返す


        self.btn = QPushButton('Push Me!')

        layout = QVBoxLayout()
        layout.addWidget(self.lbl)
        layout.addWidget(self.chx)
        layout.addWidget(self.btn)

        self.setLayout(layout)

        self.btn.clicked.connect(lambda: self.btn_clk(self.chx.isChecked(), self.lbl))

        self.show()

    def btn_clk(self, chk, lbl):
        if chk:
            lbl.setText('I guess you like dogs')
        else:
            lbl.setText('Dog hater then')
        print(chk)


app = QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())




"""






"""




import sys
from PyQt5.QtWidgets import (QLabel, QRadioButton, QPushButton, QVBoxLayout, QApplication, QWidget)


class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.lbl = QLabel('Which do you like best?')
        self.dog = QRadioButton('Dogs')
        self.cat = QRadioButton('Cats')
        self.btn = QPushButton('Select')

        layout = QVBoxLayout()
        layout.addWidget(self.lbl)
        layout.addWidget(self.dog)
        layout.addWidget(self.cat)
        layout.addWidget(self.btn)

        self.setLayout(layout)
        self.setWindowTitle('PyQt5 Lesson 10')

        self.btn.clicked.connect(lambda: self.btn_clk(self.dog.isChecked(), self.lbl))

        self.show()

    def btn_clk(self, chk, lbl):
        if chk:
            lbl.setText('I guess you like dogs')
        else:
            lbl.setText('So its cats for you')

app = QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())


"""






"""

#保存できないテキストエディタ


import sys
from PyQt5.QtWidgets import QApplication, QTextEdit, QWidget, QPushButton, QVBoxLayout


class Notepad(QWidget):

    def __init__(self):
        super(Notepad, self).__init__()
        self.text = QTextEdit(self)
        self.clr_btn = QPushButton('Clear')

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.addWidget(self.text)
        layout.addWidget(self.clr_btn)
        self.clr_btn.clicked.connect(self.clear_text)

        self.setLayout(layout)
        self.setWindowTitle('PyQt5 TextEdit')

        self.show()

    def clear_text(self):
        self.text.clear()

app = QApplication(sys.argv)
writer = Notepad()
sys.exit(app.exec_())



"""







"""
#保存まで
import sys
from PyQt5.QtWidgets import QApplication, QTextEdit, QWidget, QPushButton, QVBoxLayout


class Notepad(QWidget):

    def __init__(self):
        super(Notepad, self).__init__()
        self.text = QTextEdit(self)
        self.clr_btn = QPushButton('Save')

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.addWidget(self.text)
        layout.addWidget(self.clr_btn)
        self.clr_btn.clicked.connect(self.save_text)

        self.setLayout(layout)
        self.setWindowTitle('PyQt5 TextEdit')

        self.show()

    def save_text(self):
        with open('test.txt', 'w') as f:
            my_text = self.text.toPlainText()
            f.write(my_text)

app = QApplication(sys.argv)
writer = Notepad()
sys.exit(app.exec_())




"""


























"""

#QFileDialogの機能を使って保存や開く。

import os
import sys
from PyQt5.QtWidgets import QApplication, QTextEdit, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QFileDialog


class Notepad(QWidget):

    def __init__(self):
        super(Notepad, self).__init__()
        self.text = QTextEdit(self)
        self.clr_btn = QPushButton('Clear')
        self.sav_btn = QPushButton('Save')
        self.opn_btn = QPushButton('Open')

        self.init_ui()

    def init_ui(self):
        v_layout = QVBoxLayout()
        h_layout = QHBoxLayout()

        h_layout.addWidget(self.clr_btn)
        h_layout.addWidget(self.sav_btn)
        h_layout.addWidget(self.opn_btn)

        v_layout.addWidget(self.text)
        v_layout.addLayout(h_layout)

        self.sav_btn.clicked.connect(self.save_text)
        self.clr_btn.clicked.connect(self.clear_text)
        self.opn_btn.clicked.connect(self.open_text)

        self.setLayout(v_layout)
        self.setWindowTitle('PyQt5 TextEdit')

        self.show()

    def save_text(self):
        filename = QFileDialog.getSaveFileName(self, 'Save File', os.getenv('HOME'))
        with open(filename[0], 'w') as f:
            my_text = self.text.toPlainText()
            f.write(my_text)

    def open_text(self):
        filename = QFileDialog.getOpenFileName(self, 'Open File', os.getenv('HOME'))
        with open(filename[0], 'r') as f:
            file_text = f.read()
            self.text.setText(file_text)

    def clear_text(self):
        self.text.clear()

app = QApplication(sys.argv)
writer = Notepad()
sys.exit(app.exec_())


"""






"""



#上側にリボン？メニューバーを表示させる


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp


class MenuDemo(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create Menu Bar
        bar = self.menuBar()

        # Create Root Menus
        #大きく表示されるメニューバーの機能
        file = bar.addMenu('File')
        edit = bar.addMenu('Edit')

        # Create Actions for menus
        save_action = QAction('Save', self)
        save_action.setShortcut('Ctrl+S')

        new_action = QAction('New', self)
        new_action.setShortcut('Ctrl+N')

        quit_action = QAction('&Quit', self)
        quit_action.setShortcut('Ctrl+Q')

        find_action = QAction('Find...', self)

        replace_action = QAction('Replace...', self)

        # Add actions to Menus
        #メニューの中のボタンが押された、もしくはショートカットが押された場合を格納する
        file.addAction(new_action)
        file.addAction(save_action)
        file.addAction(quit_action)

        find_menu = edit.addMenu('Find')
        find_menu.addAction(find_action)
        find_menu.addAction(replace_action)

        # Events
        #addActionで定義したaction達ごとに適応する結果を定義
        #後で定めるquit_trigger関数にquit_actionを結び付ける
        #fileに定義した三つともに同じ処理を結び付けることも出来る
        quit_action.triggered.connect(self.quit_trigger)
        file.triggered.connect(self.selected)

        self.setWindowTitle("My Menus")
        self.resize(600, 400)

        self.show()

    def quit_trigger(self):
        qApp.quit()

    def selected(self, q):
        print(q.text() + ' selected')


app = QApplication(sys.argv)
menus = MenuDemo()
sys.exit(app.exec_())


"""








"""

import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget
from PyQt5.QtWidgets import QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout, QAction, qApp


class Notepad(QWidget):

    def __init__(self):
        super().__init__()
        self.text = QTextEdit(self)
        self.clr_btn = QPushButton('Clear')
        self.sav_btn = QPushButton('Save')
        self.opn_btn = QPushButton('Open')

        self.init_ui()

    def init_ui(self):
        v_layout = QVBoxLayout()
        h_layout = QHBoxLayout()

        h_layout.addWidget(self.clr_btn)
        h_layout.addWidget(self.sav_btn)
        h_layout.addWidget(self.opn_btn)

        v_layout.addWidget(self.text)
        v_layout.addLayout(h_layout)

        self.sav_btn.clicked.connect(self.save_text)
        self.clr_btn.clicked.connect(self.clear_text)
        self.opn_btn.clicked.connect(self.open_text)

        self.setLayout(v_layout)
        self.setWindowTitle('PyQt5 TextEdit')

        self.show()

    def save_text(self):
        filename = QFileDialog.getSaveFileName(self, 'Save File', os.getenv('HOME'))
        with open(filename[0], 'w') as f:
            my_text = self.text.toPlainText()
            f.write(my_text)

    def open_text(self):
        filename = QFileDialog.getOpenFileName(self, 'Open File', os.getenv('HOME'))
        with open(filename[0], 'r') as f:
            file_text = f.read()
            self.text.setText(file_text)

    def clear_text(self):
        self.text.clear()


class Writer(QMainWindow):
    def __init__(self):
        super().__init__()
        #mainwindowのなかにウィジェットのオブジェクトが配置されるイメージかな

        self.form_widget = Notepad()
        self.setCentralWidget(self.form_widget)

        self.init_ui()

    def init_ui(self):
        bar = self.menuBar()
        file = bar.addMenu('File')

        new_action = QAction('New', self)
        new_action.setShortcut('Ctrl+N')

        #上のQPushBottonと被らないようにアンドをつけているのかも

        save_action = QAction('&Save', self)
        save_action.setShortcut('Ctrl+S')

        open_action = QAction('&Open', self)

        quit_action = QAction('&Quit', self)

        file.addAction(new_action)
        file.addAction(save_action)
        file.addAction(open_action)
        file.addAction(quit_action)

        quit_action.triggered.connect(self.quit_trigger)
        file.triggered.connect(self.respond)

        self.show()

    def quit_trigger(self):
        qApp.quit()

    def respond(self, q):
        signal = q.text()

        if signal == 'New':
            self.form_widget.clear_text()
        elif signal == '&Open':
            self.form_widget.open_text()
        elif signal == '&Save':
            self.form_widget.save_text()


app = QApplication(sys.argv)
writer = Writer()
sys.exit(app.exec_())


"""





"""


#シートを作る機能もあり
import sys
from PyQt5.QtWidgets import QTableWidget, QApplication, QMainWindow


class MyTable(QTableWidget):
    def __init__(self, r, c):
        super().__init__(r, c)

        self.show()


class Sheet(QMainWindow):
    def __init__(self):
        super().__init__()

        self.form_widget = MyTable(10, 10)
        self.setCentralWidget(self.form_widget)

        self.show()

app = QApplication(sys.argv)
sheet = Sheet()
sys.exit(app.exec_())


"""










"""

#シートに最初から値を入れて置いたり、シートの列名を変更する

import sys
from PyQt5.QtWidgets import QTableWidget, QApplication, QMainWindow, QTableWidgetItem


class MyTable(QTableWidget):
    def __init__(self, r, c):
        super().__init__(r, c)
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

        self.form_widget = MyTable(10, 10)
        self.setCentralWidget(self.form_widget)
        col_headers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        self.form_widget.setHorizontalHeaderLabels(col_headers)

        #CurrentCellにカーソルを置いてからでないと実行できないようだ。
        number_0 = QTableWidgetItem('10')
        number_1 = QTableWidgetItem('15')
        self.form_widget.setCurrentCell(0, 0)
        self.form_widget.setItem(0, 0, number_0)
        self.form_widget.setCurrentCell(1, 1)
        self.form_widget.setItem(1, 1, number_1)

        self.show()

app = QApplication(sys.argv)
sheet = Sheet()
sys.exit(app.exec_())


"""







"""



import sys
import os
import csv
from PyQt5.QtWidgets import QTableWidget, QApplication, QMainWindow, QTableWidgetItem, QFileDialog


class MyTable(QTableWidget):
    def __init__(self, r, c):
        super().__init__(r, c)
        self.check_change = True
        self.init_ui()

    def init_ui(self):
        self.cellChanged.connect(self.c_current)
        self.show()

    def c_current(self):
        if self.check_change:
            row = self.currentRow()
            col = self.currentColumn()
            value = self.item(row, col)
            value = value.text()
            print("The current cell is ", row, ", ", col)
            print("In this cell we have: ", value)

    def open_sheet(self):
        self.check_change = False
        path = QFileDialog.getOpenFileName(self, 'Open CSV', os.getenv('HOME'), 'CSV(*.csv)')
        if path[0] != '':
            with open(path[0], newline='') as csv_file:
                self.setRowCount(0)
                self.setColumnCount(10)
                my_file = csv.reader(csv_file, delimiter=',', quotechar='|')
                for row_data in my_file:
                    row = self.rowCount()
                    self.insertRow(row)
                    if len(row_data) > 10:
                        self.setColumnCount(len(row_data))
                    for column, stuff in enumerate(row_data):
                        item = QTableWidgetItem(stuff)
                        self.setItem(row, column, item)
        self.check_change = True


class Sheet(QMainWindow):
    def __init__(self):
        super().__init__()

        self.form_widget = MyTable(10, 10)
        self.setCentralWidget(self.form_widget)
        col_headers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        self.form_widget.setHorizontalHeaderLabels(col_headers)

        self.form_widget.open_sheet()

        self.show()

app = QApplication(sys.argv)
sheet = Sheet()
sys.exit(app.exec_())



"""











"""


#save open機能をつける

import sys
import os
import csv
from PyQt5.QtWidgets import QTableWidget, QApplication, QMainWindow, QTableWidgetItem, QFileDialog
from PyQt5.QtWidgets import qApp, QAction


class MyTable(QTableWidget):
    def __init__(self, r, c):
        super().__init__(r, c)
        self.check_change = True
        self.init_ui()

    def init_ui(self):
        self.cellChanged.connect(self.c_current)
        self.show()

    def c_current(self):
        if self.check_change:
            row = self.currentRow()
            col = self.currentColumn()
            value = self.item(row, col)
            value = value.text()
            print("The current cell is ", row, ", ", col)
            print("In this cell we have: ", value)

    def open_sheet(self):
        self.check_change = False
        path = QFileDialog.getOpenFileName(self, 'Open CSV', os.getenv('HOME'), 'CSV(*.csv)')
        if path[0] != '':
            with open(path[0], newline='') as csv_file:
                self.setRowCount(0)
                self.setColumnCount(10)
                my_file = csv.reader(csv_file, dialect='excel')
                for row_data in my_file:
                    row = self.rowCount()
                    self.insertRow(row)
                    if len(row_data) > 10:
                        self.setColumnCount(len(row_data))
                    for column, stuff in enumerate(row_data):
                        item = QTableWidgetItem(stuff)
                        self.setItem(row, column, item)
        self.check_change = True

    def save_sheet(self):
        path = QFileDialog.getSaveFileName(self, 'Save CSV', os.getenv('HOME'), 'CSV(*.csv)')
        if path[0] != '':
            with open(path[0], 'w') as csv_file:
                writer = csv.writer(csv_file, dialect='excel')
                for row in range(self.rowCount()):
                    row_data = []
                    for column in range(self.columnCount()):
                        item = self.item(row, column)
                        if item is not None:
                            row_data.append(item.text())
                        else:
                            row_data.append('')
                    writer.writerow(row_data)


class Sheet(QMainWindow):
    def __init__(self):
        super().__init__()

        self.form_widget = MyTable(10, 10)
        self.setCentralWidget(self.form_widget)
        col_headers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        self.form_widget.setHorizontalHeaderLabels(col_headers)

        # Set up menu
        bar = self.menuBar()
        file = bar.addMenu('File')

        save_action = QAction('&Save', self)
        save_action.setShortcut('Ctrl+S')

        open_action = QAction('&Open', self)

        quit_action = QAction('&Quit', self)

        file.addAction(save_action)
        file.addAction(open_action)
        file.addAction(quit_action)

        quit_action.triggered.connect(self.quit_app)
        save_action.triggered.connect(self.form_widget.save_sheet)
        open_action.triggered.connect(self.form_widget.open_sheet)
        self.show()

    def quit_app(self):
        qApp.quit()

app = QApplication(sys.argv)
sheet = Sheet()
sys.exit(app.exec_())


"""






















































