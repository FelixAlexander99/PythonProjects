#Connecting modules
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton, QLineEdit
from Variables import *
from W2 import *

#Classes
class MainWin(QWidget): #Class for the creation of the first screen
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
        #Creating widgets
        self.hello_text = QLabel(W1_welcome_text)
        self.instruction = QLabel(W1_instruction_set)
        self.button = QPushButton(W1_button_text)

        #Creating layouts
        self.layout = QVBoxLayout()

        #Adding widgets to layout
        self.layout.addWidget(self.hello_text, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.instruction, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.button, alignment = Qt.AlignCenter)

        #Setting layout
        self.setLayout(self.layout)

    def connects(self):
        self.button.clicked.connect(self.next_click)
    def next_click(self):
        self.hide()
        self.tw = TestWin()

#Creating and running application obj and window
app = QApplication([])
mw = MainWin()
app.exec_()
