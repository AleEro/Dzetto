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

        # предустановки
        self.setWindowFlags(QtCore.Qt.Window)
        self.setMinimumSize(600, 150)
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

        # - присвоение боксов
        vbox = QtWidgets.QVBoxLayout()
        hbox = QtWidgets.QHBoxLayout()
        scrollareawidget = QtWidgets.QWidget()
        self.grid = QtWidgets.QGridLayout(scrollareawidget)
        scrl = QtWidgets.QScrollArea()
        scrl.setWidgetResizable(True)

        b2 = QtWidgets.QPushButton("Accept")
        b2.clicked.connect(self.accept_results)

        lb1 = QtWidgets.QLabel(F'Folder for NEW - \n{self.root.new_file_path}')
        lb2 = QtWidgets.QLabel(F'Folder for PLD - \n{self.root.old_file_path}')

        # здесь можно было бы организовать классметод
        # но мне лень пускай работает, пока работает...
        for i, v in enumerate(self.new_file_names):
            self.new_list_Label_1.append('')
            self.new_checkboxes.append(v)
            self.new_list_Label_1[i] = QtWidgets.QLabel()
            self.new_checkboxes[i] = QtWidgets.QCheckBox(v)
            self.grid.addWidget(self.new_checkboxes[i], i+1, 0)
            self.grid.addWidget(self.new_list_Label_1[i], i+1, 1)

        for i, v in enumerate(self.old_file_names):
            self.old_list_Label_1.append('')
            self.old_checkboxes.append(v)
            self.old_list_Label_1[i] = QtWidgets.QLabel()
            self.old_checkboxes[i] = QtWidgets.QCheckBox(v)
            self.grid.addWidget(self.old_checkboxes[i], i+1, 2)
            self.grid.addWidget(self.old_list_Label_1[i], i+1, 3)

        scrl.setWidget(scrollareawidget)
        hbox.addWidget(lb1)
        hbox.addWidget(lb2)
        vbox.addLayout(hbox)
        vbox.addWidget(scrl)
        vbox.addWidget(b2)
        print('setLayout DONE')
        self.setLayout(vbox)

    # здесь будет рисоваться сетка
    # def drawing_list(self):
    #     lb1 = QtWidgets.QLabel(F'Folder for NEW - \n{self.root.new_file_path}')
    #     lb2 = QtWidgets.QLabel(F'Folder for PLD - \n{self.root.old_file_path}')
    #
    #     # здесь можно было бы организовать классметод
    #     # но мне лень пускай работает, пока работает...
    #     for i, v in enumerate(self.new_file_names):
    #         self.new_list_Label_1.append('')
    #         self.new_checkboxes.append(v)
    #         self.new_list_Label_1[i] = QtWidgets.QLabel()
    #         self.new_checkboxes[i] = QtWidgets.QCheckBox(v)
    #         self.grid.addWidget(self.new_checkboxes[i], i+1, 0)
    #         self.grid.addWidget(self.new_list_Label_1[i], i+1, 1)

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

        self.close()
