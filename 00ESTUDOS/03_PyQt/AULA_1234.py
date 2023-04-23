from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton
import sys
from PySide2.QtCore import QSize #para adicao de tamanho na janela
#criacao execucao janela, adicao de bbotao, clique em botao, tamanho janela

#criacao de classe para a janela e suas caracteristicas
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        #titulo janela
        self.setWindowTitle("Setup Inicial") 
        #adicao de botao1
        self.button = QPushButton("Start")
        
        #tamanho da janela
        self.setFixedSize(QSize(600,400))

        #centralizacao do botao, adicao do botao
        self.setCentralWidget(self.button)
        #quando eu clicar no botao ele vai chamar o metodo de clique no botao1
        self.button.clicked.connect(self.clicked_button)

    #criacao de funcao para botao1
    def clicked_button(self):
        print ("Iniciando processo de configuracoes")
        self.button.setEnabled(False) #depois de utilizado o botao vai ser desabilitado
        #self.setWindowTitle("Somente um clique") 


#mensagem para desabilitar função 

#execucao aplicacao
app = QApplication(sys.argv)
window =MainWindow()
window.show()
app.exec_()


