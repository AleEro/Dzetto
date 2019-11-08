from PyQt5 import QtWidgets, QtCore


class FileDialogWindow(QtWidgets.QDialog):
    def __init__(self, root):
        super().__init__()

        # получение данных из основного цикла
        self.root = root
        self.new_file_names = self.root.new_file_names
        self.new_file_directory = self.root.new_file_directory

        self.old_file_names = self.root.old_file_names
        self.old_file_directory = self.root.new_file_directory

        # проверка того, что они получены
        print(self.new_file_names, self.new_file_directory)
        print(self.old_file_names, self.old_file_directory)

        # предустановки
        self.setWindowFlags(QtCore.Qt.Window)
        self.setMinimumSize(200, 150)
        self.setWindowTitle('Choose files to check')

        self.new_checkboxes = []
        self.new_list_Label_1 = []
        self.new_list_Label_2 = []

        self.old_checkboxes = []
        self.old_list_Label_1 = []
        self.old_list_Label_2 = []

        # строки для тестов
        # self.new_file_names = ["Checkbox_1", "Checkbox_2", "Checkbox_3", "Checkbox_4", "Checkbox_5"]
        # self.old_file_names = ["Checkbox_1", "Checkbox_2", "Checkbox_3", "Checkbox_4", "Checkbox_5"]

        # прорисовка меню
        """
        я пробовал добавить это в функцию, 
        но это плохо кончилось 
        и я решил, что это должно быть в инициализации, 
        однако никто не говорил, что кноки нельзя добавлять в конец
        или все же проще было бы создавать новый экземпляр класса диалог...
        """
        self.lb1 = QtWidgets.QLabel(F'new - \n{self.root.new_file_path}')
        self.lb2 = QtWidgets.QLabel(F'old - \n{self.root.old_file_path}')
        b2 = QtWidgets.QPushButton("Accept results")
        b2.clicked.connect(self.accept_results)

        # - присвоение боксов
        # grid => grid  для того что бы перевести сетку в функцию, что будет обновлятся новыми файлами
        grid = QtWidgets.QGridLayout()
        vbox = QtWidgets.QVBoxLayout()
        hbox = QtWidgets.QHBoxLayout()
        scrl = QtWidgets.QScrollArea()

        # здесь можно было бы организовать классметод
        # но мне лень
        for i, v in enumerate(self.new_file_names):
            self.new_list_Label_1.append('')
            self.new_checkboxes.append(v)
            self.new_list_Label_1[i] = QtWidgets.QLabel()
            self.new_checkboxes[i] = QtWidgets.QCheckBox(v)
            grid.addWidget(self.new_checkboxes[i], i+1, 0)
            grid.addWidget(self.new_list_Label_1[i], i+1, 1)

        for i, v in enumerate(self.old_file_names):
            self.old_list_Label_1.append('')
            self.old_checkboxes.append(v)
            self.old_list_Label_1[i] = QtWidgets.QLabel()
            self.old_checkboxes[i] = QtWidgets.QCheckBox(v)
            grid.addWidget(self.old_checkboxes[i], i+1, 2)
            grid.addWidget(self.old_list_Label_1[i], i+1, 3)

        # scrl.setWidget(grid)
        # scrl.setWidgetResizable(True)
        # scrl.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        hbox.addWidget(self.lb1)
        hbox.addWidget(self.lb2)
        vbox.addLayout(hbox)
        # vbox.addWidget(scrl)
        vbox.addLayout(grid)
        vbox.addWidget(b2)
        print('setLayout DONE')
        self.setLayout(vbox)

    # кнопка подтверждения
    def accept_results(self):
        """
        здесь вообще творится безумный лес
        i think i was drunk when wrote this
        """
        print('def accept_results')
        self.new_list_Label_2 = []
        self.old_list_Label_2 = []
        self.root.result_dir_list = []
        self.root.result_files_list = []
        for i, v in enumerate(self.new_checkboxes):
            if v.checkState():
                self.new_list_Label_2.append(self.new_file_names[i])
                self.root.result_dir_list.append(self.root.new_file_directory[i])
                self.root.result_files_list.append(self.new_file_names[i])

        for i, v in enumerate(self.old_checkboxes):
            if v.checkState():
                self.old_list_Label_2.append(self.old_file_names[i])
                self.root.result_dir_list.append(self.root.old_file_directory[i])
                self.root.result_files_list.append(self.old_file_names[i])

        self.root.text_box_1.setText(f'''new files are: \n{self.new_file_names}
                                     \nold files are: \n{self.old_file_names}
                                     \nfiles which you compare:
                                     \nnew \n{self.new_list_Label_2}
                                     \nold \n{self.old_list_Label_2}
                                     \nresultlist of dir are: \n{self.root.result_dir_list}
                                     \nresultlist of fls are: \n{self.root.result_files_list}''')
        self.close()
