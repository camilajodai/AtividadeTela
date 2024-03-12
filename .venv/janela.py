# criar uma tabela com duas linhas verticais, uma em cima da outra. a de cima tem 3 colunas verticais e é isso??

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget,QApplication,QLabel,QLineEdit,QTableWidget,QTableWidgetItem,QHBoxLayout,QVBoxLayout

class GUI(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setGeometry(5,50,1580,800)
        self.setWindowTitle("Tabela - Atividade")
        
        layout_hor_principal = QVBoxLayout()
        
        label_line_cima = QLabel()
        label_line_baixo = QLabel()
        
        label_line_cima.setStyleSheet("QLabel{background-color:red}")
        label_line_cima.setFixedHeight(400)
        
        label_line_baixo.setStyleSheet("QLabel{background-color:blue}")
        label_line_baixo.setFixedHeight(400)
        
        layout_hor_principal.addWidget(label_line_cima)
        layout_hor_principal.addWidget(label_line_baixo)
        
        self.setLayout(layout_hor_principal)
        
        
        
        
app = QApplication(sys.argv)
janela = GUI ()
janela.show()
app.exec_()