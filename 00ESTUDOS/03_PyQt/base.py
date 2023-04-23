
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QSize #para adicao de tamanho na janela
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        
        self.setWindowTitle("Setup Inicial") 
        self.setCentralWidget(self.widget)
       




app = QApplication(sys.argv)
window =MainWindow()
window.show()
app.exec_()


