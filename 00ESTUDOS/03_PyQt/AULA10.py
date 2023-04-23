
from PySide2.QtWidgets import QApplication, QMainWindow, QLineEdit
from PySide2.QtCore import QSize #para adicao de tamanho na janela
import sys

#linha editavel]
#QlineEdit

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        
        self.setWindowTitle("Setup Inicial") 
        self.le = QLineEdit() #atribui a uma variavel a "funcao" desejada 
        self.le.setMaxLength(10)   #tamanho maximo de entrada
        self.le.setPlaceholderText('Enter your name')   #informa ao usuario qual tipo de texto ele deve usar

        self.setCentralWidget(self.le) #centraliza o objeto desejado em geral a funcao 
       
       #chamar metodo mandar sinal para execucao de metodos
        self.le.returnPressed.connect(self.return_pressed) #chamada de funcao 
        self.le.selectionChanged.connect(self.selection_changed)
        self.le.textChanged.connect(self.text_changed)
        self.le.textEdited.connect(self.text_edited)


        #ULTILIZACAO DE MASCARA
        self.le.setInputMask('000.000.000/0000-00;_')

    #mandar sinais conecta funcao imprime nome digitado e e ola. pega o texto e transforma em uma variavel
    def return_pressed(self):
        print("botao clicado")
        self.centralWidget().setText("Ola {}".format(self.le.text())) ##para pegar o texto digitado 

    def selection_changed(self): #troca secao 
        print("Selecao mudada!")
        print(self.centralWidget().selectedText())
    
    def text_changed(self,s): #texto trocado
        print("Text changed")
        print(s)

    def text_edited(self,s):
        print("text edited...")
        print(s)







app = QApplication(sys.argv)
window =MainWindow()
window.show()
app.exec_()