# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'team.ui',
# licensing of 'team.ui' applies.
#
# Created: Sat Aug 10 15:37:39 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_teamWidget(object):
    def setupUi(self, teamWidget):
        teamWidget.setObjectName("teamWidget")
        teamWidget.resize(250, 381)
        teamWidget.setMinimumSize(QtCore.QSize(250, 0))
        self.verticalLayout = QtWidgets.QVBoxLayout(teamWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.upper_hlayout = QtWidgets.QHBoxLayout()
        self.upper_hlayout.setObjectName("upper_hlayout")
        self.team_list = QtWidgets.QListWidget(teamWidget)
        self.team_list.setObjectName("team_list")
        self.upper_hlayout.addWidget(self.team_list)
        self.delete_btn = QtWidgets.QPushButton(teamWidget)
        self.delete_btn.setMaximumSize(QtCore.QSize(100, 16777215))
        self.delete_btn.setObjectName("delete_btn")
        self.upper_hlayout.addWidget(self.delete_btn)
        self.verticalLayout.addLayout(self.upper_hlayout)
        self.bottom_hlayout = QtWidgets.QHBoxLayout()
        self.bottom_hlayout.setObjectName("bottom_hlayout")
        self.team_combo = QtWidgets.QComboBox(teamWidget)
        self.team_combo.setObjectName("team_combo")
        self.bottom_hlayout.addWidget(self.team_combo)
        self.add_btn = QtWidgets.QPushButton(teamWidget)
        self.add_btn.setMaximumSize(QtCore.QSize(100, 16777215))
        self.add_btn.setObjectName("add_btn")
        self.bottom_hlayout.addWidget(self.add_btn)
        self.verticalLayout.addLayout(self.bottom_hlayout)

        self.retranslateUi(teamWidget)
        QtCore.QMetaObject.connectSlotsByName(teamWidget)

    def retranslateUi(self, teamWidget):
        teamWidget.setWindowTitle(QtWidgets.QApplication.translate("teamWidget", "Form", None, -1))
        self.delete_btn.setText(QtWidgets.QApplication.translate("teamWidget", "Delete", None, -1))
        self.add_btn.setText(QtWidgets.QApplication.translate("teamWidget", "Add", None, -1))

