
from PySide2.QtWidgets import QApplication, QMainWindow, QComboBox
from PySide2.QtCore import QSize #para adicao de tamanho na janela
import sys

#Combobox - alteracao de combox mandar sinal

#caixa de escolha com seta para baixo
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("ComboBox") 
        self.setFixedSize(QSize(600,300))

        self.widget = QComboBox() #variavel
        self.widget.addItems(['item 1','item 2', 'item 3'])
        #quando ele mudar ele vai chamar a variavel
        self.widget.currentIndexChanged.connect(self.index_change) #quando nosso indice mudar ele vai conectar
       
        self.widget.currentTextChanged.connect(self.text_change)

        
        self.setCentralWidget(self.widget) #centralizacao deste elemento
    #metodo 1
    def index_change(self,i):
        print(i)
    #metodo 2
    def text_change(self,s):
        print(s)
    


       




#execucao aplicacao
app = QApplication(sys.argv)
window =MainWindow()
window.show()
app.exec_()
