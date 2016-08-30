# -*- coding: utf-8 -*-
import random
from PyQt4 import QtGui

import time
from PyQt4.QtCore import QThread


class ParseThread(QThread):
    def __init__(self, filePath, outPath):
        QThread.__init__(self)
        self.filePath = filePath
        self.outPath = outPath

    def __del__(self):
        self.wait()

    def file_parse(self, filePAth):
        if not self.outPath:
            QtGui.QMessageBox.critical(self.outPath, u'Ошибка', u'Передан пустой путь для выгрузки', QtGui.QMessageBox.Ok)
            return

        if filePAth:
            with open(filePAth) as f:

                content = f.readlines()

                if len(content) == 0:
                    QtGui.QMessageBox.critical(self.filePath, u'Ошибка', u'Передан пустой файл', QtGui.QMessageBox.Ok)
                    return

                self.progressBar.setMaximum(len(content))
                self.progressBar.setValue(0)
                for line in content:
                    fo = open(str(self.outFolder) + "/" + str(random.randrange(0, 50000)) + ".txt", "wb")
                    fo.write(line)
                    fo.close()
                    self.progressBar.setValue(self.progressBar.value() + 1)
                    time.sleep(1)

                self.progressBar.setValue(0)
                QtGui.QMessageBox.information(self, u'Успешно', u'Анализ закончен', QtGui.QMessageBox.Ok)

                return
        else:
            QtGui.QMessageBox.critical(self, u'Ошибка', u'Файл не передан', QtGui.QMessageBox.Ok)
            return

    def run(self):
        self.file_parse(self.filePath)
        self.sleep(2)
