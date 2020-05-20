from PySide2.QtWidgets import *

class Fenetre(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("IHM")

        layout = QGridLayout()   #Création du layout

        label = QLabel("Laisser un commentaire")    #Création des widgets
        button1 = QPushButton("Succes")
        button2 = QPushButton("Cancel")
        text = QTextEdit()

        layout.addWidget(label,0,0,1,2)     #Ajout des widgets dans le layout
        layout.addWidget(text,1,0,1,2)
        layout.addWidget(button1,2,0,1,1)
        layout.addWidget(button2,2,1,1,1)



        self.setLayout(layout)        #Associer du layout

if __name__ == "__main__":
   app = QApplication([])
   win = Fenetre()
   win.show()
   app.exec_()
