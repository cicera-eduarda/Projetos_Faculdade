
from PySide2.QtWidgets import QApplication, QMainWindow, QSpinBox, QDoubleSpinBox
from PySide2.QtCore import QSize #para adicao de tamanho na janela
import sys

#maximo e minimo
##Qspinbox e QdoubleSpinbox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        
        self.setWindowTitle("QSpinbox and QDoubleSpinbox")  
        #self.spin = QSpinBox() #nao suporta numeros flutuantes 
        #parametros
        self.spin = QDoubleSpinBox() #suporta numero do conjunto float

        self.spin.setMinimum(-5)
        self.spin.setMaximum(5) 
        self.spin.setPrefix('R$') #sufixo e pre fixo
        self.spin.setSuffix(' C')
        #para chamar o metodo deveremos mandar um sinal
        self.spin.valueChanged.connect(self.value_changed) #imprime o valor 
        self.spin.valueChanged[str].connect(self.value_changed_str) #imprime o texto

        self.setCentralWidget(self.spin)


    #criacao de metodo

    def value_changed(self,i):
        print(i)

    def value_changed_str(self,s):
        print(s)


       




app = QApplication(sys.argv)
window =MainWindow()
window.show()
app.exec_()