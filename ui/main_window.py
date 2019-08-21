# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1127, 639)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.local_camera_radio = QtWidgets.QRadioButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.local_camera_radio.sizePolicy().hasHeightForWidth())
        self.local_camera_radio.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(14)
        self.local_camera_radio.setFont(font)
        self.local_camera_radio.setAcceptDrops(False)
        self.local_camera_radio.setChecked(True)
        self.local_camera_radio.setObjectName("local_camera_radio")
        self.verticalLayout.addWidget(self.local_camera_radio)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.network_camera_radio = QtWidgets.QRadioButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.network_camera_radio.sizePolicy().hasHeightForWidth())
        self.network_camera_radio.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(14)
        self.network_camera_radio.setFont(font)
        self.network_camera_radio.setObjectName("network_camera_radio")
        self.verticalLayout_2.addWidget(self.network_camera_radio)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.rtsp_editline = QtWidgets.QLineEdit(self.centralwidget)
        self.rtsp_editline.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rtsp_editline.sizePolicy().hasHeightForWidth())
        self.rtsp_editline.setSizePolicy(sizePolicy)
        self.rtsp_editline.setObjectName("rtsp_editline")
        self.horizontalLayout_2.addWidget(self.rtsp_editline)
        self.confirm_button = QtWidgets.QPushButton(self.centralwidget)
        self.confirm_button.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.confirm_button.sizePolicy().hasHeightForWidth())
        self.confirm_button.setSizePolicy(sizePolicy)
        self.confirm_button.setObjectName("confirm_button")
        self.horizontalLayout_2.addWidget(self.confirm_button)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.record_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.record_button.sizePolicy().hasHeightForWidth())
        self.record_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        self.record_button.setFont(font)
        self.record_button.setObjectName("record_button")
        self.horizontalLayout.addWidget(self.record_button)
        self.imgrecord_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imgrecord_button.sizePolicy().hasHeightForWidth())
        self.imgrecord_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        self.imgrecord_button.setFont(font)
        self.imgrecord_button.setObjectName("imgrecord_button")
        self.horizontalLayout.addWidget(self.imgrecord_button)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.table = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table.sizePolicy().hasHeightForWidth())
        self.table.setSizePolicy(sizePolicy)
        self.table.setObjectName("table")
        self.table.setColumnCount(0)
        self.table.setRowCount(0)
        self.verticalLayout_3.addWidget(self.table)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.frame_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_label.sizePolicy().hasHeightForWidth())
        self.frame_label.setSizePolicy(sizePolicy)
        self.frame_label.setMinimumSize(QtCore.QSize(640, 480))
        self.frame_label.setMaximumSize(QtCore.QSize(1280, 960))
        self.frame_label.setStyleSheet("background-color: balck")
        self.frame_label.setObjectName("frame_label")
        self.horizontalLayout_3.addWidget(self.frame_label)
        self.frame_label.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.local_camera_radio.setText(_translate("MainWindow", "本地摄像头"))
        self.network_camera_radio.setText(_translate("MainWindow", "网络摄像头"))
        self.confirm_button.setText(_translate("MainWindow", "确认"))
        self.record_button.setText(_translate("MainWindow", "在线注册"))
        self.imgrecord_button.setText(_translate("MainWindow", "照片注册"))
        self.table.setSortingEnabled(False)
        self.frame_label.setText(_translate("MainWindow", "TextLabel"))
