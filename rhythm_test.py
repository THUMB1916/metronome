# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rhythm_test.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(595, 227)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/res/icon_metronome.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("#centralwidget {border-image: url(:/images/res/background.jpg);}\n"
"\n"
"QPushButton{border-style:none;padding:10px;border-radius:5px;color:#FFFFFF;background:#34495E;}\n"
"QPushButton:hover{color:#F0F0F0;background:#4E6D8C;}\n"
"QPushButton:pressed{color:#B8C6D1;background:#2D3E50;}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_timer = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(24)
        self.label_timer.setFont(font)
        self.label_timer.setAlignment(QtCore.Qt.AlignCenter)
        self.label_timer.setObjectName("label_timer")
        self.verticalLayout.addWidget(self.label_timer)
        self.label_result = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.label_result.setFont(font)
        self.label_result.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.label_result.setText("")
        self.label_result.setObjectName("label_result")
        self.verticalLayout.addWidget(self.label_result)
        self.button_rhythm_test_stop = QtWidgets.QPushButton(self.centralwidget)
        self.button_rhythm_test_stop.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.button_rhythm_test_stop.setFont(font)
        self.button_rhythm_test_stop.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_rhythm_test_stop.setObjectName("button_rhythm_test_stop")
        self.verticalLayout.addWidget(self.button_rhythm_test_stop)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "节奏测试"))
        self.label_timer.setText(_translate("MainWindow", "0.00"))
        self.button_rhythm_test_stop.setText(_translate("MainWindow", "停止测试"))


import resources_rc
