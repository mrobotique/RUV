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


def button1_action():
    if form.lcdMag_1.value() == 0:
        form.lcdMag_1.display(1)
    else:
        form.lcdMag_1.display(0)


def serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result


def setup_callbacks():


    for port in serial_ports():
        print(port)
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