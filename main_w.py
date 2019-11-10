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
        self.element = []
        self.locker = False

        # - регистрирование доп окон
        self.tr_window = Trwindow(self)

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

        exit_button = QtWidgets.QAction(QtGui.QIcon(None), 'exit_button', self)
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
        """
        указание старой папки
        после чего должно выкинуть все файлы в старой и новой папке
        в место где лежит прога
        создать папку с датой + время,а в ней:
        папка старое
        папка новое
        папка результат
        вывод на основной экран результата действий
        """
        # проверка на пустые директории
        if self.new_file_path is None or self.new_file_path is '' or self.old_file_path is '':
            self.choose_directory()

        self.new_file_names, self.new_file_directory = self.file_list(self.new_file_path)
        self.old_file_names, self.old_file_directory = self.file_list(self.old_file_path)

        self.locker = False
        self.files_to_check = FileDialogWindow(self)
        self.files_to_check.exec()
        """
        после того, как результирующие папки получены
        происходит вызов функции, 
        которая выполняет парсинг, 
        отправляя в него имена файлов и их положение на пк
        """

        if self.locker is True:
            print("___________continue")

    @staticmethod
    def file_list(file_path):
        print(f'file_list {file_path}')
        file_names = []
        file_dir = []
        # r=root, d=directories, f=files
        for r, d, f in os.walk(file_path):
            for file in f:
                if '.yml' in file:
                    file_names.append(file)
                    file_dir.append(r)
        return file_names, file_dir

    # вызов окна для перевода файлов
    def translate_w(self):
        print('translate_w')
        self.tr_window.exec()

    # открытие файла
    def parse_file(self, file_name, raw_str=r'''(?P<key>^[A-Za-z._0-9]*):(?P<value>.*["]*)''', file_encoding="utf_8"):
        print(f'\n\n{"-_" *5}',
              '\nfile_name: ', file_name,
              '\nraw_str: ', raw_str,
              '\nencoding: ', file_encoding,
              '\nfile: \n')

        with open(file_name, "r", encoding=file_encoding) as stream:
            match_str = stream.read()
            parse_result = re.findall(raw_str, match_str, re.MULTILINE)
        self.element.append(parse_result)
        return parse_result

    # сравнение файлов
    @staticmethod
    def text_compare(b, d):
        filename = f'result{strftime("%H_%M")}.yml'
        with open(filename, 'w', encoding="utf-8-sig") as result_file:
            result_file.write('l_russian:\n')
            l_1 = []
            l_2 = []
            # сортировка старых ключей
            for i_1 in b:
                l_1.append(i_1[0])
            # сортировка новых ключей
            for i_2 in d:
                l_2.append(i_2[0])

            # поиск страых существующих ключей
            for m, n in enumerate(l_1):
                if n in l_2:
                    result_file.write(f'{b[m][0]}:{b[m][1]}\n')
                    print('старые живые', n)
            result_file.write(f'\n###НОЫЕ_СТРОКИ###\n\n')

            # поиск новых существующих ключей среди старых
            for j, i in enumerate(l_2):
                if i not in l_1:
                    result_file.write(f'{d[j][0]}:{d[j][1]}\n')
                    print('абсолютно новые', i)

        # перепись кодировки с винды на линку
        # мб и не нужно, но пускай будет
        windows_line_ending = b'\r\n'
        unix_line_ending = b'\n'
        with open(filename, 'rb') as file_data:
            file_text = file_data.read()
        file_text = file_text.replace(windows_line_ending, unix_line_ending)
        with open(filename, 'wb') as file_data:
            file_data.write(file_text)

    # собственно вызывает парсинг файлов
    def text_parse(self):
        """
        получение имен файлов
        """
        print('text_parse')
        a = input('Введите имя старого файла (с расширением): ')
        c = input('Введите имя нового файла (с расширением): ')
        b = self.parse_file(file_name=f'{os.path.dirname(__file__)}/{a}.yml')
        d = self.parse_file(file_name=f'{os.path.dirname(__file__)}/{c}.yml')
        print('\n\nрабочий каталог: ', os.path.abspath(__file__))
        self.text_compare(b, d)
        return print("\nFINISHED")

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
