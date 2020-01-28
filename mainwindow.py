from mainwindow_ui import Ui_MainWindow
from PySide2 import QtCore, QtGui, QtWidgets
from form import Form
from PySide2 import QtNetwork
import json


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.sports = []
        self.ui.add_btn.clicked.connect(self._newForm)

        self.ui.item1 = QtWidgets.QListWidgetItem("Events")
        self.ui.main_list.addItem(self.ui.item1)
        self.ui.item2 = QtWidgets.QListWidgetItem("Results")
        self.ui.main_list.addItem(self.ui.item2)
        self.ui.main_list.itemClicked.connect(self._mainClicked)

        self.manager = QtNetwork.QNetworkAccessManager()
        self.sport_req = QtNetwork.QNetworkRequest(QtCore.QUrl("http://aseman.io:3000/api/sports"))
        self.sport_reply = self.manager.get(self.sport_req)
        self.sport_reply.finished.connect(self._sportsReply)

        self.ui.sport_combo.activated.connect(self._mainReq)
        self.ui.subClass_list.itemClicked.connect(self._loadForm)
        self.sport_dic = {}
        self.loaded = []
        self.resizeTimer = QtCore.QTimer()
        self.resizeTimer.setSingleShot(True)
        self.resizeTimer.timeout.connect(self.tryResize)
        
    def _mainReq(self):
        self.ui.subClass_list.clear()
        self.ui.add_btn.setEnabled(True)
        self.selected_sport = self.sport_dic.get(self.ui.sport_combo.currentText())
        selected = self.ui.main_list.currentItem()
        if selected.text() == "Events" :
            dic = {
                "offset" : 0,
                "limit" : 100,
                "sport_id" : self.selected_sport
            }
            vari_req = QtCore.QJsonDocument.fromVariant(dic)
            json_req = QtCore.QJsonDocument.toJson(vari_req)

            req = QtNetwork.QNetworkRequest(QtCore.QUrl("http://aseman.io:3000/api/events"))
            req.setHeader(QtNetwork.QNetworkRequest.ContentTypeHeader, "application/json")
            self.event_reply = self.manager.post(req,json_req)
            self.event_reply.finished.connect(self._eventsReply)

        if selected.text() == "Results":
            pass

    def _loadForm(self,item):
        i = self.ui.subClass_list.currentRow()
        self.form = Form()
        self.ui.formWidgetLayout.addWidget(self.form)
        self.form.formClosed.connect(self._closeForm)

        title = self.events["message"][i]["title"]
        self.loaded.append(title)
        self.form.form.title_edit_3.setText(title)

        dateTime = str(self.events["message"][i]["event_time"])[0:19]
        date = QtCore.QDateTime.fromString(dateTime,"yyyy-MM-ddTHH:mm:ss")
        self.form.form.dateTime_edit_3.setDateTime(date)
        self.loaded.append(dateTime)   ####fix this after Ali comes!

        description = self.events["message"][i]["description"]
        self.form.form.description_edit_5.append(description)
        self.loaded.append(description)

        self.event_id = self.events["message"][i]["id"]

        league = self.events["message"][i]["league"]["name"]
        self.form.form.lig_combo_5.addItem(league)
        self.loaded.append(league)
        self.leaguesReq(self.selected_sport)

        location = self.events["message"][i]["location"]["address"]+ " "+ self.events["message"][i]["location"]["name"]+ " "+ self.events["message"][i]["location"]["city"]
        self.form.form.location_combo_3.addItem(location)
        self.loaded.append(location)
        teams =[]
        for j in range(len(self.events["message"][i]["teams"])):
            self.form.team.addTeam(self.events["message"][i]["teams"][j]["name"])
            teams.append(self.events["message"][i]["teams"][j]["name"])
        self.loaded.append(teams)

    def _eventsReply(self):
        reply_file = self.event_reply.readAll()
        json_file = QtCore.QJsonDocument.fromJson(reply_file)
        self.events = json_file.toVariant()
        # print(self.events)

        for i in range(len(self.events["message"])):
            self.ui.subClass_list.addItem(str(self.events["message"][i]["title"]))

    def leaguesReq (self,sport_id):

        dic = {
            "sports":[
                {
                    "id":sport_id
                }
            ]
        }
        vari_req = QtCore.QJsonDocument.fromVariant(dic)
        json_req = QtCore.QJsonDocument.toJson(vari_req)

        req = QtNetwork.QNetworkRequest(QtCore.QUrl("http://aseman.io:3000/api/leagues"))
        req.setHeader(QtNetwork.QNetworkRequest.ContentTypeHeader, "application/json")
        self.league_reply = self.manager.post(req,json_req)
        self.league_reply.finished.connect(self._leaguesReply)

    def _leaguesReply(self):
        reply_file = self.league_reply.readAll()
        json_file = QtCore.QJsonDocument.fromJson(reply_file)
        v = json_file.toVariant()
        for i in range(len(v["message"])):
            self.form.form.lig_combo_5.addItem(v["message"][i]["name"])

    def _sportsReply(self):
        reply_file = self.sport_reply.readAll()
        json_file = QtCore.QJsonDocument.fromJson(reply_file)
        v = json_file.toVariant() #changing variant of c++ to normal python variable that can be anything
        for i in range(len(v["message"])) :
            self.sport_dic.update({v["message"][i]["name"] : v["message"][i]["id"]})
            self.ui.sport_combo.addItem(v["message"][i]["name"])

    def _mainClicked(self):
        try:
            self.form.cancel()
        except AttributeError:
            self.ui.sport_combo.setEnabled(True)
        

    def _newForm (self):
        self.ui.add_btn.setDisabled(True)
        self.ui.sport_combo.setDisabled(True)
        self.leaguesReq(self.selected_sport)
        self.form = Form()
        self.ui.formWidgetLayout.addWidget(self.form)
        self.form.formClosed.connect(self._closeForm)
        self.repaint()

    def _closeForm(self,btn):
        if btn == "save" :
            pass
            # self.ui.sizePolicy.setHorizontalStretch(0)
            # self.restoreState(self.state)
        elif btn == "close" :
            pass

        self.form.close()
        del(self.form)
        self.ui.add_btn.setEnabled(True)
        self.ui.sport_combo.setEnabled(True)
        self.resizeTimer.start(200)
        self.updateGeometry()
        self.repaint()

    def tryResize(self):
        self.resize(400,400)