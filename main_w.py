# -*- Encoding: utf-8 -*-
import os
import sys
import re
from PyQt5 import QtWidgets, QtGui, QtCore
from translate_window import Trwindow
from file_dilog_window import FileDialogWindow
from time import strftime


class AppMainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # дополнительные параметры для всего класса
        self.new_file_path = ''
        self.new_file_names = []
        self.new_file_directory = []

        self.old_file_path = ''
        self.old_file_names = []
        self.old_file_directory = []

        self.result_dir_list = []
        self.result_files_list = []
        self.locker = False

        # - регистрирование доп окон
        self.tr_window = Trwindow(self)
        self.files_to_check = FileDialogWindow(self)

        # прорисовка интерфеса
        self.width = 640
        self.height = 480

        self.setMinimumSize(QtCore.QSize(self.width, self.height))
        self.setWindowIcon(QtGui.QIcon('img\\ico1.png'))
        self.setWindowTitle('Dzetto')
        self.statusBar().showMessage('for more information check info in main menu')

        # создание доп меню
        main_menu = self.menuBar()
        file_menu = main_menu.addMenu('File')
        compare_menu = main_menu.addMenu('compared files')

        choose_dir = QtWidgets.QAction(QtGui.QIcon(None), 'Chose dir', self)
        choose_dir.setShortcut('Ctrl+Shift+D')
        choose_dir.triggered.connect(self.choose_directory)
        file_menu.addAction(choose_dir)

        choose_scan_files = QtWidgets.QAction(QtGui.QIcon(None), 'Chose files to scan', self)
        choose_scan_files.setShortcut('Ctrl+Shift+F')
        choose_scan_files.triggered.connect(self.choose_scanned_files)
        compare_menu.addAction(choose_scan_files)

        scan_files = QtWidgets.QAction(QtGui.QIcon(None), 'Translate files', self)
        scan_files.setShortcut('Ctrl+Shift+G')
        scan_files.triggered.connect(self.translate_w)
        compare_menu.addAction(scan_files)

        exit_button = QtWidgets.QAction(QtGui.QIcon(None), 'Quit', self)
        exit_button.setShortcut('Ctrl+Q')
        exit_button.triggered.connect(app.closeAllWindows)
        file_menu.addAction(exit_button)

        # добавление text_box_1, будет как лог.
        self.text_box_1 = QtWidgets.QTextEdit()
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.text_box_1)
        self.setCentralWidget(self.text_box_1)

    # выбор директории
    def choose_directory(self):
        print('choose_directory')
        self.new_file_path = QtWidgets.QFileDialog().getExistingDirectory(
            None, "Select a new files folder")
        print("new directory: ", self.new_file_path, "\n")

        self.old_file_path = QtWidgets.QFileDialog().getExistingDirectory(
            None, "Select a old files folder")
        print("old directory: ", self.old_file_path, "\n")
        self.activateWindow()

    # вызов окна для выбора и парсинга файлов
    def choose_scanned_files(self):
        # указание старой папки
        # после чего должно выкинуть все файлы в старой и новой папке
        # в место где лежит прога
        # создать папку с датой + время,а в ней:
        # папка старое
        # папка новое
        # папка результат
        # вывод на основной экран результата действий

        # проверка на пустые директории
        if self.new_file_path is '' or self.old_file_path is '':
            self.choose_directory()
            if self.new_file_path is '' or self.old_file_path is '':
                return

        self.new_file_names, self.new_file_directory = self.file_list(self.new_file_path)
        self.old_file_names, self.old_file_directory = self.file_list(self.old_file_path)

        self.files_to_check.root = self
        self.files_to_check.exec()
        # self.locker = False
        #
        # # после того, как результирующие папки получены
        # # происходит вызов функции,
        # # которая выполняет парсинг,
        # # отправляя в него имена файлов и их положение на пк
        #
        # if self.locker is True:
        #     print("___________continue")

    @staticmethod
    def file_list(file_path):
        print(f'file_list {file_path}')
        file_names = []
        file_dir = []
        # r=root, d=directories, f=files
        for r, d, files in os.walk(file_path):
            for file in files:
                if '.yml' in file:
                    file_names.append(file)
                    file_dir.append(r)
        return file_names, file_dir

    # вызов окна для перевода файлов
    def translate_w(self):
        print('translate_w')
        self.tr_window.exec()

    # подтверждение выхода из программы
    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(self, 'Quit?', "Do you want quit?",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.Cancel)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


#  на случай если программа запускается из оболочки
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = AppMainWindow()
    main.show()
    sys.exit(app.exec_())
