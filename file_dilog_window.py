from PyQt5 import QtWidgets, QtCore


class FileDialogWindow(QtWidgets.QDialog):
    def __init__(self, root):
        super().__init__()

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
        self.lb1 = QtWidgets.QLabel(F'Folder for NEW - \n{self.root.new_file_path}')
        self.lb2 = QtWidgets.QLabel(F'Folder for PLD - \n{self.root.old_file_path}')

        self.left_vbox = QtWidgets.QVBoxLayout()
        self.right_vbox = QtWidgets.QVBoxLayout()

        b2 = QtWidgets.QPushButton("Accept")
        b2.clicked.connect(self.accept_results)

        # создание макета
        main_hbox = QtWidgets.QHBoxLayout()
        main_hbox.addLayout(self.left_vbox)
        main_hbox.addLayout(self.right_vbox)

        self.left_vbox.addWidget(self.lb1)
        self.right_vbox.addWidget(self.lb2)

        main_vbox = QtWidgets.QVBoxLayout()
        main_vbox.addLayout(main_hbox)
        main_vbox.addWidget(b2)

        self.setLayout(main_vbox)

    def init_Gui(self):
        # тестовые строки
        # new_file_names = ["Checkbox_1", "Checkbox_2", "Checkbox_3", "Checkbox_4", "Checkbox_5"]
        # old_file_names = ["Checkbox_1", "Checkbox_2", "Checkbox_3", "Checkbox_4", "Checkbox_5"]
        pass

    @staticmethod
    def fill_list(box, file_list):
        for v in file_list:
            box.addWidget(QtWidgets.QCheckBox(v))

    # кнопка подтверждения
    def accept_results(self):
        self.close()

    def closeEvent(self, event):
        print('def closeEvent')
        # self.left_vbox.deletLater()
        # self.right_vbox.deletLater()
        event.accept()
