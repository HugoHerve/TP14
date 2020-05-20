from PySide2.QtWidgets import *
from PySide2.QtGui import *


class Case(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.setFixedSize(400, 300)
        self.setWindowTitle("IHM")
        icon = QIcon(r'C:\Users\hugoh\Downloads\fr-flag.png')     #problème
        self.setWindowIcon(icon)
        layout = QGridLayout()
        label = QLabel("Hello World")
        label.setAlignment(Qt.AlignCenter)
        barre = QProgressBar()
        barre.setValue(50)
        lien = QLineEdit()
        button = QPushButton("Click me !")
        button.setToolTip("We did well")

        layout.addWidget(label)
        layout.addWidget(barre)
        layout.addWidget(lien)
        layout.addWidget(button)

        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication([])
    win = Case()
    win.show()
    app.exec_()
