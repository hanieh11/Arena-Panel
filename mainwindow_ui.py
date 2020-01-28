# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui',
# licensing of 'mainwindow.ui' applies.
#
# Created: Sun Sep  1 18:52:51 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(472, 461)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.main_list = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_list.sizePolicy().hasHeightForWidth())
        self.main_list.setSizePolicy(sizePolicy)
        self.main_list.setMinimumSize(QtCore.QSize(200, 0))
        self.main_list.setMaximumSize(QtCore.QSize(200, 16777215))
        self.main_list.setObjectName("main_list")
        self.horizontalLayout_2.addWidget(self.main_list)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.sport_combo = QtWidgets.QComboBox(self.centralwidget)
        self.sport_combo.setEnabled(False)
        self.sport_combo.setObjectName("sport_combo")
        self.horizontalLayout.addWidget(self.sport_combo)
        self.add_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_btn.setEnabled(False)
        self.add_btn.setMaximumSize(QtCore.QSize(50, 16777215))
        self.add_btn.setFlat(False)
        self.add_btn.setObjectName("add_btn")
        self.horizontalLayout.addWidget(self.add_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.subClass_list = QtWidgets.QListWidget(self.centralwidget)
        self.subClass_list.setMinimumSize(QtCore.QSize(200, 0))
        self.subClass_list.setMaximumSize(QtCore.QSize(200, 16777215))
        self.subClass_list.setObjectName("subClass_list")
        self.verticalLayout.addWidget(self.subClass_list)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.formWidget = QtWidgets.QWidget(self.centralwidget)
        self.formWidget.setAutoFillBackground(True)
        self.formWidget.setObjectName("formWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.formWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.formWidgetLayout = QtWidgets.QVBoxLayout()
        self.formWidgetLayout.setObjectName("formWidgetLayout")
        self.horizontalLayout_3.addLayout(self.formWidgetLayout)
        self.horizontalLayout_2.addWidget(self.formWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar()
        self.menubar.setGeometry(QtCore.QRect(0, 0, 472, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.add_btn.setText(QtWidgets.QApplication.translate("MainWindow", "Add", None, -1))

