# -*- Encoding: utf-8 -*-
import os
import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from file_dilog_window import FileDialogWindow
from translate_window import Trwindow


class File:
    def __init__(self, name, directory, data):
        self.name = name
        self.dir = directory
        self.data = data


class AppMainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # дополнительные параметры для всего класса
        self.files_dict = {}
        # КОРОЧЕ ВСЁЁЁЁЁЁЁЁЁ ЧЕРЕЗ СЛОВАРЬ
        self.files_dict['New'] = ''
        self.files_dict['Old'] = ''
        self.unchecked_files_list = []

        # # регистрирование доп окон
        # Все могло быть проще если бы каждый раз вызывался новый экземпляр этих класов
        # но я не считаю, что это правильно
        self.tr_window = Trwindow(self)
        self.file_dialog = FileDialogWindow(self)

        # натройка основного меню
        main_menu = self.menuBar()
        file_menu = main_menu.addMenu('File')

        exit_button = QtWidgets.QAction(QtGui.QIcon(None), 'Exit', self)
        exit_button.setShortcut('Ctrl+Q')
        exit_button.triggered.connect(app.closeAllWindows)
        file_menu.addAction(exit_button)

        compare_menu = main_menu.addMenu('Compare files')

        choose_scan_files = QtWidgets.QAction(QtGui.QIcon(None), 'Chose files to scan', self)
        choose_scan_files.setShortcut('Ctrl+Shift+F')
        choose_scan_files.triggered.connect(self.create_v_file)
        compare_menu.addAction(choose_scan_files)
        scan_files = QtWidgets.QAction(QtGui.QIcon(None), 'Translate files', self)
        scan_files.setShortcut('Ctrl+Shift+G')
        scan_files.triggered.connect(self.translate_w)
        compare_menu.addAction(scan_files)

        # предустановки окна
        self.width = 640
        self.height = 480

        self.setMinimumSize(QtCore.QSize(self.width, self.height))
        self.setWindowIcon(QtGui.QIcon('../../img/ico1.png'))
        self.setWindowTitle('Dzetto')
        self.statusBar().showMessage('for more information check info in main menu')
        #
        # self.text_box_1 = QtWidgets.QTextEdit()
        # self.setCentralWidget(self.text_box_1)
        self.create_v_file()

    # вызов окна для выбора и парсинга файлов
    def create_v_file(self):
        if self.files_dict['New'] == '' or self.files_dict['Old'] == '':
            self.files_dict['New'] = self.file_list(QtWidgets.QFileDialog().getExistingDirectory(
                None, "New"))
            self.files_dict['Old'] = self.file_list(QtWidgets.QFileDialog().getExistingDirectory(
                None, "Old"))
            if self.files_dict['New'] == '' or self.files_dict['Old'] == '':
                return
        print('\n\nfile_dialog_window\n\n')
        self.activateWindow()
        self.file_dialog.fill_layout(self.file_dialog.left_vbox, self.files_dict['New'])
        self.file_dialog.fill_layout(self.file_dialog.right_vbox, self.files_dict['Old'])

        self.file_dialog.exec()
        self.activateWindow()

    @staticmethod
    def file_list(file_path):
        print(f'Working path "{file_path}"')
        files = []
        # r=root, d=directories, f=files
        for r, d, f in os.walk(file_path):
            for file in f:
                if '.yml' in file:
                    # print(f'\n f= {f}, \nfile= {file}, \nr= {r}, \nd= {r}')
                    with open(f'{r}/{file}', encoding='utf-8') as data:
                        data = data.read()

                    files.append(File(name=file, directory=r, data=data))
        return files

    # вызов окна для перевода файлов
    def translate_w(self):
        print('translate_w')
        self.tr_window.exec()

    # закрытие других окон + подтверждение выхода
    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(
            self, 'Quit?', "Do you want quit?", QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = AppMainWindow()
    main.show()
    sys.exit(app.exec_())
