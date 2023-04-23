from PySide2.QtWidgets import QApplication, QMainWindow, QLabel
from PySide2.QtCore import QSize, Qt
import sys
from   PySide2.QtGui import QPixmap


#imagem de fundo 


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AULA06")
        widget = QLabel("Pixmap")
        widget.setPixmap(QPixmap("jake.jpeg")) #ou caminho que se encontra]
        widget.setScaledContents(True)
        self.setCentralWidget(widget)

app = QApplication(sys.argv)
window =MainWindow()
window.show()
app.exec_()