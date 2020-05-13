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

        layout.addWidget(label)     #Ajout des widgets dans le layout
        layout.addWidget(text)
        layout.addWidget(button1), layout.addWidget(button2)



        self.setLayout(layout)        #Associer du layout

if __name__ == "__main__":
   app = QApplication([])
   win = Fenetre()
   win.show()
   app.exec_()
