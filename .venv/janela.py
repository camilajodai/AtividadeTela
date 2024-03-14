import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget,QApplication,QLabel,QLineEdit,QTableWidget,QTableWidgetItem,QHBoxLayout,QVBoxLayout,QCheckBox

class GUI(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setGeometry(5,50,1580,900)
        self.setWindowTitle("Tabela - Atividade")
        
        # layout principal vertical 
        layout_principal = QVBoxLayout()
        
        # separação 4 labels
        label_superior = QLabel() 
        label_meio = QLabel()
        label_tabela = QLabel()
        label_rodape = QLabel()
        
        # aplicação de estilos e ajute da altura
        label_superior.setStyleSheet("QLabel{background-color:blue}")
        label_superior.setFixedHeight(300)
        label_meio.setStyleSheet("QLabel{background-color:green}")
        label_meio.setFixedHeight(60)
        label_tabela.setStyleSheet("QLabel{background-color:red}")
        label_tabela.setFixedHeight(400)
        label_rodape.setStyleSheet("QLabel{background-color:purple}")
        label_rodape.setFixedHeight(100)
        
        # adicionar as labels na tela
        layout_principal.addWidget(label_superior)
        layout_principal.addWidget(label_meio)
        layout_principal.addWidget(label_tabela)
        layout_principal.addWidget(label_rodape)
        
        # layout horizontal para distribuir as 3 colunas na parte superior
        layout_hor_lb_superior = QHBoxLayout()
        layout_hor_esquerda = QHBoxLayout()
        # colunas
        label_col_esquerda = QLabel()
        label_col_meio = QLabel()
        label_col_direita = QLabel()
        # estilo das colunas
        label_col_esquerda.setStyleSheet("QLabel{background-color:pink}")
        label_col_meio.setStyleSheet("QLabel{background-color:yellow}")
        label_col_direita.setStyleSheet("QLabel{background-color:brown}")
        # adicionar no layout as labels
        # ------------------------------------------------------------------------------------------------
        
        layout_ver_col_esquerda = QVBoxLayout()
        
        label_estabelecimento = QLabel("Estabelecimento")
        label_estabelecimento.setStyleSheet("QLabel{font-size:15pt; color:white}")
        layout_ver_col_esquerda.addWidget(label_estabelecimento)

        edit_estabelecimento = QLineEdit()
        edit_estabelecimento.setStyleSheet("QLineEdit{border: 1px; padding: 10px}")
        edit_estabelecimento.setFixedWidth(500)
        layout_ver_col_esquerda.addWidget(edit_estabelecimento)
        # -----------------------------------------------------------------------------------------------
        label_documento = QLabel("Documento")
        label_documento.setStyleSheet("QLabel{font-size:15pt; color:white}")
        layout_ver_col_esquerda.addWidget(label_documento)

        edit_documento = QLineEdit()
        edit_documento.setStyleSheet("QLineEdit{border: 1px; padding: 10px}")
        edit_documento.setFixedWidth(500)
        layout_ver_col_esquerda.addWidget(edit_documento)
        # -----------------------------------------------------------------------------------------------
        label_grupo = QLabel("Grupo")
        label_grupo.setStyleSheet("QLabel{font-size:15pt; color:white}")
        layout_ver_col_esquerda.addWidget(label_grupo)

        edit_grupo = QLineEdit()
        edit_grupo.setStyleSheet("QLineEdit{border: 1px; padding: 10px}")
        edit_grupo.setFixedWidth(500)
        layout_ver_col_esquerda.addWidget(edit_grupo)
        # ----------------------------------------------------------------------------------------------------
        layout_hor_lb_superior.addLayout(layout_ver_col_esquerda)

        layout_ver_col_meio = QVBoxLayout()
        
        label_projeto = QLabel("Projeto")
        label_projeto.setStyleSheet("QLabel{font-size:15pt; color:white}")
        layout_ver_col_meio.addWidget(label_projeto)

        edit_projeto = QLineEdit()
        edit_projeto.setStyleSheet("QLineEdit{border: 1px; padding: 10px}")
        edit_projeto.setFixedWidth(500)
        layout_ver_col_meio.addWidget(edit_projeto)
        #
        label_numero = QLabel("Número")
        label_numero.setStyleSheet("QLabel{font-size:15pt; color:white}")
        layout_ver_col_meio.addWidget(label_numero)

        edit_numero = QLineEdit()
        edit_numero.setStyleSheet("QLineEdit{border: 1px; padding: 10px}")
        edit_numero.setFixedWidth(500)
        layout_ver_col_meio.addWidget(edit_numero)
        #
        label_usuela = QLabel("Usuário Elaborador")
        label_usuela.setStyleSheet("QLabel{font-size:15pt; color:white}")
        layout_ver_col_meio.addWidget(label_usuela)

        edit_usuela = QLineEdit()
        edit_usuela.setStyleSheet("QLineEdit{border: 1px; padding: 10px}")
        edit_usuela.setFixedWidth(500)
        layout_ver_col_meio.addWidget(edit_usuela)
        
        label_produto = QLabel("Produto")
        label_produto.setStyleSheet("QLabel{font-size:15pt; color:white}")
        layout_ver_col_meio.addWidget(label_produto)

        edit_produto = QLineEdit()
        edit_produto.setStyleSheet("QLineEdit{border: 1px; padding: 10px}")
        edit_produto.setFixedWidth(500)
        layout_ver_col_meio.addWidget(edit_produto)
        
        layout_hor_lb_superior.addLayout(layout_ver_col_meio)
        # -----------------------------------------------------------------------
        layout_ver_col_direita = QVBoxLayout()
        
        label_status = QLabel("Status")
        label_status.setStyleSheet("QLabel{font-size:15pt; color:white}")
        layout_ver_col_direita.addWidget(label_status)

        edit_status = QLineEdit()
        edit_status.setStyleSheet("QLineEdit{border: 1px; padding: 10px}")
        edit_status.setFixedWidth(500)
        layout_ver_col_direita.addWidget(edit_status)
        #
        label_dest = QLabel("Usuário Destinatário")
        label_dest.setStyleSheet("QLabel{font-size:15pt; color:white}")
        layout_ver_col_direita.addWidget(label_dest)

        edit_dest = QLineEdit()
        edit_dest.setStyleSheet("QLineEdit{border: 1px; padding: 10px}")
        edit_dest.setFixedWidth(500)
        layout_ver_col_direita.addWidget(edit_dest)
        #
        label_variante = QLabel("Variante")
        label_variante.setStyleSheet("QLabel{font-size:15pt; color:white}")
        layout_ver_col_direita.addWidget(label_variante)

        edit_variante = QLineEdit()
        edit_variante.setStyleSheet("QLineEdit{border: 1px; padding: 10px}")
        edit_variante.setFixedWidth(500)
        layout_ver_col_direita.addWidget(edit_variante)
        
        layout_hor_lb_superior.addLayout(layout_ver_col_direita)
        # ----------------------------------------------------------------------------------------
        label_superior.setLayout(layout_hor_lb_superior)
        # -----------------------------------------------------------------------------------------------------------------------
        layout_hor_lb_meio = QHBoxLayout()
        # colunas
        
        label_meio.setLayout(layout_hor_lb_meio)
        self.setLayout(layout_principal)
        # -----------------------------------------------------------------------------------------------------------------------
app = QApplication(sys.argv)
janela = GUI ()
janela.show()
app.exec_()