# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\Jupyter_nb\Work\Amazon_Review\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1089, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_id = QtWidgets.QLabel(self.centralwidget)
        self.label_id.setGeometry(QtCore.QRect(20, 40, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        self.label_id.setFont(font)
        self.label_id.setObjectName("label_id")
        self.lineEdit_id = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_id.setGeometry(QtCore.QRect(60, 40, 211, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.lineEdit_id.setFont(font)
        self.lineEdit_id.setObjectName("lineEdit_id")
        self.textBrowser_log = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_log.setGeometry(QtCore.QRect(410, 40, 651, 401))
        self.textBrowser_log.setObjectName("textBrowser_log")
        self.label_log = QtWidgets.QLabel(self.centralwidget)
        self.label_log.setGeometry(QtCore.QRect(410, 10, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        self.label_log.setFont(font)
        self.label_log.setObjectName("label_log")
        self.pushButton_start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_start.setGeometry(QtCore.QRect(50, 360, 48, 48))
        self.pushButton_start.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons8-start-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_start.setIcon(icon)
        self.pushButton_start.setIconSize(QtCore.QSize(48, 48))
        self.pushButton_start.setAutoDefault(False)
        self.pushButton_start.setObjectName("pushButton_start")
        self.pushButton_stop = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_stop.setGeometry(QtCore.QRect(180, 360, 48, 48))
        self.pushButton_stop.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons8-stop-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_stop.setIcon(icon1)
        self.pushButton_stop.setIconSize(QtCore.QSize(48, 48))
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.pushButton_quit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_quit.setGeometry(QtCore.QRect(310, 360, 48, 48))
        self.pushButton_quit.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons8-export-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_quit.setIcon(icon2)
        self.pushButton_quit.setIconSize(QtCore.QSize(48, 48))
        self.pushButton_quit.setObjectName("pushButton_quit")
        self.label_filter = QtWidgets.QLabel(self.centralwidget)
        self.label_filter.setGeometry(QtCore.QRect(20, 90, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        self.label_filter.setFont(font)
        self.label_filter.setObjectName("label_filter")
        self.checkBox_5star = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_5star.setGeometry(QtCore.QRect(140, 130, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.checkBox_5star.setFont(font)
        self.checkBox_5star.setChecked(True)
        self.checkBox_5star.setObjectName("checkBox_5star")
        self.label_star = QtWidgets.QLabel(self.centralwidget)
        self.label_star.setGeometry(QtCore.QRect(80, 130, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        self.label_star.setFont(font)
        self.label_star.setObjectName("label_star")
        self.checkBox_4star = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4star.setGeometry(QtCore.QRect(140, 170, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.checkBox_4star.setFont(font)
        self.checkBox_4star.setChecked(True)
        self.checkBox_4star.setObjectName("checkBox_4star")
        self.checkBox_3star = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3star.setGeometry(QtCore.QRect(140, 210, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.checkBox_3star.setFont(font)
        self.checkBox_3star.setChecked(True)
        self.checkBox_3star.setObjectName("checkBox_3star")
        self.checkBox_2star = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2star.setGeometry(QtCore.QRect(140, 250, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.checkBox_2star.setFont(font)
        self.checkBox_2star.setChecked(True)
        self.checkBox_2star.setObjectName("checkBox_2star")
        self.checkBox_1star = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_1star.setGeometry(QtCore.QRect(140, 290, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.checkBox_1star.setFont(font)
        self.checkBox_1star.setChecked(True)
        self.checkBox_1star.setObjectName("checkBox_1star")
        self.checkBox_5star_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_5star_2.setGeometry(QtCore.QRect(80, 90, 301, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.checkBox_5star_2.setFont(font)
        self.checkBox_5star_2.setChecked(True)
        self.checkBox_5star_2.setObjectName("checkBox_5star_2")
        self.label_intro = QtWidgets.QLabel(self.centralwidget)
        self.label_intro.setGeometry(QtCore.QRect(10, 450, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        self.label_intro.setFont(font)
        self.label_intro.setObjectName("label_intro")
        self.label_url = QtWidgets.QLabel(self.centralwidget)
        self.label_url.setGeometry(QtCore.QRect(130, 450, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        self.label_url.setFont(font)
        self.label_url.setOpenExternalLinks(True)
        self.label_url.setObjectName("label_url")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Amazon Review Scrapy"))
        self.label_id.setText(_translate("MainWindow", "ID:"))
        self.label_log.setText(_translate("MainWindow", "Log Window:"))
        self.label_filter.setText(_translate("MainWindow", "Filter:"))
        self.checkBox_5star.setText(_translate("MainWindow", "5 star"))
        self.label_star.setText(_translate("MainWindow", "Star:"))
        self.checkBox_4star.setText(_translate("MainWindow", "4 star"))
        self.checkBox_3star.setText(_translate("MainWindow", "3 star"))
        self.checkBox_2star.setText(_translate("MainWindow", "2 star"))
        self.checkBox_1star.setText(_translate("MainWindow", "1 star"))
        self.checkBox_5star_2.setText(_translate("MainWindow", "Only show Verify Purchased Reivew"))
        self.label_intro.setText(_translate("MainWindow", "Powered By   "))
        self.label_url.setText(_translate("MainWindow", "<html><head/><body><p><a href=\"https://github.com/G0Lotus/Amazon-Review\"><span style=\" text-decoration: underline; color:#0000ff;\">G0Lotus</span></a></p></body></html>"))