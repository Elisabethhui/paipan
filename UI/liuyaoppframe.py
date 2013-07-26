# -*- coding: utf-8 -*-
import datetime
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import liuyaoppframe_ui

class LiuyaoPPFrame(QFrame):
    def setupUi(self):
        self.ui=liuyaoppframe_ui.Ui_LiuyaoPPFrame()
        self.ui.setupUi(self)
        self._funcpp=None
    def setCbPaipan(self,func):
        self._funcpp=func
    def data(self):
        info={}
        info['name']=self.ui.edit_name.text().toUtf8().data()
        info['question']=self.ui.edit_question.text().toUtf8().data()
        if self.ui.radio_number.isChecked():
            info['method1']="%d,%d,%d"%(self.ui.edit_mtd11.text().toInt()[0], self.ui.edit_mtd12.text().toInt()[0], self.ui.edit_mtd13.text().toInt()[0])
        elif self.ui.radio_gua.isChecked():
            guacode=[]
            guacode.append(self.ui.combo_mtd21.currentIndex()+1)
            guacode.append(self.ui.combo_mtd22.currentIndex()+1)
            if self.ui.check_mtd21.isChecked():
                guacode.append(1)
            if self.ui.check_mtd22.isChecked():
                guacode.append(2)
            if self.ui.check_mtd23.isChecked():
                guacode.append(3)
            if self.ui.check_mtd24.isChecked():
                guacode.append(4)
            if self.ui.check_mtd25.isChecked():
                guacode.append(5)
            if self.ui.check_mtd26.isChecked():
                guacode.append(6)
            info['method2']=",".join([str(x) for x in guacode])
        else:
            info['method3']="%d,%d,%d,%d,%d,%d"%(self.ui.combo_mtd31.currentText().toInt()[0], self.ui.combo_mtd32.currentText().toInt()[0], self.ui.combo_mtd33.currentText().toInt()[0], self.ui.combo_mtd34.currentText().toInt()[0], self.ui.combo_mtd35.currentText().toInt()[0], self.ui.combo_mtd36.currentText().toInt()[0])
        d=self.ui.calendar.selectedDate()
        t=self.ui.time.time()
        info['datetime']=(d.year(),d.month(),d.day(),t.hour(),t.minute(),t.second())
        return info
    def onMethodToggled(self,flag):
        if self.ui.radio_number.isChecked():
            self.ui.edit_mtd11.setEnabled(True)
            self.ui.edit_mtd12.setEnabled(True)
            self.ui.edit_mtd13.setEnabled(True)
        else:
            self.ui.edit_mtd11.setEnabled(False)
            self.ui.edit_mtd12.setEnabled(False)
            self.ui.edit_mtd13.setEnabled(False)
        if self.ui.radio_gua.isChecked():
            self.ui.combo_mtd21.setEnabled(True)
            self.ui.combo_mtd22.setEnabled(True)
            self.ui.check_mtd21.setEnabled(True)
            self.ui.check_mtd22.setEnabled(True)
            self.ui.check_mtd23.setEnabled(True)
            self.ui.check_mtd24.setEnabled(True)
            self.ui.check_mtd25.setEnabled(True)
            self.ui.check_mtd26.setEnabled(True)
        else:
            self.ui.combo_mtd21.setEnabled(False)
            self.ui.combo_mtd22.setEnabled(False)
            self.ui.check_mtd21.setEnabled(False)
            self.ui.check_mtd22.setEnabled(False)
            self.ui.check_mtd23.setEnabled(False)
            self.ui.check_mtd24.setEnabled(False)
            self.ui.check_mtd25.setEnabled(False)
            self.ui.check_mtd26.setEnabled(False)
        if self.ui.radio_coin.isChecked():
            self.ui.combo_mtd31.setEnabled(True)
            self.ui.combo_mtd32.setEnabled(True)
            self.ui.combo_mtd33.setEnabled(True)
            self.ui.combo_mtd34.setEnabled(True)
            self.ui.combo_mtd35.setEnabled(True)
            self.ui.combo_mtd36.setEnabled(True)
        else:
            self.ui.combo_mtd31.setEnabled(False)
            self.ui.combo_mtd32.setEnabled(False)
            self.ui.combo_mtd33.setEnabled(False)
            self.ui.combo_mtd34.setEnabled(False)
            self.ui.combo_mtd35.setEnabled(False)
            self.ui.combo_mtd36.setEnabled(False)
    def onBtnPaipan(self):
        if self._funcpp:
            self._funcpp(self)
    def onBtnNow(self):
        n=datetime.datetime.now()
        self.ui.calendar.setSelectedDate(QDate(n.year,n.month,n.day))
        self.ui.time.setTime(QTime(n.hour,n.minute,n.second))
