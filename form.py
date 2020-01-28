from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QMessageBox
from form_ui import Ui_Form
from team import Team

class Form(QtWidgets.QWidget):

    formClosed = QtCore.Signal(str)


    def __init__(self):

        QtWidgets.QWidget.__init__(self)
        self.form = Ui_Form()
        self.form.setupUi(self)
        self.team = Team()
        self.form.teamWidgetLayout.addWidget(self.team)
        self.form.cancel_btn.clicked.connect(self.cancel)
        self.form.save_btn.clicked.connect(self.save)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

    def currentValues(self):
        values = []
        values.append(self.form.title_edit_3.text())
        date = self.form.dateTime_edit_3.dateTime()
        dateTime = QtCore.QDateTime.ToString(date,"yyyy-MM-ddTHH:mm:ss")
        values.append(dateTime)
        values.append(self.form.lig_combo_5.currentText)
        values.append(self.form.location_combo_3.currentText)
        values.append(self.form.description_edit_5.toPlainText)
        teams = []
        
    def cancel(self):
        msg_box = QMessageBox()
        msg_box.setText("If you cancel without saving current form, all your changes will be lost!")
        msg_box.setInformativeText("Do you want to cancel?")
        msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg_box.setDefaultButton(QMessageBox.Yes)
        msg_box.buttonClicked.connect(self.msgBtn)
        msg_box.exec_()

    def save(self):
        msg_box = QMessageBox()
        msg_box.setText("This form has been modified.")
        msg_box.setInformativeText("Do you want to save your changes?")
        msg_box.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
        msg_box.setDefaultButton(QMessageBox.Save)
        msg_box.buttonClicked.connect(self.msgBtn)
        msg_box.exec_()

    def msgBtn(self,btn):
        if btn.text() == "&Yes" :
            self.formClosed.emit("close")
        elif btn.text() == "Save" :
            self.formClosed.emit("save")
        elif btn.text() == "Don't Save" :
            self.formClosed.emit("close")
            
