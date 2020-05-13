from PySide2.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QVBoxLayout()
        box = QCheckBox()
        stick = QComboBox()
        layout.addWidget(box)
        layout.addWidget(stick)

        self.setLayout(layout)

if __name__ == "__main__":
   app = QApplication([])
   win = Window()
   win.show()
   app.exec_()



