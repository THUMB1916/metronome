# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'metronome_window.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(667, 357)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("#centralwidget {border-image: url(:/images/res/background.jpg);}\n"
"\n"
"QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"}\n"
" \n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
" \n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"}\n"
" \n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
"                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);\n"
"}\n"
" \n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
" \n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
" \n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
" \n"
"QComboBox::down-arrow {\n"
"    image: url(/usr/share/icons/crystalsvg/16x16/actions/1downarrow.png);\n"
"}\n"
" \n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
"\n"
"QPushButton{border-style:none;padding:10px;border-radius:5px;color:#FFFFFF;background:#34495E;}\n"
"QPushButton:hover{color:#F0F0F0;background:#4E6D8C;}\n"
"QPushButton:pressed{color:#B8C6D1;background:#2D3E50;}\n"
"\n"
"QSlider::groove:horizontal,QSlider::add-page:horizontal{height:8px;border-radius:4px;background:#E8EDF2;}\n"
"QSlider::sub-page:horizontal{height:8px;border-radius:4px;background:#1ABC9C;}\n"
"QSlider::handle:horizontal{width:13px;margin-top:-3px;margin-bottom:-3px;border-radius:6px;background:qradialgradient(spread:pad,cx:0.5,cy:0.5,radius:0.5,fx:0.5,fy:0.5,stop:0.6 #FFFFFF,stop:0.8 #1ABC9C);}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(20, 0, 20, 0)
        self.horizontalLayout.setSpacing(100)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.button_80bpm = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(19)
        sizePolicy.setHeightForWidth(self.button_80bpm.sizePolicy().hasHeightForWidth())
        self.button_80bpm.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.button_80bpm.setFont(font)
        self.button_80bpm.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_80bpm.setStyleSheet("")
        self.button_80bpm.setObjectName("button_80bpm")
        self.horizontalLayout.addWidget(self.button_80bpm)
        self.button_100bpm = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_100bpm.sizePolicy().hasHeightForWidth())
        self.button_100bpm.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.button_100bpm.setFont(font)
        self.button_100bpm.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_100bpm.setStyleSheet("")
        self.button_100bpm.setObjectName("button_100bpm")
        self.horizontalLayout.addWidget(self.button_100bpm)
        self.button_120bpm = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_120bpm.sizePolicy().hasHeightForWidth())
        self.button_120bpm.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.button_120bpm.setFont(font)
        self.button_120bpm.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_120bpm.setAutoFillBackground(False)
        self.button_120bpm.setStyleSheet("")
        self.button_120bpm.setObjectName("button_120bpm")
        self.horizontalLayout.addWidget(self.button_120bpm)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(20, 0, 20, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.button_dec_bpm = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.button_dec_bpm.setFont(font)
        self.button_dec_bpm.setStyleSheet("")
        self.button_dec_bpm.setObjectName("button_dec_bpm")
        self.horizontalLayout_2.addWidget(self.button_dec_bpm)
        self.button_inc_bpm = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        self.button_inc_bpm.setFont(font)
        self.button_inc_bpm.setStyleSheet("")
        self.button_inc_bpm.setObjectName("button_inc_bpm")
        self.horizontalLayout_2.addWidget(self.button_inc_bpm)
        self.slider_bpm = QtWidgets.QSlider(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slider_bpm.sizePolicy().hasHeightForWidth())
        self.slider_bpm.setSizePolicy(sizePolicy)
        self.slider_bpm.setMinimum(1)
        self.slider_bpm.setMaximum(300)
        self.slider_bpm.setOrientation(QtCore.Qt.Horizontal)
        self.slider_bpm.setObjectName("slider_bpm")
        self.horizontalLayout_2.addWidget(self.slider_bpm)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 10)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_bpm = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        self.label_bpm.setFont(font)
        self.label_bpm.setAlignment(QtCore.Qt.AlignCenter)
        self.label_bpm.setObjectName("label_bpm")
        self.horizontalLayout_3.addWidget(self.label_bpm)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(20, 0, 20, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.combo_signature = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.combo_signature.setFont(font)
        self.combo_signature.setObjectName("combo_signature")
        self.horizontalLayout_6.addWidget(self.combo_signature)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.combo_division = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.combo_division.setFont(font)
        self.combo_division.setObjectName("combo_division")
        self.horizontalLayout_6.addWidget(self.combo_division)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_6.addWidget(self.label)
        self.combo_sound = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.combo_sound.setFont(font)
        self.combo_sound.setObjectName("combo_sound")
        self.horizontalLayout_6.addWidget(self.combo_sound)
        self.check_accent = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.check_accent.setFont(font)
        self.check_accent.setChecked(True)
        self.check_accent.setObjectName("check_accent")
        self.horizontalLayout_6.addWidget(self.check_accent)
        self.horizontalLayout_6.setStretch(1, 3)
        self.horizontalLayout_6.setStretch(3, 3)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(20, 0, 20, 0)
        self.horizontalLayout_4.setSpacing(100)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.button_play = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_play.sizePolicy().hasHeightForWidth())
        self.button_play.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.button_play.setFont(font)
        self.button_play.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_play.setStyleSheet("")
        self.button_play.setObjectName("button_play")
        self.horizontalLayout_4.addWidget(self.button_play)
        self.button_test = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_test.sizePolicy().hasHeightForWidth())
        self.button_test.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.button_test.setFont(font)
        self.button_test.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_test.setStyleSheet("")
        self.button_test.setObjectName("button_test")
        self.horizontalLayout_4.addWidget(self.button_test)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 2)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(4, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "节拍器"))
        self.button_80bpm.setText(_translate("MainWindow", "80 BPM"))
        self.button_100bpm.setText(_translate("MainWindow", "100 BPM"))
        self.button_120bpm.setText(_translate("MainWindow", "120 BPM"))
        self.button_dec_bpm.setText(_translate("MainWindow", "-"))
        self.button_inc_bpm.setText(_translate("MainWindow", "+"))
        self.label_bpm.setText(_translate("MainWindow", "80"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt;\">BPM</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "拍子"))
        self.label_6.setText(_translate("MainWindow", "划分"))
        self.label.setText(_translate("MainWindow", "音效"))
        self.check_accent.setText(_translate("MainWindow", "重音"))
        self.button_play.setText(_translate("MainWindow", "播放节拍"))
        self.button_test.setText(_translate("MainWindow", "节拍测试"))


import resources_rc
