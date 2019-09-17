import os
import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from translate_window import Tr_window
from file_dilog_window import FileButtons


class AppMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.new_file_path = 'E:/proektu/decoder_app/new_files'
        self.new_file_names = []
        self.new_file_directory = []

        self.old_file_path = 'E:/proektu/decoder_app/old_files'
        self.old_file_names = []
        self.old_file_directory = []

        self.result_dir_list = []
        self.result_files_list = []

        self.width = 640
        self.height = 480

        self.setMinimumSize(QtCore.QSize(self.width, self.height))
        self.setWindowIcon(QtGui.QIcon('img\\ico1.png'))
        self.setWindowTitle('Dzetto')

        self.statusBar().showMessage('for more information check info in main menu')
        self.text_box_1 = QtWidgets.QTextEdit(self)
        self.text_box_1.resize(self.width, self.height)
        self.text_box_1.move(0, 20)
        self.init_gui()
        # self.choose_directory()

    def init_gui(self):  # Need to add clean button
        print('def initGUI')
        main_menu = self.menuBar()
        file_menu = main_menu.addMenu('File')
        compare_menu = main_menu.addMenu('compared files')

        choose_dir = QtWidgets.QAction(QtGui.QIcon(None), 'choose_directory', self)
        choose_dir.setShortcut('Ctrl+Shift+D')
        # choose_dir.triggered.connect(self.choose_directory)
        file_menu.addAction(choose_dir)

        choose_scan_files = QtWidgets.QAction(QtGui.QIcon(None), 'choose_scan_files', self)
        choose_scan_files.setShortcut('Ctrl+Shift+F')
        choose_scan_files.triggered.connect(self.choose_scanned_files)
        compare_menu.addAction(choose_scan_files)

        scan_files = QtWidgets.QAction(QtGui.QIcon(None), 'scan_files', self)
        scan_files.setShortcut('Ctrl+Shift+G')
        scan_files.triggered.connect(self.scan_files_ev)
        compare_menu.addAction(scan_files)

        exit_button = QtWidgets.QAction(QtGui.QIcon(None), 'Exit', self)
        exit_button.setShortcut('Ctrl+Q')
        exit_button.triggered.connect(app.closeAllWindows)
        file_menu.addAction(exit_button)

    def choose_directory(self):
        print('def choose_directory')
        print('\nChoose_NEW_Directory')
        self.new_file_path = QtWidgets.QFileDialog().getExistingDirectory(
            None, "Select a new files folder")
        print("new directory: ", self.new_file_path, "\n")

        print('\nChoose_OLD_Directory')
        self.old_file_path = QtWidgets.QFileDialog().getExistingDirectory(
            None, "Select a old files folder")
        print("old directory: ", self.old_file_path, "\n")

    def choose_scanned_files(self):
        # call if was'nt
        # show if hided
        print('def choose_scanned_files')
        print(self.new_file_path)
        print(self.old_file_path)
        if self.new_file_path is None or self.new_file_path is '' or self.old_file_path is '':
            self.choose_directory()

        self.new_file_names, self.new_file_directory = self.file_list(self.new_file_path)
        self.old_file_names, self.old_file_directory = self.file_list(self.old_file_path)
        print(self.new_file_names, self.new_file_directory)
        print(self.old_file_names, self.old_file_directory)
        print('called choose_scanned_files')
        files_to_check = FileButtons(self)
        print("window call SUCCESS")
        files_to_check.show()
        files_to_check.exec()

    def file_list(self, file_path):
        print('def file_list')

        file_names = []
        file_dir = []
        # r=root, d=directories, f=files
        for r, d, f in os.walk(file_path):
            for file in f:
                while ('.yml' in file) and (file not in file_names):
                    file_names.append(file)
                    file_dir.append(r)
        return file_names, file_dir

    def scan_files_ev(self):
        # call if was'nt
        # show if hided
        print('called scan_files_ev')
        self.check_file = Tr_window(self)
        print("window call SUCCESS")
        self.check_file.show()
        self.check_file.exec()

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
