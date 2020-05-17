from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
import user_interface
import glob
import serial
global form


class ExampleApp(QtWidgets.QMainWindow, user_interface.Ui_MainWindow):
    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(847, 588)


def setup_callbacks():
    for port in form.serial_ports():
        form.port_comboBox.addItem(port)
    pass


def main():
    global form
    app = QApplication(sys.argv)
    form = ExampleApp()
    setup_callbacks()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()