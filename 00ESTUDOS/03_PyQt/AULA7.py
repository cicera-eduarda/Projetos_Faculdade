
from PySide2.QtWidgets import QApplication, QMainWindow, QCheckBox
from PySide2.QtCore import Qt, QSize #para adicao de tamanho na janela
import sys
#checkbox
#checa o estado atual dele e chama um metodo 


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        #titulo janela
        self.setWindowTitle("Checkbox") 
        ck = QCheckBox("Selecione as opcoes desejadas")
        ck.setCheckState(Qt.Checked)
        ck.stateChanged.connect(self.show_state) #checa se esta habilitada ou nao 
        ck.setCheckState(Qt.PartiallyChecked)#PARCIALMENTE MARCADO (marcado0 naomarcado2 e parcialmentemarcado 1)

        #chamada do metodo

        self.setCentralWidget(ck) 

    #metodo para conferencia checkboz
    def show_state(self,s): #variavel s
        print(s==Qt.Checked)
        print(s)

       




#execucao aplicacao
app = QApplication(sys.argv)
window =MainWindow()
window.show()
app.exec_()


