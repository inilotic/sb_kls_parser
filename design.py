# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(603, 394)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 601, 401))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_1 = QtGui.QWidget()
        self.tab_1.setObjectName(_fromUtf8("tab_1"))
        self.sourceFileSelectBtn = QtGui.QToolButton(self.tab_1)
        self.sourceFileSelectBtn.setGeometry(QtCore.QRect(550, 20, 31, 31))
        self.sourceFileSelectBtn.setObjectName(_fromUtf8("sourceFileSelectBtn"))
        self.sourceFileNameLbl = QtGui.QLabel(self.tab_1)
        self.sourceFileNameLbl.setGeometry(QtCore.QRect(10, 26, 541, 21))
        self.sourceFileNameLbl.setObjectName(_fromUtf8("sourceFileNameLbl"))
        self.outDirLbl = QtGui.QLabel(self.tab_1)
        self.outDirLbl.setGeometry(QtCore.QRect(10, 70, 541, 17))
        self.outDirLbl.setObjectName(_fromUtf8("outDirLbl"))
        self.outSelectBtn = QtGui.QToolButton(self.tab_1)
        self.outSelectBtn.setGeometry(QtCore.QRect(550, 60, 31, 31))
        self.outSelectBtn.setObjectName(_fromUtf8("outSelectBtn"))
        self.rulesFileLbl = QtGui.QLabel(self.tab_1)
        self.rulesFileLbl.setGeometry(QtCore.QRect(10, 110, 541, 17))
        self.rulesFileLbl.setObjectName(_fromUtf8("rulesFileLbl"))
        self.rulesFileSelectBtn = QtGui.QToolButton(self.tab_1)
        self.rulesFileSelectBtn.setGeometry(QtCore.QRect(550, 100, 31, 31))
        self.rulesFileSelectBtn.setObjectName(_fromUtf8("rulesFileSelectBtn"))
        self.explodeProgressBar = QtGui.QProgressBar(self.tab_1)
        self.explodeProgressBar.setGeometry(QtCore.QRect(10, 170, 571, 23))
        self.explodeProgressBar.setProperty("value", 0)
        self.explodeProgressBar.setObjectName(_fromUtf8("explodeProgressBar"))
        self.explodeStart = QtGui.QPushButton(self.tab_1)
        self.explodeStart.setGeometry(QtCore.QRect(180, 210, 99, 27))
        self.explodeStart.setObjectName(_fromUtf8("explodeStart"))
        self.explodeCancel = QtGui.QPushButton(self.tab_1)
        self.explodeCancel.setEnabled(False)
        self.explodeCancel.setGeometry(QtCore.QRect(290, 210, 99, 27))
        self.explodeCancel.setObjectName(_fromUtf8("explodeCancel"))
        self.tabWidget.addTab(self.tab_1, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Разборщик ключевых файлов", None))
        self.sourceFileSelectBtn.setText(_translate("MainWindow", "...", None))
        self.sourceFileNameLbl.setText(_translate("MainWindow", "Укажите файл для разбора...", None))
        self.outDirLbl.setText(_translate("MainWindow", "Укажите путь выгрузки...", None))
        self.outSelectBtn.setText(_translate("MainWindow", "...", None))
        self.rulesFileLbl.setText(_translate("MainWindow", "Укажите файл с правилами разбивки файлов...", None))
        self.rulesFileSelectBtn.setText(_translate("MainWindow", "...", None))
        self.explodeStart.setText(_translate("MainWindow", "Начать", None))
        self.explodeCancel.setText(_translate("MainWindow", "Отмена", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "Разбор файла", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Отчеты", None))

