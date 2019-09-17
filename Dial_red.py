from PyQt5 import QtWidgets, QtCore


class FileButtons(QtWidgets.QDialog):
    def __init__(self, root):
        super().__init__()

        self.root = root
        self.vacabulary = ('original line', 'purposed translate',
                           'your variant', "next", "Cancel", "accept traslate",
                           'move translate to radaction field'
                           )
        self.vbox = QtWidgets.QVBoxLayout()
        self.hbox = QtWidgets.QHBoxLayout()

        self.text_box_2 = QtWidgets.QLineEdit(self)
        self.text_box_3 = QtWidgets.QLineEdit(self)
        self.text_box_4 = QtWidgets.QTextEdit(self)

        self.label_2 = QtWidgets.QLabel(self.vacabulary[0])
        self.label_3 = QtWidgets.QLabel(self.vacabulary[1])
        self.label_4 = QtWidgets.QLabel(self.vacabulary[2])

        self.nextButton = QtWidgets.QPushButton(self.vacabulary[3])
        self.cancelButton = QtWidgets.QPushButton(self.vacabulary[4])
        self.traslateButton = QtWidgets.QPushButton(self.vacabulary[5])
        self.move_to_red = QtWidgets.QPushButton(self.vacabulary[6])

        self.nextButton.clicked.connect(self.next_button)
        self.cancelButton.clicked.connect(self.cancel_button)
        self.traslateButton.clicked.connect(self.traslate_button)
        self.move_to_red.clicked.connect(self.move_to_button)

        self.vbox.addWidget(self.label_2)
        self.vbox.addWidget(self.text_box_2)
        self.vbox.addWidget(self.label_3)
        self.vbox.addWidget(self.text_box_3)
        self.vbox.addWidget(self.move_to_red)
        self.vbox.addWidget(self.label_4)
        self.vbox.addWidget(self.text_box_4)

        self.hbox.addWidget(self.nextButton)
        self.hbox.addWidget(self.traslateButton)
        self.hbox.addWidget(self.cancelButton)

        self.vbox.addLayout(self.hbox)

        self.setMinimumSize(QtCore.QSize(600, 200))
        self.setLayout(self.vbox)

    def next_button(self):
        print('next_button')
        self.root.text_box_1.setText(self.text_box_3.toPlainText())
        self.label_2.setText(self.vacabulary[0])
        self.label_3.setText(self.vacabulary[1])
        self.label_4.setText(self.vacabulary[2])

    def cancel_button(self):
        print('cancel_button')
        self.close()

    def traslate_button(self):
        print('traslatelButton')
        self.root.text_box_1.setText(self.text_box_4.toPlainText())

    def move_to_button(self):
        print('move_to_button')
        self.text_box_4.setText(self.text_box_3.text())
        self.text_box_3.clear()
