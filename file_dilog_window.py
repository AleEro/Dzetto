from PyQt5 import QtWidgets


class TrWindow(QtWidgets.QDialog):
    def __init__(self, root):
        super().__init__()
        self.root = root

        self.new_file_names = self.root.new_file_names
        self.new_file_directory = self.root.new_file_directory

        self.old_file_names = self.root.old_file_names
        self.old_file_directory = self.root.new_file_directory

        self.setWindowTitle('Choose files to check')

        # self.new_file_names = ["Checkbox_1", "Checkbox_2", "Checkbox_3", "Checkbox_4", "Checkbox_5"]

        # self.old_file_names = ["Checkbox_1", "Checkbox_2", "Checkbox_3", "Checkbox_4", "Checkbox_5"]

        print(self.new_file_names, self.new_file_directory)
        print(self.old_file_names, self.old_file_directory)

        self.setMinimumSize(200, 150)

        self.new_checkboxes = []
        self.new_list_Label_1 = []
        self.new_list_Label_2 = []

        self.old_checkboxes = []
        self.old_list_Label_1 = []
        self.old_list_Label_2 = []

        self.lb1 = QtWidgets.QLabel(F'new - \n{self.root.new_file_path}', self)
        self.lb2 = QtWidgets.QLabel(F'old - \n{self.root.old_file_path}', self)

        self.b2 = QtWidgets.QPushButton("Accept results")
        self.b2.clicked.connect(self.accept_results)

        grid = QtWidgets.QGridLayout()
        grid.addWidget(self.lb1,
                       0, 0, 1, 2)
        grid.addWidget(self.lb2,
                       0, 2, 1, 2)

        for i, v in enumerate(self.new_file_names):
            self.new_list_Label_1.append('')
            self.new_checkboxes.append(v)
            self.new_list_Label_1[i] = QtWidgets.QLabel()
            self.new_checkboxes[i] = QtWidgets.QCheckBox(v)
            grid.addWidget(self.new_checkboxes[i],
                           i+1, 0)
            grid.addWidget(self.new_list_Label_1[i],
                           i+1, 1)

        for i, v in enumerate(self.old_file_names):
            self.old_list_Label_1.append('')
            self.old_checkboxes.append(v)
            self.old_list_Label_1[i] = QtWidgets.QLabel()
            self.old_checkboxes[i] = QtWidgets.QCheckBox(v)
            grid.addWidget(self.old_checkboxes[i],
                           i+1, 2)
            grid.addWidget(self.old_list_Label_1[i],
                           i+1, 3)

        # set the buttons position as last element
        self.last_elem = (len(self.new_file_names)
                          if len(self.new_file_names) > len(self.old_file_names)
                          else len(self.old_file_names))

        grid.addWidget(self.b2,
                       self.last_elem+1, 2, 1, 2)
        print('setLayout DONE')
        self.setLayout(grid)

    def data_update(self):
        self.new_file_names = self.root.new_file_names
        self.new_file_directory = self.root.new_file_directory

        self.old_file_names = self.root.old_file_names
        self.old_file_directory = self.root.new_file_directory
        print('data_update DONE')

    # - - - - - - - - - - - - -

    # def show_menu(self, ):
    #
    #     for i, v in enumerate(self.new_file_names):
    #         self.new_list_Label_1.append('')
    #         self.new_checkboxes.append(v)
    #         self.new_list_Label_1[i] = QtWidgets.QLabel()
    #         self.new_checkboxes[i] = QtWidgets.QCheckBox(v)
    #         grid.addWidget(self.new_checkboxes[i],
    #                        i+1, 0)
    #         grid.addWidget(self.new_list_Label_1[i],
    #                        i+1, 1)


    def accept_results(self):
        print('def accept_results')
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
        self.hide()
