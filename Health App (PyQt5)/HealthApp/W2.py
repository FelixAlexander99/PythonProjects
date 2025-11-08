#Connecting modules
from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton, QLineEdit
from Variables import *
from W3 import *

#Window 2 class
class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()   #sets what the window will look like
        self.initUI()       #creating and configuring graphic elements
        self.connects()     #establishes connections between elements
        self.show()         #make window visible
    def set_appear(self):
        self.setWindowTitle(W1_window_name)
        self.resize(win_width, win_height)
        self.move(win_move_x, win_move_y)
    def initUI(self):
        #Creating layouts
        self.h_line = QHBoxLayout()
        self.l_line = QVBoxLayout()    
        self.r_line = QVBoxLayout()

        #Creating widgets
        self.insert_name = QLabel(W2_name)
        self.name_edit = QLineEdit(W2_namebox)
        self.age = QLabel(W2_age)
        self.insert_age = QLineEdit(W2_default)
        self.instruction1 = QLabel(W2_instruction1)
        self.test1_btn = QPushButton(W2_button1_text)
        self.insert_test1 = QLineEdit(W2_default)
        self.instruction2 = QLabel(W2_instruction2)
        self.test2_btn = QPushButton(W2_button2_text)
        self.instruction3 = QLabel(W2_instruction3)
        self.test3_btn = QPushButton(W2_button3_text)
        self.insert_test2 = QLineEdit(W2_default)
        self.insert_test3 = QLineEdit(W2_default)
        #self.timer = QTime(0,0,15)
        #self.timer.toString("hh:mm:ss")
        self.page3_btn = QPushButton(W2_button4_text)

        #Adding widgets to layouts
        self.l_line.addWidget(self.insert_name, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.name_edit, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.age, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.insert_age, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.instruction1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.test1_btn, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.insert_test1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.instruction2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.test2_btn, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.instruction3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.test3_btn, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.insert_test2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.insert_test3, alignment = Qt.AlignLeft)
        #self.r_line.addWidget(self.timer, alignment = Qt.AlignRight)
        self.l_line.addWidget(self.page3_btn, alignment = Qt.AlignCenter)

        #Combining layouts
        self.h_line.addLayout(self.l_line)        
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)

    def connects(self):
        self.page3_btn.clicked.connect(self.next_click)
        #self.test1_btn.clicked.connect(self.timer_test)

    def next_click(self):
        self.hide()
        self.tw = FinalWin()

    def timer_test(self):
        pass