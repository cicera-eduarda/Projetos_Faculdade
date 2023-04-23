
from PySide2.QtWidgets import QApplication, QMainWindow, QListWidget
from PySide2.QtCore import QSize 
import sys

# QListBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Setup Inicial") 
        
        
        lb = QListWidget() # variavel
        lb.addItems(['item1', 'item2', 'item3'])
        self.setCentralWidget(lb) 

        #sinal de execucao de funcao pegar maneiras de texto no list
        lb.currentItemChanged.connect(self.index_changed)
        lb.currentTextChanged.connect(self.text_cheanged)
    
    def index_changed(self , i):
        print(i.text())
    
    def text_cheanged(self, s):
        print(s)
        if s =="item1":
            print('Ok')
        elif s =="item2":
            print ('OLA')
        





#execucao aplicacao
app = QApplication(sys.argv)
window =MainWindow()
window.show()
app.exec_()
