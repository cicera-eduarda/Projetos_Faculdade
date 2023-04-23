from PySide2.QtWidgets import QApplication, QMainWindow, QLabel
from PySide2.QtCore import QSize, Qt
import sys
from PySide2.QtCore import QSize #para adicao de tamanho na janela

#label, nomear elementos

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Aula05")
        widget = QLabel ("Aula 05 - Label") 
        font = widget.font() #declaracao fonte
        font.setPointSize(35)  #tamanho da fonte
        widget.setFont(font) #chamada de fonte
        
        widget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) #alinhamento
        self.setCentralWidget(widget) #ficara no meio da janela

        self.setFixedSize(QSize(600,600))
        self.setCentralWidget(widget)




app= QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec_()
