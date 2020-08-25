from PyQt5 import QtWidgets, QtCore


class FileDialogWindow(QtWidgets.QDialog):
    def __init__(self, root):
        super(FileDialogWindow, self).__init__()

        # получение данных из основного цикла
        self.root = root

        # проверка того, что параметры получены
        # print(self.new_file_names, self.new_file_directory)
        # print(self.old_file_names, self.old_file_directory)

        # предустановки окна
        self.setWindowFlags(QtCore.Qt.Window)
        self.setMinimumSize(600, 150)
        self.setWindowTitle('Choose files to check')

        # основные элемменты
        self.lb1 = QtWidgets.QLabel('NEW')
        self.lb2 = QtWidgets.QLabel('OLD')

        b2 = QtWidgets.QPushButton("Accept")
        b2.clicked.connect(self.accept_results)

        # создание макета
        self.left_vbox = QtWidgets.QVBoxLayout()
        self.left_vbox.addWidget(self.lb1)

        self.right_vbox = QtWidgets.QVBoxLayout()
        self.right_vbox.addWidget(self.lb2)

        self.left_widget = QtWidgets.QWidget()
        self.left_widget.setLayout(self.left_vbox)

        self.right_widget = QtWidgets.QWidget()
        self.right_widget.setLayout(self.right_vbox)

        main_hbox = QtWidgets.QHBoxLayout()
        main_hbox.addWidget(self.left_widget)
        main_hbox.addWidget(self.right_widget)

        main_vbox = QtWidgets.QVBoxLayout()
        main_vbox.addLayout(main_hbox)
        main_vbox.addWidget(b2)

        self.setLayout(main_vbox)

    @staticmethod
    def fill_layout(box, file_list):
        [box.addWidget(QtWidgets.QCheckBox(v.name)) for v in file_list]

    # кнопка подтверждения
    def clear_widgets(self):
        [i.deleteLater() for i in self.left_widget.findChildren(QtWidgets.QCheckBox)]
        [i.deleteLater() for i in self.right_widget.findChildren(QtWidgets.QCheckBox)]

    def get_list(self, widget):
        return 1
    
    def accept_results(self):
        new_to_check = self.get_list(self.left_widget)
        old_to_check = self.get_list(self.right_widget)
        self.clear_widgets()
        self.close()
