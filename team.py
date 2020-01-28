# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'team.ui',
# licensing of 'team.ui' applies.
#
# Created: Tue Aug  6 17:53:38 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!
from team_ui import Ui_teamWidget
from PySide2 import QtCore, QtGui, QtWidgets

class Team(QtWidgets.QWidget):
    def __init__(self):

        QtWidgets.QWidget.__init__(self)
        self.team = Ui_teamWidget()
        self.team.setupUi(self)
        
        self.team.team_combo.addItem("FCB")
        self.team.team_combo.addItem("Manchester")
        self.team.team_combo.addItem("Tottenham")
        self.team.team_combo.addItem("Chelsea")
        self.team.add_btn.clicked.connect(self._add)
        self.team.delete_btn.clicked.connect(self.deleteTeam)
    
    def _add(self):
        self.team.item =QtWidgets.QListWidgetItem(self.team.team_combo.currentText())
        self.addTeam(self.team.item)

    def addTeam(self,team):
        self.team.team_list.addItem(team)

    def deleteTeam(self):
        d_item = self.team.team_list.takeItem(self.team.team_list.currentRow())
        del d_item
        # self.team.team_list.repaint()