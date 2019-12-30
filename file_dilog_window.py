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

        # строки для тестов
        self.new_file_names = ["Checkbox_1", "Checkbox_2", "Checkbox_3", "Checkbox_4", "Checkbox_5"]
        self.old_file_names = ["Checkbox_1", "Checkbox_2", "Checkbox_3", "Checkbox_4", "Checkbox_5"]

        lb1 = QtWidgets.QLabel(F'Folder for NEW - \n{self.root.new_file_path}')
        lb2 = QtWidgets.QLabel(F'Folder for PLD - \n{self.root.old_file_path}')

        accept_button = QtWidgets.QPushButton("Accept")
        accept_button.clicked.connect(self.accept_results)

        v_box = QtWidgets.QVBoxLayout()
        h_box = QtWidgets.QHBoxLayout()
        v_box_1 = QtWidgets.QVBoxLayout()
        v_box_2 = QtWidgets.QVBoxLayout()

        v_box.addLayout(h_box)
        h_box.addLayout(v_box_1)
        h_box.addLayout(v_box_2)
        v_box_1.addWidget(lb1)
        v_box_2.addWidget(lb2)
        v_box.addWidget(accept_button)

        self.fill(v_box_1, self.new_file_names)
        self.fill(v_box_2, self.old_file_names)

        self.setLayout(v_box)

    # - присвоение боксов
    @staticmethod
    def fill(box, element):
        for i, v in enumerate(element):
            box.addWidget(QtWidgets.QRadioButton(text=v))
    #     for i, v in enumerate(self.old_file_names):
    #         self.old_list_Label_1.append('')
    #         self.old_checkboxes.append(v)
    #         self.old_list_Label_1[i] = QtWidgets.QLabel()
    #         self.old_checkboxes[i] = QtWidgets.QCheckBox(v)
    #         self.grid.addWidget(self.old_checkboxes[i], i+1, 2)
    #         self.grid.addWidget(self.old_list_Label_1[i], i+1, 3)
    #
    #     scrl.setWidget(scrollareawidget)
    #     hbox.addWidget(lb1)
    #     hbox.addWidget(lb2)
    #     vbox.addLayout(hbox)
    #     vbox.addWidget(scrl)
    #     vbox.addWidget(b2)
    #     print('setLayout DONE')
    #     self.setLayout(vbox)

    # # кнопка подтверждения
    def accept_results(self):
        self.close()

    #     """
    #     здесь вообще творится безумный лес
    #     i think i was drunk when wrote this
    #     """
    #     print('def accept_results')
    #     self.new_list_Label_2 = []
    #     self.old_list_Label_2 = []
    #     self.root.result_dir_list = []
    #     self.root.result_files_list = []
    #     for i, v in enumerate(self.new_checkboxes):
    #         if v.checkState():
    #             self.new_list_Label_2.append(self.new_file_names[i])
    #             self.root.result_dir_list.append(self.root.new_file_directory[i])
    #             self.root.result_files_list.append(self.new_file_names[i])
    #
    #     for i, v in enumerate(self.old_checkboxes):
    #         if v.checkState():
    #             self.old_list_Label_2.append(self.old_file_names[i])
    #             self.root.result_dir_list.append(self.root.old_file_directory[i])
    #             self.root.result_files_list.append(self.old_file_names[i])
    #
    #     self.hide()
