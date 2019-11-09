from PyQt5 import QtWidgets, QtCore


class Trwindow(QtWidgets.QDialog):
    def __init__(self, root):
        super().__init__()

        # получение данных из основного цикла
        self.root = root

        # проверка того, что они получены
        # ----

        # предустав=новки
        self.setWindowFlags(QtCore.Qt.Window)
        self.setMinimumSize(QtCore.QSize(600, 200))

        # прорисовка окна
        self.setWindowTitle('translate_window')
        self.vacabulary = ('original line',
                           'purposed translate',
                           'your variant',
                           "accept",
                           "Cancel",
                           "accept traslate",
                           'move translate to redaction field',
                           'prev',
                           'here will be line numb',
                           'next'
                           )

        self.tr_vbox = QtWidgets.QVBoxLayout()
        self.tr_hbox = QtWidgets.QHBoxLayout()
        self.tr_hbox_1 = QtWidgets.QHBoxLayout()

        self.tr_text_box_2 = QtWidgets.QTextEdit('here will be line from your old file')
        self.tr_text_box_3 = QtWidgets.QTextEdit('here line from the translate service')
        self.tr_text_box_4 = QtWidgets.QTextEdit('here u need to input your variant of translate')

        self.label_2 = QtWidgets.QLabel(self.vacabulary[0])
        self.label_3 = QtWidgets.QLabel(self.vacabulary[1])
        self.label_4 = QtWidgets.QLabel(self.vacabulary[2])

        self.accept_Button = QtWidgets.QPushButton(self.vacabulary[3])
        self.accept_Button.clicked.connect(self.accept_func)

        self.cancel_Button = QtWidgets.QPushButton(self.vacabulary[4])
        self.cancel_Button.clicked.connect(self.cancel_func)

        self.traslate_Button = QtWidgets.QPushButton(self.vacabulary[5])
        self.traslate_Button.clicked.connect(self.traslate_func)

        self.move_to_red = QtWidgets.QPushButton(self.vacabulary[6])
        self.move_to_red.clicked.connect(self.move_to_red_func)

        self.prev_button = QtWidgets.QPushButton(self.vacabulary[7])
        # self.prev_button.clicked.connect(self.move_to_red_func)

        self.cur_string = QtWidgets.QLineEdit(self.vacabulary[8])
        # self.cur_string.clicked.connect(self.move_to_red_func)

        self.next_button = QtWidgets.QPushButton(self.vacabulary[9])
        # self.next_button.clicked.connect(self.move_to_red_func)

        self.tr_hbox.addWidget(self.accept_Button)
        self.tr_hbox.addWidget(self.traslate_Button)
        self.tr_hbox.addWidget(self.cancel_Button)

        self.tr_hbox_1.addWidget(self.prev_button)
        self.tr_hbox_1.addWidget(self.cur_string)
        self.tr_hbox_1.addWidget(self.next_button)

        self.tr_vbox.addLayout(self.tr_hbox_1)
        self.tr_vbox.addWidget(self.label_2)
        self.tr_vbox.addWidget(self.tr_text_box_2)
        self.tr_vbox.addWidget(self.label_3)
        self.tr_vbox.addWidget(self.tr_text_box_3)
        self.tr_vbox.addWidget(self.move_to_red)
        self.tr_vbox.addWidget(self.label_4)
        self.tr_vbox.addWidget(self.tr_text_box_4)
        self.tr_vbox.addLayout(self.tr_hbox)

        self.setLayout(self.tr_vbox)

        """
        пока не забыл
        начинать счетчик строк не с 0 а с 1 
        з.ы. для первой строки
        """
        # self.counter = 1

    def accept_func(self):
        print('accept_func')
        self.root.text_box_1.setText(self.tr_text_box_3.toPlainText())
        self.label_2.setText(self.vacabulary[0])
        self.label_3.setText(self.vacabulary[1])
        self.label_4.setText(self.vacabulary[2])

    def cancel_func(self):
        print('cancel_func')
        self.close()

    def traslate_func(self):
        print('traslatelButton')
        self.root.text_box_1.setText(self.tr_text_box_4.toPlainText())

    def move_to_red_func(self):
        print('move_to_red_func')
        self.tr_text_box_4.setText(self.tr_text_box_3.toPlainText())
        self.tr_text_box_3.clear()

    def closeEvent(self, event):
        print('def closeEvent')
        self.hide()
