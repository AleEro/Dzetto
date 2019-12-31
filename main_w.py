# -*- Encoding: utf-8 -*-
import os
import sys
import re
from PyQt5 import QtWidgets, QtGui, QtCore
from translate_window import Trwindow
from file_dilog_window import FileDialogWindow
from time import strftime
import parse_0


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
        self.element = []
        self.locker = False
        
        # регистрирование доп окон
        self.tr_window = Trwindow(self)
        self.files_to_check = FileDialogWindow(self)
        
        # прорисовка интерфеса
        self.width = 640
        self.height = 480
        
        self.setMinimumSize(QtCore.QSize(self.width, self.height))
        self.setWindowIcon(QtGui.QIcon('img\\ico1.png'))
        self.setWindowTitle('Dzetto')
        self.statusBar().showMessage('for more information check info in main menu')
        
        main_menu = self.menuBar()
        file_menu = main_menu.addMenu('File')
        compare_menu = main_menu.addMenu('Compare files')
        
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
        
        exit_button = QtWidgets.QAction(QtGui.QIcon(None), 'Exit', self)
        exit_button.setShortcut('Ctrl+Q')
        exit_button.triggered.connect(app.closeAllWindows)
        file_menu.addAction(exit_button)
        
        self.text_box_1 = QtWidgets.QTextEdit()
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.text_box_1)
        self.setCentralWidget(self.text_box_1)
        
    # выбор директории
    def choose_directory(self):
        self.new_file_path = QtWidgets.QFileDialog().getExistingDirectory(
            None, "Select a new files folder")
        
        self.old_file_path = QtWidgets.QFileDialog().getExistingDirectory(
            None, "Select a old files folder")
        print("new directory: ", self.new_file_path, "\n")
        print("old directory: ", self.old_file_path, "\n")
        self.activateWindow()
        
    # вызов окна для выбора и парсинга файлов
    def choose_scanned_files(self):
        # проверка на пустые директории
        if self.new_file_path is '' or self.old_file_path is '':
            self.choose_directory()
            if self.new_file_path is '' or self.old_file_path is '':
                return
        self.new_file_names, self.new_file_directory = self.file_list(self.new_file_path)
        self.old_file_names, self.old_file_directory = self.file_list(self.old_file_path)
        print('file_dilog_window')
        self.files_to_check.fill_list(self.files_to_check.left_vbox, self.new_file_names)
        self.files_to_check.fill_list(self.files_to_check.right_vbox, self.old_file_names)
        self.files_to_check.exec()
         
    @staticmethod
    def file_list(file_path):
        print(f'file_list {file_path}')
        file_names = []
        file_dir = []
        # r=root, d=directories, f=files
        for r, d, f in os.walk(file_path):
            for file in f:
                while ('.yml' in file) and (file not in file_names):
                    file_names.append(file)
                    file_dir.append(r)
        return file_names, file_dir
        
    # вызов окна для перевода файлов
    def translate_w(self):
        print('translate_w')
        self.tr_window.exec()
        
    # закрытие других окон + подтверждение выхода
    def closeEvent(self, event):
        print('def closeEvent')
        reply = QtWidgets.QMessageBox.question(self, 'Quit?', "Do you want quit?",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.Cancel)
        if reply == QtWidgets.QMessageBox.Yes:
            print("accepted")
            event.accept()
        else:
            print("ignore")
            event.ignore()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = AppMainWindow()
    main.show()
    sys.exit(app.exec_())
