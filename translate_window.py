from PyQt5 import QtWidgets, QtCore


class Trwindow(QtWidgets.QDialog):
    def __init__(self, root):
        super().__init__()

        self.root = root
        self.setWindowTitle('translate_window')
        self.vacabulary = ('original line', 'purposed translate',
                           'your variant', "next", "Cancel", "accept traslate",
                           'move translate to redaction field'
                           )

        self.vbox = QtWidgets.QVBoxLayout()
        self.hbox = QtWidgets.QHBoxLayout()

        self.text_box_2 = QtWidgets.QTextEdit(self)
        self.text_box_3 = QtWidgets.QTextEdit(self)
        self.text_box_4 = QtWidgets.QTextEdit(self)
        self.text_box_2.setMinimumSize(200, 50)

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

        self.text_box_3.setText('is aeaasasdad this is aeaasasdad this is aeaasasdad this is aeaasasdad')

        """
        пока не забыл
        начинать счетчик строк не с 0 а с 1 
        з.ы. для первой строки
        """
        # self.counter = 1

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
        self.text_box_4.setText(self.text_box_3.toPlainText())
        self.text_box_3.clear()

    def closeEvent(self, event):
        print('def closeEvent')
        self.hide()
