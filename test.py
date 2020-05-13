from PySide2.QtWidgets import *
app = QApplication([])
mainWidget = QWidget()


layout = QVBoxLayout()


label = QLabel("Ceci est un QLabel")
button = QPushButton("Ceci est un QPushButton")
combobox = QComboBox()
checkbox1 = QCheckBox("oui")
checkbox2 = QCheckBox("non")

layout.addWidget(label)
layout.addWidget(button)
layout.addWidget(combobox)
layout.addWidget(checkbox1)
layout.addWidget(checkbox2)

mainWidget.setLayout(layout)


mainWidget.setWindowTitle("Ma première interface en Qt")
mainWidget.show()
app.exec_()
