# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user_interface.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, QtSerialPort
from PyQt5.QtCore import QTimer
import time
import json
import sys
import glob
import serial

class Ui_MainWindow(object):
    def __init__(self):
        self.icon_ok = "./icons/green-led-on.png"
        self.icon_nok = "./icons/led-red-on.png"
        self.icon_uv = "./icons/led-uv.png"
        self.icon_off = "./icons/led-gray-off.png"
        self.comm_toggle = False
        self.sensor_names = ['deadman', 'pir1', 'pir2', 'pir3', 'pir4', 'mag1', 'mag2', 'mag3', 'mag4', 'mag5', 'mag6',
                             'lamp1', 'lamp2', 'lamp3', 'lamp4', 'lamp5', 'lamp6', 'lamp7', 'lamp8']
        # fill dict with 1
        self.data_dict = {self.sensor_names[i]: 0 for i in range(len(self.sensor_names))}
        self.comm_timeout = 1.3
        self.comm_last_time = 0
        self._timer_comm = QTimer(self)
        self._timer_comm.start(600) # Check every 600ms
        self._timer_comm.timeout.connect(self.check_comm)

        self.rgb_led = {
            "r":0,
            "g":1,
            "b":2,
            "w":3,
        }

        self.operation_mode = {
            'manual': 0,
            'auto': 1,
            'test': 2
        }

        self.comm_data = {
            "lamp1": 0,
            "lamp2": 0,
            "lamp3": 0,
            "lamp4": 0,
            "lamp5": 0,
            "lamp6": 0,
            "lamp7": 0,
            "lamp8": 0,
            "led_color": self.rgb_led['r'],
            "led_pwm": 0,
            "mode": 0
        }

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(847, 588)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(250, 10, 241, 291))
        self.groupBox.setObjectName("groupBox")
        self.lamp_button_8 = QtWidgets.QPushButton(self.groupBox)
        self.lamp_button_8.setGeometry(QtCore.QRect(160, 210, 51, 51))
        self.lamp_button_8.setObjectName("lamp_button_8")
        self.lamp_button_3 = QtWidgets.QPushButton(self.groupBox)
        self.lamp_button_3.setGeometry(QtCore.QRect(20, 150, 51, 51))
        self.lamp_button_3.setObjectName("lamp_button_3")
        self.lamp_button_6 = QtWidgets.QPushButton(self.groupBox)
        self.lamp_button_6.setGeometry(QtCore.QRect(160, 90, 51, 51))
        self.lamp_button_6.setObjectName("lamp_button_6")
        self.lamp_button_1 = QtWidgets.QPushButton(self.groupBox)
        self.lamp_button_1.setGeometry(QtCore.QRect(20, 30, 51, 51))
        self.lamp_button_1.setObjectName("lamp_button_1")
        self.lamp_button_4 = QtWidgets.QPushButton(self.groupBox)
        self.lamp_button_4.setGeometry(QtCore.QRect(20, 210, 51, 51))
        self.lamp_button_4.setObjectName("lamp_button_4")
        self.lamp_button_5 = QtWidgets.QPushButton(self.groupBox)
        self.lamp_button_5.setGeometry(QtCore.QRect(160, 30, 51, 51))
        self.lamp_button_5.setObjectName("lamp_button_5")
        self.lamp_button_2 = QtWidgets.QPushButton(self.groupBox)
        self.lamp_button_2.setGeometry(QtCore.QRect(20, 90, 51, 51))
        self.lamp_button_2.setObjectName("lamp_button_2")
        self.lamp_button_7 = QtWidgets.QPushButton(self.groupBox)
        self.lamp_button_7.setGeometry(QtCore.QRect(160, 150, 51, 51))
        self.lamp_button_7.setObjectName("lamp_button_7")
        self.led_lamp_1 = QtWidgets.QLabel(self.groupBox)
        self.led_lamp_1.setGeometry(QtCore.QRect(80, 50, 16, 16))
        self.led_lamp_1.setText("")
        self.led_lamp_1.setPixmap(QtGui.QPixmap("icons/led-gray-off.png"))
        self.led_lamp_1.setScaledContents(True)
        self.led_lamp_1.setObjectName("led_lamp_1")
        self.led_lamp_2 = QtWidgets.QLabel(self.groupBox)
        self.led_lamp_2.setGeometry(QtCore.QRect(80, 110, 16, 16))
        self.led_lamp_2.setText("")
        self.led_lamp_2.setPixmap(QtGui.QPixmap("icons/led-gray-off.png"))
        self.led_lamp_2.setScaledContents(True)
        self.led_lamp_2.setObjectName("led_lamp_2")
        self.led_lamp_3 = QtWidgets.QLabel(self.groupBox)
        self.led_lamp_3.setGeometry(QtCore.QRect(80, 170, 16, 16))
        self.led_lamp_3.setText("")
        self.led_lamp_3.setPixmap(QtGui.QPixmap("icons/led-gray-off.png"))
        self.led_lamp_3.setScaledContents(True)
        self.led_lamp_3.setObjectName("led_lamp_3")
        self.led_lamp_4 = QtWidgets.QLabel(self.groupBox)
        self.led_lamp_4.setGeometry(QtCore.QRect(80, 230, 16, 16))
        self.led_lamp_4.setText("")
        self.led_lamp_4.setPixmap(QtGui.QPixmap("icons/led-gray-off.png"))
        self.led_lamp_4.setScaledContents(True)
        self.led_lamp_4.setObjectName("led_lamp_4")
        self.led_lamp_5 = QtWidgets.QLabel(self.groupBox)
        self.led_lamp_5.setGeometry(QtCore.QRect(220, 50, 16, 16))
        self.led_lamp_5.setText("")
        self.led_lamp_5.setPixmap(QtGui.QPixmap("icons/led-gray-off.png"))
        self.led_lamp_5.setScaledContents(True)
        self.led_lamp_5.setObjectName("led_lamp_5")
        self.led_lamp_6 = QtWidgets.QLabel(self.groupBox)
        self.led_lamp_6.setGeometry(QtCore.QRect(220, 110, 16, 16))
        self.led_lamp_6.setText("")
        self.led_lamp_6.setPixmap(QtGui.QPixmap("icons/led-gray-off.png"))
        self.led_lamp_6.setScaledContents(True)
        self.led_lamp_6.setObjectName("led_lamp_6")
        self.led_lamp_7 = QtWidgets.QLabel(self.groupBox)
        self.led_lamp_7.setGeometry(QtCore.QRect(220, 170, 16, 16))
        self.led_lamp_7.setText("")
        self.led_lamp_7.setPixmap(QtGui.QPixmap("icons/led-gray-off.png"))
        self.led_lamp_7.setScaledContents(True)
        self.led_lamp_7.setObjectName("led_lamp_7")
        self.led_lamp_8 = QtWidgets.QLabel(self.groupBox)
        self.led_lamp_8.setGeometry(QtCore.QRect(220, 230, 16, 16))
        self.led_lamp_8.setText("")
        self.led_lamp_8.setPixmap(QtGui.QPixmap("icons/led-gray-off.png"))
        self.led_lamp_8.setScaledContents(True)
        self.led_lamp_8.setObjectName("led_lamp_8")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(560, 430, 261, 101))
        self.groupBox_2.setObjectName("groupBox_2")
        self.port_comboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.port_comboBox.setGeometry(QtCore.QRect(10, 30, 241, 27))
        self.port_comboBox.setObjectName("port_comboBox")
        self.commButton = QtWidgets.QPushButton(self.groupBox_2)
        self.commButton.setGeometry(QtCore.QRect(10, 60, 241, 27))
        self.commButton.setObjectName("commButton")
        self.led_comm = QtWidgets.QLabel(self.groupBox_2)
        self.led_comm.setGeometry(QtCore.QRect(240, 10, 16, 16))
        self.led_comm.setText("")
        self.led_comm.setPixmap(QtGui.QPixmap("icons/led-gray-off.png"))
        self.led_comm.setScaledContents(True)
        self.led_comm.setObjectName("led_comm")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(540, 10, 301, 271))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setGeometry(QtCore.QRect(30, 40, 41, 17))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 41, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(30, 120, 41, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(30, 160, 41, 17))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(30, 200, 41, 17))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(30, 240, 41, 17))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setGeometry(QtCore.QRect(210, 40, 31, 17))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_8.setGeometry(QtCore.QRect(210, 80, 31, 17))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setGeometry(QtCore.QRect(210, 120, 31, 17))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox_3)
        self.label_10.setGeometry(QtCore.QRect(210, 160, 31, 17))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox_3)
        self.label_11.setGeometry(QtCore.QRect(170, 240, 67, 17))
        self.label_11.setObjectName("label_11")
        self.led_Mag_1 = QtWidgets.QLabel(self.groupBox_3)
        self.led_Mag_1.setGeometry(QtCore.QRect(80, 40, 16, 16))
        self.led_Mag_1.setText("")
        self.led_Mag_1.setPixmap(QtGui.QPixmap("icons/led-gray-off.png"))
        self.led_Mag_1.setScaledContents(True)
        self.led_Mag_1.setObjectName("led_Mag_1")
        self.led_Mag_2 = QtWidgets.QLabel(self.groupBox_3)
        self.led_Mag_2.setGeometry(QtCore.QRect(80, 80, 16, 16))
        self.led_Mag_2.setText("")
        self.led_Mag_2.setPixmap(QtGui.QPixmap("icons/led-gray-off.png"))
        self.led_Mag_2.setScaledContents(True)
        self.led_Mag_2.setObjectName("led_Mag_2")
        self.led_Mag_3 = QtWidgets.QLabel(self.groupBox_3)
        self.led_Mag_3.setGeometry(QtCore.QRect(80, 120, 16, 16))
        self.led_Mag_3.setText("")
        self.led_Mag_3.setPixmap(QtGui.QPixmap("icons/led-gray-off.png"))
        self.led_Mag_3.setScaledContents(True)
        self.led_Mag_3.setObjectName("led_Mag_3")
        self.led_Mag_4 = QtWidgets.QLabel(self.groupBox_3)
        self.led_Mag_4.setGeometry(QtCore.QRect(80, 160, 16, 16))
        self.led_Mag_4.setText("")
        self.led_Mag_4.setPixmap(QtGui.QPixmap("icons/led-gray-off.png"))
        self.led_Mag_4.setScaledContents(True)
        self.led_Mag_4.setObjectName("led_Mag_4")
        self.led_Mag_5 = QtWidgets.QLabel(self.groupBox_3)
        self.led_Mag_5.setGeometry(QtCore.QRect(80, 200, 16, 16))
        self.led_Mag_5.setText("")
        self.led_Mag_5.setPixmap(QtGui.QPixmap("icons/led-gray-off.png"))
        self.led_Mag_5.setScaledContents(True)
        self.led_Mag_5.setObjectName("led_Mag_5")
        self.led_Mag_6 = QtWidgets.QLabel(self.groupBox_3)
        self.led_Mag_6.setGeometry(QtCore.QRect(80, 240, 16, 16))
        self.led_Mag_6.setText("")
        self.led_Mag_6.setPixmap(QtGui.QPixmap("icons/led-gray-off.png"))
        self.led_Mag_6.setScaledContents(True)
        self.led_Mag_6.setObjectName("led_Mag_6")
        self.led_pir_1 = QtWidgets.QLabel(self.groupBox_3)
        self.led_pir_1.setGeometry(QtCore.QRect(250, 40, 16, 16))
        self.led_pir_1.setText("")
        self.led_pir_1.setPixmap(QtGui.QPixmap("icons/led-gray-off.png"))
        self.led_pir_1.setScaledContents(True)
        self.led_pir_1.setObjectName("led_pir_1")
        self.led_pir_2 = QtWidgets.QLabel(self.groupBox_3)
        self.led_pir_2.setGeometry(QtCore.QRect(250, 80, 16, 16))
        self.led_pir_2.setText("")
        self.led_pir_2.setPixmap(QtGui.QPixmap("icons/led-gray-off.png"))
        self.led_pir_2.setScaledContents(True)
        self.led_pir_2.setObjectName("led_pir_2")
        self.led_pir_3 = QtWidgets.QLabel(self.groupBox_3)
        self.led_pir_3.setGeometry(QtCore.QRect(250, 120, 16, 16))
        self.led_pir_3.setText("")
        self.led_pir_3.setPixmap(QtGui.QPixmap("icons/led-gray-off.png"))
        self.led_pir_3.setScaledContents(True)
        self.led_pir_3.setObjectName("led_pir_3")
        self.led_pir_4 = QtWidgets.QLabel(self.groupBox_3)
        self.led_pir_4.setGeometry(QtCore.QRect(250, 160, 16, 16))
        self.led_pir_4.setText("")
        self.led_pir_4.setPixmap(QtGui.QPixmap("icons/led-gray-off.png"))
        self.led_pir_4.setScaledContents(True)
        self.led_pir_4.setObjectName("led_pir_4")
        self.led_deadman = QtWidgets.QLabel(self.groupBox_3)
        self.led_deadman.setGeometry(QtCore.QRect(250, 240, 16, 16))
        self.led_deadman.setText("")
        self.led_deadman.setPixmap(QtGui.QPixmap("icons/led-gray-off.png"))
        self.led_deadman.setScaledContents(True)
        self.led_deadman.setObjectName("led_deadman")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(550, 310, 271, 101))
        self.groupBox_4.setObjectName("groupBox_4")
        self.radioMode_1 = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioMode_1.setGeometry(QtCore.QRect(10, 30, 117, 21))
        self.radioMode_1.setObjectName("radioMode_1")
        self.radioMode_2 = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioMode_2.setGeometry(QtCore.QRect(10, 50, 117, 21))
        self.radioMode_2.setObjectName("radioMode_2")
        self.radioMode_3 = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioMode_3.setGeometry(QtCore.QRect(10, 70, 117, 21))
        self.radioMode_3.setChecked(True)
        self.radioMode_3.setObjectName("radioMode_3")
        self.timer_button = QtWidgets.QPushButton(self.groupBox_4)
        self.timer_button.setGeometry(QtCore.QRect(130, 30, 131, 61))
        self.timer_button.setObjectName("timer_button")
        self.led_timer = QtWidgets.QLabel(self.groupBox_4)
        self.led_timer.setGeometry(QtCore.QRect(100, 50, 16, 16))
        self.led_timer.setText("")
        self.led_timer.setPixmap(QtGui.QPixmap("icons/led-gray-off.png"))
        self.led_timer.setScaledContents(True)
        self.led_timer.setObjectName("led_timer")
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(250, 310, 251, 211))
        self.groupBox_5.setMouseTracking(True)
        self.groupBox_5.setFlat(True)
        self.groupBox_5.setCheckable(False)
        self.groupBox_5.setObjectName("groupBox_5")
        self.conf_timer_button = QtWidgets.QPushButton(self.groupBox_5)
        self.conf_timer_button.setGeometry(QtCore.QRect(0, 156, 241, 51))
        self.conf_timer_button.setObjectName("conf_timer_button")
        self.lcdNumber = QtWidgets.QLCDNumber(self.groupBox_5)
        self.lcdNumber.setGeometry(QtCore.QRect(170, 80, 61, 41))
        self.lcdNumber.setDigitCount(3)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber.setProperty("intValue", 0)
        self.lcdNumber.setObjectName("lcdNumber")
        self.label_12 = QtWidgets.QLabel(self.groupBox_5)
        self.label_12.setGeometry(QtCore.QRect(170, 60, 61, 17))
        self.label_12.setObjectName("label_12")
        self.timer_dial = QtWidgets.QDial(self.groupBox_5)
        self.timer_dial.setGeometry(QtCore.QRect(10, 20, 141, 131))
        self.timer_dial.setMaximum(180)
        self.timer_dial.setProperty("value", 0)
        self.timer_dial.setInvertedAppearance(False)
        self.timer_dial.setInvertedControls(False)
        self.timer_dial.setObjectName("dial")
        self.labelLogo = QtWidgets.QLabel(self.centralwidget)
        self.labelLogo.setGeometry(QtCore.QRect(-20, 20, 261, 251))
        self.labelLogo.setText("")
        self.labelLogo.setPixmap(QtGui.QPixmap("icons/logo.png"))
        self.labelLogo.setScaledContents(True)
        self.labelLogo.setObjectName("labelLogo")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(520, 40, 16, 471))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(220, 40, 16, 481))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.groupBox_6 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_6.setGeometry(QtCore.QRect(10, 310, 211, 211))
        self.groupBox_6.setObjectName("groupBox_6")
        self.radio_Led_R = QtWidgets.QRadioButton(self.groupBox_6)
        self.radio_Led_R.setGeometry(QtCore.QRect(10, 40, 117, 22))
        self.radio_Led_R.setChecked(True)
        self.radio_Led_R.setObjectName("radio_Led_R")
        self.radio_Led_G = QtWidgets.QRadioButton(self.groupBox_6)
        self.radio_Led_G.setGeometry(QtCore.QRect(10, 70, 117, 22))
        self.radio_Led_G.setObjectName("radio_Led_G")
        self.radio_Led_B = QtWidgets.QRadioButton(self.groupBox_6)
        self.radio_Led_B.setGeometry(QtCore.QRect(10, 100, 117, 22))
        self.radio_Led_B.setObjectName("radio_Led_B")
        self.radioButton_W = QtWidgets.QRadioButton(self.groupBox_6)
        self.radioButton_W.setGeometry(QtCore.QRect(10, 130, 117, 22))
        self.radioButton_W.setObjectName("radioButton_W")
        self.horizontalSlider_LedPower = QtWidgets.QSlider(self.groupBox_6)
        self.horizontalSlider_LedPower.setGeometry(QtCore.QRect(10, 180, 181, 31))
        self.horizontalSlider_LedPower.setMaximum(255)
        self.horizontalSlider_LedPower.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_LedPower.setObjectName("horizontalSlider_LedPower")
        self.label_14 = QtWidgets.QLabel(self.groupBox_6)
        self.label_14.setGeometry(QtCore.QRect(10, 160, 71, 17))
        self.label_14.setObjectName("label_14")
        self.labelLogo.raise_()
        self.groupBox.raise_()
        self.groupBox_2.raise_()
        self.groupBox_3.raise_()
        self.groupBox_4.raise_()
        self.groupBox_5.raise_()
        self.line_3.raise_()
        self.line.raise_()
        self.groupBox_6.raise_()

        #set buttons callbacks
        self.commButton.clicked.connect(self.on_toggled)
        self.timer_dial.valueChanged.connect(self.timer_dial_change)
        self.lamp_button_1.clicked.connect(self.buttons_cb)
        self.lamp_button_2.clicked.connect(self.buttons_cb)
        self.lamp_button_3.clicked.connect(self.buttons_cb)
        self.lamp_button_4.clicked.connect(self.buttons_cb)
        self.lamp_button_5.clicked.connect(self.buttons_cb)
        self.lamp_button_6.clicked.connect(self.buttons_cb)
        self.lamp_button_7.clicked.connect(self.buttons_cb)
        self.lamp_button_8.clicked.connect(self.buttons_cb)
        self.timer_button.clicked.connect(self.buttons_cb)
        self.conf_timer_button.clicked.connect(self.buttons_cb)
        self.radio_Led_R.toggled.connect(self.rgb_led_cb)
        self.radio_Led_G.toggled.connect(self.rgb_led_cb)
        self.radio_Led_B.toggled.connect(self.rgb_led_cb)
        self.radioButton_W.toggled.connect(self.rgb_led_cb)
        self.horizontalSlider_LedPower.valueChanged.connect(self.rgb_led_cb)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 847, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Lamparas"))
        self.lamp_button_8.setText(_translate("MainWindow", "Opt2"))
        self.lamp_button_3.setText(_translate("MainWindow", "L3"))
        self.lamp_button_6.setText(_translate("MainWindow", "L6"))
        self.lamp_button_1.setText(_translate("MainWindow", "L1"))
        self.lamp_button_4.setText(_translate("MainWindow", "L4"))
        self.lamp_button_5.setText(_translate("MainWindow", "L5"))
        self.lamp_button_2.setText(_translate("MainWindow", "L2"))
        self.lamp_button_7.setText(_translate("MainWindow", "Opt1"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Puerto Serie"))
        self.commButton.setText(_translate("MainWindow", "Conectar"))
        self.commButton.setCheckable(True)
        self.groupBox_3.setTitle(_translate("MainWindow", "Sensores "))
        self.label.setText(_translate("MainWindow", "Mag1"))
        self.label_2.setText(_translate("MainWindow", "Mag2"))
        self.label_3.setText(_translate("MainWindow", "Mag3"))
        self.label_4.setText(_translate("MainWindow", "Mag4"))
        self.label_5.setText(_translate("MainWindow", "Mag5"))
        self.label_6.setText(_translate("MainWindow", "Mag6"))
        self.label_7.setText(_translate("MainWindow", "PIR1"))
        self.label_8.setText(_translate("MainWindow", "PIR2"))
        self.label_9.setText(_translate("MainWindow", "PIR3"))
        self.label_10.setText(_translate("MainWindow", "PIR4"))
        self.label_11.setText(_translate("MainWindow", "Deadman"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Modo de operaccion"))
        self.radioMode_1.setText(_translate("MainWindow", "A&uto"))
        self.radioMode_2.setText(_translate("MainWindow", "Manua&l"))
        self.radioMode_3.setText(_translate("MainWindow", "Test"))
        self.timer_button.setText(_translate("MainWindow", "Timer Test"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Confi&guracion de timer"))
        self.conf_timer_button.setText(_translate("MainWindow", "Confirmar"))
        self.label_12.setText(_translate("MainWindow", "Minutos"))
        self.groupBox_6.setTitle(_translate("MainWindow", "LED Test"))
        self.radio_Led_R.setText(_translate("MainWindow", "Ro&jo"))
        self.radio_Led_G.setText(_translate("MainWindow", "Verde"))
        self.radio_Led_B.setText(_translate("MainWindow", "A&zul"))
        self.radioButton_W.setText(_translate("MainWindow", "Blanco"))
        self.label_14.setText(_translate("MainWindow", "Intensidad"))

    ## Otras funciones no creadas con el qt5 designer
    @QtCore.pyqtSlot()
    def receive(self):

        if self.comm_toggle:
            self.comm_toggle = False
            self.led_comm.setPixmap(QtGui.QPixmap(self.icon_ok))
        else:
            self.comm_toggle = True
            self.led_comm.setPixmap(QtGui.QPixmap(self.icon_nok))

        while self.serial.canReadLine():
            self.comm_last_time = time.time()
            data_txt = self.serial.readLine().data().decode()
            data_txt = data_txt.rstrip('\r\n')
            data_json = json.loads(data_txt)
            # using dictionary comprehension
            # to convert lists to dictionary
            self.data_dict = {self.sensor_names[i]: data_json['data'][i] for i in range(len(data_json['data']))}
            #UPDATE LEDS (Todos en logica inversa por que tiene pull up": si el sensor detecta --> 0)
            if self.data_dict['deadman'] == 1:
                self.led_deadman.setPixmap(QtGui.QPixmap(self.icon_nok))
            else:
                self.led_deadman.setPixmap(QtGui.QPixmap(self.icon_ok))
            # Pir Sensors
            if self.data_dict['pir1'] == 1:
                self.led_pir_1.setPixmap(QtGui.QPixmap(self.icon_nok))
            else:
                self.led_pir_1.setPixmap(QtGui.QPixmap(self.icon_ok))

            if self.data_dict['pir2'] == 1:
                self.led_pir_2.setPixmap(QtGui.QPixmap(self.icon_nok))
            else:
                self.led_pir_2.setPixmap(QtGui.QPixmap(self.icon_ok))

            if self.data_dict['pir3'] == 1:
                self.led_pir_3.setPixmap(QtGui.QPixmap(self.icon_nok))
            else:
                self.led_pir_3.setPixmap(QtGui.QPixmap(self.icon_ok))

            if self.data_dict['pir4'] == 1:
                self.led_pir_4.setPixmap(QtGui.QPixmap(self.icon_nok))
            else:
                self.led_pir_4.setPixmap(QtGui.QPixmap(self.icon_ok))

            # Magnetic Sensors
            if self.data_dict['mag1'] == 1:
                self.led_Mag_1.setPixmap(QtGui.QPixmap(self.icon_nok))
            else:
                self.led_Mag_1.setPixmap(QtGui.QPixmap(self.icon_ok))

            if self.data_dict['mag2'] == 1:
                self.led_Mag_2.setPixmap(QtGui.QPixmap(self.icon_nok))
            else:
                self.led_Mag_2.setPixmap(QtGui.QPixmap(self.icon_ok))

            if self.data_dict['mag3'] == 1:
                self.led_Mag_3.setPixmap(QtGui.QPixmap(self.icon_nok))
            else:
                self.led_Mag_3.setPixmap(QtGui.QPixmap(self.icon_ok))

            if self.data_dict['mag4'] == 1:
                self.led_Mag_4.setPixmap(QtGui.QPixmap(self.icon_nok))
            else:
                self.led_Mag_4.setPixmap(QtGui.QPixmap(self.icon_ok))

            if self.data_dict['mag5'] == 1:
                self.led_Mag_5.setPixmap(QtGui.QPixmap(self.icon_nok))
            else:
                self.led_Mag_5.setPixmap(QtGui.QPixmap(self.icon_ok))

            if self.data_dict['mag6'] == 1:
                self.led_Mag_6.setPixmap(QtGui.QPixmap(self.icon_nok))
            else:
                self.led_Mag_6.setPixmap(QtGui.QPixmap(self.icon_ok))

            #LAMPARAS (Relevadores) Estos si tienen logica directa 1=on/ 0=off
            if self.data_dict['lamp1'] == 1:
                self.led_lamp_1.setPixmap(QtGui.QPixmap(self.icon_uv))
            else:
                self.led_lamp_1.setPixmap(QtGui.QPixmap(self.icon_off))

            if self.data_dict['lamp2'] == 1:
                self.led_lamp_2.setPixmap(QtGui.QPixmap(self.icon_uv))
            else:
                self.led_lamp_2.setPixmap(QtGui.QPixmap(self.icon_off))

            if self.data_dict['lamp3'] == 1:
                self.led_lamp_3.setPixmap(QtGui.QPixmap(self.icon_uv))
            else:
                self.led_lamp_3.setPixmap(QtGui.QPixmap(self.icon_off))

            if self.data_dict['lamp4'] == 1:
                self.led_lamp_4.setPixmap(QtGui.QPixmap(self.icon_uv))
            else:
                self.led_lamp_4.setPixmap(QtGui.QPixmap(self.icon_off))

            if self.data_dict['lamp5'] == 1:
                self.led_lamp_5.setPixmap(QtGui.QPixmap(self.icon_uv))
            else:
                self.led_lamp_5.setPixmap(QtGui.QPixmap(self.icon_off))

            if self.data_dict['lamp6'] == 1:
                self.led_lamp_6.setPixmap(QtGui.QPixmap(self.icon_uv))
            else:
                self.led_lamp_6.setPixmap(QtGui.QPixmap(self.icon_off))

            if self.data_dict['lamp7'] == 1:
                self.led_lamp_7.setPixmap(QtGui.QPixmap(self.icon_uv))
            else:
                self.led_lamp_7.setPixmap(QtGui.QPixmap(self.icon_off))

            if self.data_dict['lamp8'] == 1:
                self.led_lamp_8.setPixmap(QtGui.QPixmap(self.icon_uv))
            else:
                self.led_lamp_8.setPixmap(QtGui.QPixmap(self.icon_off))

    @QtCore.pyqtSlot()
    def send(self):
        self.serial.write(self.message_le.text().encode())

    @QtCore.pyqtSlot(bool)
    def on_toggled(self, checked):
        self.serial = QtSerialPort.QSerialPort(
            self.port_comboBox.currentText(),
            baudRate=QtSerialPort.QSerialPort.Baud115200,
            readyRead=self.receive)
        self.commButton.setText("Desconectar" if checked else "Conectar")

        if checked:
            if not self.serial.isOpen():
                if not self.serial.open(QtCore.QIODevice.ReadWrite):
                    self.serial.clear()
                    self.commButton.setChecked(False)
        else:
            self.serial.close()
            self.led_comm.setPixmap(QtGui.QPixmap(self.icon_off))
            self.port_comboBox.clear()
            for port in self.serial_ports():
                self.port_comboBox.addItem(port)


    def timer_dial_change(self):
        self.lcdNumber.display(self.timer_dial.value())

    def rgb_led_cb(self):
        sender = self.sender().objectName()
        print(sender)
        if sender == "horizontalSlider_LedPower":
            self.comm_data["pwm"] = self.horizontalSlider_LedPower.value()
        if self.radio_Led_R.isChecked():
            self.comm_data["led_color"] = self.rgb_led['r']
        if self.radio_Led_G.isChecked():
            self.comm_data["led_color"] = self.rgb_led['g']
        if self.radio_Led_B.isChecked():
            self.comm_data["led_color"] = self.rgb_led['b']
        if self.radioButton_W.isChecked():
            self.comm_data["led_color"] = self.rgb_led['w']
        print(self.comm_data)

    def serial_ports(self):
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

    def check_comm(self):
        if (time.time() - self.comm_last_time) > self.comm_timeout :
            # Todos los leds a negro
            self.led_deadman.setPixmap(QtGui.QPixmap(self.icon_off))
            self.led_pir_1.setPixmap(QtGui.QPixmap(self.icon_off))
            self.led_pir_2.setPixmap(QtGui.QPixmap(self.icon_off))
            self.led_pir_3.setPixmap(QtGui.QPixmap(self.icon_off))
            self.led_pir_4.setPixmap(QtGui.QPixmap(self.icon_off))
            self.led_Mag_1.setPixmap(QtGui.QPixmap(self.icon_off))
            self.led_Mag_2.setPixmap(QtGui.QPixmap(self.icon_off))
            self.led_Mag_3.setPixmap(QtGui.QPixmap(self.icon_off))
            self.led_Mag_4.setPixmap(QtGui.QPixmap(self.icon_off))
            self.led_Mag_5.setPixmap(QtGui.QPixmap(self.icon_off))
            self.led_Mag_6.setPixmap(QtGui.QPixmap(self.icon_off))
            self.led_lamp_1.setPixmap(QtGui.QPixmap(self.icon_off))
            self.led_lamp_2.setPixmap(QtGui.QPixmap(self.icon_off))
            self.led_lamp_3.setPixmap(QtGui.QPixmap(self.icon_off))
            self.led_lamp_4.setPixmap(QtGui.QPixmap(self.icon_off))
            self.led_lamp_5.setPixmap(QtGui.QPixmap(self.icon_off))
            self.led_lamp_6.setPixmap(QtGui.QPixmap(self.icon_off))
            self.led_lamp_7.setPixmap(QtGui.QPixmap(self.icon_off))
            self.led_lamp_8.setPixmap(QtGui.QPixmap(self.icon_off))
            self.led_comm.setPixmap(QtGui.QPixmap(self.icon_off))

    def buttons_cb(self):
        sender = self.sender().objectName()
        for i in range(1, 9): #Lee todos el estado de las lamparas desde el mircro y pone el estado inverso
                              # en el sring que se enviara para actualizar las salidas del microcontrolador
            sender_name = "lamp_button_" + str(i)
            key_name = "lamp" + str(i)
            if sender == sender_name:
                if self.data_dict[key_name] == 1:
                    self.comm_data[key_name] = 0
                else:
                    self.comm_data[key_name] = 1

        if sender == "conf_timer_button":
            #             ToDo: Enviar la configuracion de tiempo para el timer de la lampara
            #             ToDo: Este valor sera guardado en la EEPROM del arduino y es el tiempo
            #             ToDo: que durara prendida la lampara cuando se lance el automatico
            time_to_send = self.lcdNumber.value()
            print(time_to_send)

        if sender == "timer_button":
#             ToDo: Enviar al micro el comando de start/stop para el timer
            print("timer_button: Funcion no implementada")