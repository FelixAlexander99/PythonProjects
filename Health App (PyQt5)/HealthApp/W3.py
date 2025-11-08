#Connecting modules
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton, QLineEdit
from Variables import *

#Classes
class FinalWin(QWidget): #Class for the creation of the first screen
    def __init__(self):
        super().__init__()
        self.set_appear()   #sets what the window will look like
        self.initUI()       #creating and configuring graphic elements
        self.show()         #make window visible

    def set_appear(self):
        self.setWindowTitle(W3_window_name)
        self.resize(win_width, win_height)
        self.move(win_move_x, win_move_y)
    
    def initUI(self):
        #Creating layout
        self.v_line = QVBoxLayout()

        #Creating widgets
        self.r_index = QLabel(W3_Rindex_text)
        self.c_perf = QLabel(W3_CPerf_text)

        #Arranging widgets on layout
        self.v_line.addWidget(self.r_index, alignment = Qt.AlignCenter)
        self.v_line.addWidget(self.c_perf, alignment = Qt.AlignCenter)

        #Setting layout
        self.setLayout(self.v_line)
    