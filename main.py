# -*- coding: utf-8 -*-
import os
import random
from PyQt4 import QtGui
import sys

import time

import design

class ExampleApp(QtGui.QMainWindow, design.Ui_MainWindow):

    sourceFilename = u'/home/inilotic/python/qt1/files/ЗП/40EK1906.ENC'
    rulesFilename = u'/home/inilotic/python/qt1/files/ЗП/Список УС на 11.02.2016.csv'
    outFolder = u'/home/inilotic/python/qt1/out'

    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)
        self.sourceFileSelectBtn.clicked.connect(self.browse_source_file)
        self.outSelectBtn.clicked.connect(self.pick_output_folder)
        self.rulesFileSelectBtn.clicked.connect(self.browse_rules_file)
        self.explodeStart.clicked.connect(self.fileParse)

    def browse_source_file(self):
        self.sourceFilename = QtGui.QFileDialog.getOpenFileName(self, "Pick a file")
        self.sourceFileNameLbl.setText(self.sourceFilename)

    def pick_output_folder(self):
        self.outFolder = QtGui.QFileDialog.getExistingDirectory(self, "Pick a folder")
        self.outDirLbl.setText(self.outFolder)

    def browse_rules_file(self):
        self.rulesFilename = QtGui.QFileDialog.getOpenFileName(self, "Pick a file")
        self.rulesFileLbl.setText(self.rulesFilename)

    def fileParse(self):
        if not self.outFolder:
            QtGui.QMessageBox.critical(self, u'Ошибка', u'Не указан путь выгрузки', QtGui.QMessageBox.Ok)
            return
        if not self.sourceFilename:
            QtGui.QMessageBox.critical(self, u'Ошибка', u'Не указан файл для разбора', QtGui.QMessageBox.Ok)
            return
        if not self.rulesFilename:
            QtGui.QMessageBox.critical(self, u'Ошибка', u'Не указан файл c правилами разбора', QtGui.QMessageBox.Ok)
            return

        if self.sourceFilename:

            with open(unicode(self.sourceFilename)) as sourceLines, open(unicode(self.rulesFilename)) as rulesLines:

                content = sourceLines.readlines()
                #popup last broken string
                content.pop()
                rules = rulesLines.readlines()
                #trim header
                rules = rules[1::]



                if not bool(len(content)) or not bool(len(rules)):
                    QtGui.QMessageBox.critical(self, u'Ошибка', u'Передан пустой файл для разбора или файл с правилами', QtGui.QMessageBox.Ok)
                    return

                #get rules
                us_list = {}
                for line in rules:
                    lineSet = line.split(",")
                    if not us_list.has_key(lineSet[2]):
                        us_list[lineSet[2]] = []
                    us_list[lineSet[2]].append(lineSet[0])

                #get source
                analized_list = []
                for line in content:
                    analized_list.append(line.split(";"))

                result = {
                    'others': []
                }

                self.explodeProgressBar.setMaximum(len(analized_list))
                self.explodeProgressBar.setValue(0)

                for klc in analized_list:
                    for k, v in us_list.iteritems():
                        if klc[0] not in ['P', 'M']:
                            result['others'].append(';'.join(klc))
                            continue

                        if klc[1] in v:
                            if not result.has_key(k):
                                result[k] = []
                            result[k].append(';'.join(klc))
                    self.explodeProgressBar.setValue(self.explodeProgressBar.value()+1)

                for k, v in result.iteritems():
                    fo = open(unicode(self.outFolder) + "/" + k.decode('utf-8') + ".txt", "wb")
                    for line in v:
                        fo.write(line)
                    fo.close()


                self.explodeProgressBar.setValue(0)
                QtGui.QMessageBox.information(self, u'Успешно', u'Разбор закончен', QtGui.QMessageBox.Ok)

                return
        else:
            QtGui.QMessageBox.critical(self, u'Ошибка', u'Файл не передан', QtGui.QMessageBox.Ok)
            return

def main():
    app = QtGui.QApplication(sys.argv)
    form = ExampleApp()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()