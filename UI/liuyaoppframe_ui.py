# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'liuyaoppframe.ui'
#
# Created: Sat Jul 27 08:39:08 2013
#      by: PyQt4 UI code generator 4.10.2
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

class Ui_LiuyaoPPFrame(object):
    def setupUi(self, LiuyaoPPFrame):
        LiuyaoPPFrame.setObjectName(_fromUtf8("LiuyaoPPFrame"))
        LiuyaoPPFrame.resize(475, 428)
        LiuyaoPPFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        LiuyaoPPFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.formLayout = QtGui.QFormLayout(LiuyaoPPFrame)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(LiuyaoPPFrame)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.edit_name = QtGui.QLineEdit(LiuyaoPPFrame)
        self.edit_name.setObjectName(_fromUtf8("edit_name"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.edit_name)
        self.groupBox_3 = QtGui.QGroupBox(LiuyaoPPFrame)
        self.groupBox_3.setTitle(_fromUtf8(""))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.btnNow = QtGui.QPushButton(self.groupBox_3)
        self.btnNow.setObjectName(_fromUtf8("btnNow"))
        self.horizontalLayout_2.addWidget(self.btnNow)
        self.btnPaipan = QtGui.QPushButton(self.groupBox_3)
        self.btnPaipan.setEnabled(False)
        self.btnPaipan.setObjectName(_fromUtf8("btnPaipan"))
        self.horizontalLayout_2.addWidget(self.btnPaipan)
        self.formLayout.setWidget(4, QtGui.QFormLayout.SpanningRole, self.groupBox_3)
        self.label_2 = QtGui.QLabel(LiuyaoPPFrame)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.edit_question = QtGui.QLineEdit(LiuyaoPPFrame)
        self.edit_question.setObjectName(_fromUtf8("edit_question"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.edit_question)
        self.groupBox = QtGui.QGroupBox(LiuyaoPPFrame)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.radio_gua = QtGui.QRadioButton(self.groupBox)
        self.radio_gua.setObjectName(_fromUtf8("radio_gua"))
        self.gridLayout.addWidget(self.radio_gua, 1, 0, 1, 1)
        self.radio_coin = QtGui.QRadioButton(self.groupBox)
        self.radio_coin.setObjectName(_fromUtf8("radio_coin"))
        self.gridLayout.addWidget(self.radio_coin, 5, 0, 1, 1)
        self.radio_number = QtGui.QRadioButton(self.groupBox)
        self.radio_number.setChecked(True)
        self.radio_number.setObjectName(_fromUtf8("radio_number"))
        self.gridLayout.addWidget(self.radio_number, 0, 0, 1, 1)
        self.groupBox_6 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_6.setTitle(_fromUtf8(""))
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.edit_mtd11 = QtGui.QLineEdit(self.groupBox_6)
        self.edit_mtd11.setMinimumSize(QtCore.QSize(60, 20))
        self.edit_mtd11.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.edit_mtd11.setInputMethodHints(QtCore.Qt.ImhNone)
        self.edit_mtd11.setMaxLength(5)
        self.edit_mtd11.setCursorPosition(0)
        self.edit_mtd11.setObjectName(_fromUtf8("edit_mtd11"))
        self.horizontalLayout_3.addWidget(self.edit_mtd11)
        self.edit_mtd12 = QtGui.QLineEdit(self.groupBox_6)
        self.edit_mtd12.setMinimumSize(QtCore.QSize(60, 20))
        self.edit_mtd12.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.edit_mtd12.setInputMethodHints(QtCore.Qt.ImhNone)
        self.edit_mtd12.setMaxLength(5)
        self.edit_mtd12.setCursorPosition(0)
        self.edit_mtd12.setObjectName(_fromUtf8("edit_mtd12"))
        self.horizontalLayout_3.addWidget(self.edit_mtd12)
        self.edit_mtd13 = QtGui.QLineEdit(self.groupBox_6)
        self.edit_mtd13.setMinimumSize(QtCore.QSize(60, 20))
        self.edit_mtd13.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.edit_mtd13.setInputMethodHints(QtCore.Qt.ImhNone)
        self.edit_mtd13.setMaxLength(5)
        self.edit_mtd13.setCursorPosition(0)
        self.edit_mtd13.setObjectName(_fromUtf8("edit_mtd13"))
        self.horizontalLayout_3.addWidget(self.edit_mtd13)
        self.gridLayout.addWidget(self.groupBox_6, 0, 1, 1, 1)
        self.groupBox_5 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_5.setTitle(_fromUtf8(""))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.combo_mtd21 = QtGui.QComboBox(self.groupBox_5)
        self.combo_mtd21.setEnabled(False)
        self.combo_mtd21.setObjectName(_fromUtf8("combo_mtd21"))
        self.combo_mtd21.addItem(_fromUtf8(""))
        self.combo_mtd21.addItem(_fromUtf8(""))
        self.combo_mtd21.addItem(_fromUtf8(""))
        self.combo_mtd21.addItem(_fromUtf8(""))
        self.combo_mtd21.addItem(_fromUtf8(""))
        self.combo_mtd21.addItem(_fromUtf8(""))
        self.combo_mtd21.addItem(_fromUtf8(""))
        self.combo_mtd21.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.combo_mtd21)
        self.combo_mtd22 = QtGui.QComboBox(self.groupBox_5)
        self.combo_mtd22.setEnabled(False)
        self.combo_mtd22.setObjectName(_fromUtf8("combo_mtd22"))
        self.combo_mtd22.addItem(_fromUtf8(""))
        self.combo_mtd22.addItem(_fromUtf8(""))
        self.combo_mtd22.addItem(_fromUtf8(""))
        self.combo_mtd22.addItem(_fromUtf8(""))
        self.combo_mtd22.addItem(_fromUtf8(""))
        self.combo_mtd22.addItem(_fromUtf8(""))
        self.combo_mtd22.addItem(_fromUtf8(""))
        self.combo_mtd22.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.combo_mtd22)
        self.check_mtd21 = QtGui.QCheckBox(self.groupBox_5)
        self.check_mtd21.setEnabled(False)
        self.check_mtd21.setObjectName(_fromUtf8("check_mtd21"))
        self.horizontalLayout.addWidget(self.check_mtd21)
        self.check_mtd22 = QtGui.QCheckBox(self.groupBox_5)
        self.check_mtd22.setEnabled(False)
        self.check_mtd22.setObjectName(_fromUtf8("check_mtd22"))
        self.horizontalLayout.addWidget(self.check_mtd22)
        self.check_mtd23 = QtGui.QCheckBox(self.groupBox_5)
        self.check_mtd23.setEnabled(False)
        self.check_mtd23.setObjectName(_fromUtf8("check_mtd23"))
        self.horizontalLayout.addWidget(self.check_mtd23)
        self.check_mtd24 = QtGui.QCheckBox(self.groupBox_5)
        self.check_mtd24.setEnabled(False)
        self.check_mtd24.setObjectName(_fromUtf8("check_mtd24"))
        self.horizontalLayout.addWidget(self.check_mtd24)
        self.check_mtd25 = QtGui.QCheckBox(self.groupBox_5)
        self.check_mtd25.setEnabled(False)
        self.check_mtd25.setObjectName(_fromUtf8("check_mtd25"))
        self.horizontalLayout.addWidget(self.check_mtd25)
        self.check_mtd26 = QtGui.QCheckBox(self.groupBox_5)
        self.check_mtd26.setEnabled(False)
        self.check_mtd26.setObjectName(_fromUtf8("check_mtd26"))
        self.horizontalLayout.addWidget(self.check_mtd26)
        self.gridLayout.addWidget(self.groupBox_5, 1, 1, 1, 1)
        self.groupBox_4 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_4)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_3 = QtGui.QLabel(self.groupBox_4)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.combo_mtd31 = QtGui.QComboBox(self.groupBox_4)
        self.combo_mtd31.setEnabled(False)
        self.combo_mtd31.setObjectName(_fromUtf8("combo_mtd31"))
        self.combo_mtd31.addItem(_fromUtf8(""))
        self.combo_mtd31.addItem(_fromUtf8(""))
        self.combo_mtd31.addItem(_fromUtf8(""))
        self.combo_mtd31.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.combo_mtd31, 0, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox_4)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 0, 2, 1, 1)
        self.label_5 = QtGui.QLabel(self.groupBox_4)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 0, 4, 1, 1)
        self.combo_mtd32 = QtGui.QComboBox(self.groupBox_4)
        self.combo_mtd32.setEnabled(False)
        self.combo_mtd32.setObjectName(_fromUtf8("combo_mtd32"))
        self.combo_mtd32.addItem(_fromUtf8(""))
        self.combo_mtd32.addItem(_fromUtf8(""))
        self.combo_mtd32.addItem(_fromUtf8(""))
        self.combo_mtd32.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.combo_mtd32, 0, 3, 1, 1)
        self.combo_mtd33 = QtGui.QComboBox(self.groupBox_4)
        self.combo_mtd33.setEnabled(False)
        self.combo_mtd33.setObjectName(_fromUtf8("combo_mtd33"))
        self.combo_mtd33.addItem(_fromUtf8(""))
        self.combo_mtd33.addItem(_fromUtf8(""))
        self.combo_mtd33.addItem(_fromUtf8(""))
        self.combo_mtd33.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.combo_mtd33, 0, 5, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupBox_4)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_2.addWidget(self.label_6, 1, 0, 1, 1)
        self.combo_mtd34 = QtGui.QComboBox(self.groupBox_4)
        self.combo_mtd34.setEnabled(False)
        self.combo_mtd34.setObjectName(_fromUtf8("combo_mtd34"))
        self.combo_mtd34.addItem(_fromUtf8(""))
        self.combo_mtd34.addItem(_fromUtf8(""))
        self.combo_mtd34.addItem(_fromUtf8(""))
        self.combo_mtd34.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.combo_mtd34, 1, 1, 1, 1)
        self.label_8 = QtGui.QLabel(self.groupBox_4)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_2.addWidget(self.label_8, 1, 2, 1, 1)
        self.combo_mtd35 = QtGui.QComboBox(self.groupBox_4)
        self.combo_mtd35.setEnabled(False)
        self.combo_mtd35.setObjectName(_fromUtf8("combo_mtd35"))
        self.combo_mtd35.addItem(_fromUtf8(""))
        self.combo_mtd35.addItem(_fromUtf8(""))
        self.combo_mtd35.addItem(_fromUtf8(""))
        self.combo_mtd35.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.combo_mtd35, 1, 3, 1, 1)
        self.label_7 = QtGui.QLabel(self.groupBox_4)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_2.addWidget(self.label_7, 1, 4, 1, 1)
        self.combo_mtd36 = QtGui.QComboBox(self.groupBox_4)
        self.combo_mtd36.setEnabled(False)
        self.combo_mtd36.setObjectName(_fromUtf8("combo_mtd36"))
        self.combo_mtd36.addItem(_fromUtf8(""))
        self.combo_mtd36.addItem(_fromUtf8(""))
        self.combo_mtd36.addItem(_fromUtf8(""))
        self.combo_mtd36.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.combo_mtd36, 1, 5, 1, 1)
        self.gridLayout.addWidget(self.groupBox_4, 5, 1, 1, 1)
        self.formLayout.setWidget(2, QtGui.QFormLayout.SpanningRole, self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(LiuyaoPPFrame)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.radio_time1 = QtGui.QRadioButton(self.groupBox_2)
        self.radio_time1.setChecked(True)
        self.radio_time1.setObjectName(_fromUtf8("radio_time1"))
        self.gridLayout_3.addWidget(self.radio_time1, 0, 0, 1, 1)
        self.radio_time2 = QtGui.QRadioButton(self.groupBox_2)
        self.radio_time2.setObjectName(_fromUtf8("radio_time2"))
        self.gridLayout_3.addWidget(self.radio_time2, 1, 0, 1, 1)
        self.label_9 = QtGui.QLabel(self.groupBox_2)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_3.addWidget(self.label_9, 1, 2, 1, 1)
        self.label_10 = QtGui.QLabel(self.groupBox_2)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_3.addWidget(self.label_10, 1, 4, 1, 1)
        self.combo_month = QtGui.QComboBox(self.groupBox_2)
        self.combo_month.setEnabled(False)
        self.combo_month.setObjectName(_fromUtf8("combo_month"))
        self.combo_month.addItem(_fromUtf8(""))
        self.combo_month.addItem(_fromUtf8(""))
        self.combo_month.addItem(_fromUtf8(""))
        self.combo_month.addItem(_fromUtf8(""))
        self.combo_month.addItem(_fromUtf8(""))
        self.combo_month.addItem(_fromUtf8(""))
        self.combo_month.addItem(_fromUtf8(""))
        self.combo_month.addItem(_fromUtf8(""))
        self.combo_month.addItem(_fromUtf8(""))
        self.combo_month.addItem(_fromUtf8(""))
        self.combo_month.addItem(_fromUtf8(""))
        self.combo_month.addItem(_fromUtf8(""))
        self.gridLayout_3.addWidget(self.combo_month, 1, 1, 1, 1)
        self.combo_day = QtGui.QComboBox(self.groupBox_2)
        self.combo_day.setEnabled(False)
        self.combo_day.setObjectName(_fromUtf8("combo_day"))
        self.combo_day.addItem(_fromUtf8(""))
        self.combo_day.addItem(_fromUtf8(""))
        self.combo_day.addItem(_fromUtf8(""))
        self.combo_day.addItem(_fromUtf8(""))
        self.combo_day.addItem(_fromUtf8(""))
        self.combo_day.addItem(_fromUtf8(""))
        self.combo_day.addItem(_fromUtf8(""))
        self.combo_day.addItem(_fromUtf8(""))
        self.combo_day.addItem(_fromUtf8(""))
        self.combo_day.addItem(_fromUtf8(""))
        self.combo_day.addItem(_fromUtf8(""))
        self.combo_day.addItem(_fromUtf8(""))
        self.combo_day.addItem(_fromUtf8(""))
        self.combo_day.addItem(_fromUtf8(""))
        self.combo_day.addItem(_fromUtf8(""))
        self.combo_day.addItem(_fromUtf8(""))
        self.combo_day.addItem(_fromUtf8(""))
        self.combo_day.addItem(_fromUtf8(""))
        self.combo_day.addItem(_fromUtf8(""))
        self.combo_day.addItem(_fromUtf8(""))
        self.combo_day.addItem(_fromUtf8(""))
        self.combo_day.addItem(_fromUtf8(""))
        self.combo_day.addItem(_fromUtf8(""))
        self.combo_day.addItem(_fromUtf8(""))
        self.combo_day.addItem(_fromUtf8(""))
        self.combo_day.addItem(_fromUtf8(""))
        self.combo_day.addItem(_fromUtf8(""))
        self.combo_day.addItem(_fromUtf8(""))
        self.combo_day.addItem(_fromUtf8(""))
        self.combo_day.addItem(_fromUtf8(""))
        self.combo_day.addItem(_fromUtf8(""))
        self.combo_day.addItem(_fromUtf8(""))
        self.combo_day.addItem(_fromUtf8(""))
        self.combo_day.addItem(_fromUtf8(""))
        self.combo_day.addItem(_fromUtf8(""))
        self.combo_day.addItem(_fromUtf8(""))
        self.combo_day.addItem(_fromUtf8(""))
        self.combo_day.addItem(_fromUtf8(""))
        self.combo_day.addItem(_fromUtf8(""))
        self.combo_day.addItem(_fromUtf8(""))
        self.combo_day.addItem(_fromUtf8(""))
        self.combo_day.addItem(_fromUtf8(""))
        self.combo_day.addItem(_fromUtf8(""))
        self.combo_day.addItem(_fromUtf8(""))
        self.combo_day.addItem(_fromUtf8(""))
        self.combo_day.addItem(_fromUtf8(""))
        self.combo_day.addItem(_fromUtf8(""))
        self.combo_day.addItem(_fromUtf8(""))
        self.combo_day.addItem(_fromUtf8(""))
        self.combo_day.addItem(_fromUtf8(""))
        self.combo_day.addItem(_fromUtf8(""))
        self.combo_day.addItem(_fromUtf8(""))
        self.combo_day.addItem(_fromUtf8(""))
        self.combo_day.addItem(_fromUtf8(""))
        self.combo_day.addItem(_fromUtf8(""))
        self.combo_day.addItem(_fromUtf8(""))
        self.combo_day.addItem(_fromUtf8(""))
        self.combo_day.addItem(_fromUtf8(""))
        self.combo_day.addItem(_fromUtf8(""))
        self.combo_day.addItem(_fromUtf8(""))
        self.gridLayout_3.addWidget(self.combo_day, 1, 3, 1, 1)
        self.dateTimeEdit = QtGui.QDateTimeEdit(self.groupBox_2)
        self.dateTimeEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.dateTimeEdit.setObjectName(_fromUtf8("dateTimeEdit"))
        self.gridLayout_3.addWidget(self.dateTimeEdit, 0, 1, 1, 4)
        self.formLayout.setWidget(3, QtGui.QFormLayout.SpanningRole, self.groupBox_2)
        self.label.setBuddy(self.edit_name)
        self.label_2.setBuddy(self.edit_question)
        self.label_9.setBuddy(self.combo_month)
        self.label_10.setBuddy(self.combo_day)

        self.retranslateUi(LiuyaoPPFrame)
        QtCore.QObject.connect(self.btnNow, QtCore.SIGNAL(_fromUtf8("clicked()")), LiuyaoPPFrame.onBtnNow)
        QtCore.QObject.connect(self.radio_number, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), LiuyaoPPFrame.onMethodToggled)
        QtCore.QObject.connect(self.radio_gua, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), LiuyaoPPFrame.onMethodToggled)
        QtCore.QObject.connect(self.radio_coin, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), LiuyaoPPFrame.onMethodToggled)
        QtCore.QObject.connect(self.btnPaipan, QtCore.SIGNAL(_fromUtf8("clicked()")), LiuyaoPPFrame.onBtnPaipan)
        QtCore.QObject.connect(self.radio_time1, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), LiuyaoPPFrame.onTimeToggled)
        QtCore.QObject.connect(self.radio_time2, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), LiuyaoPPFrame.onTimeToggled)
        QtCore.QMetaObject.connectSlotsByName(LiuyaoPPFrame)
        LiuyaoPPFrame.setTabOrder(self.edit_name, self.edit_question)
        LiuyaoPPFrame.setTabOrder(self.edit_question, self.radio_number)
        LiuyaoPPFrame.setTabOrder(self.radio_number, self.radio_gua)
        LiuyaoPPFrame.setTabOrder(self.radio_gua, self.radio_coin)
        LiuyaoPPFrame.setTabOrder(self.radio_coin, self.btnNow)
        LiuyaoPPFrame.setTabOrder(self.btnNow, self.btnPaipan)

    def retranslateUi(self, LiuyaoPPFrame):
        LiuyaoPPFrame.setWindowTitle(_translate("LiuyaoPPFrame", "Frame", None))
        self.label.setText(_translate("LiuyaoPPFrame", "求测人", None))
        self.btnNow.setText(_translate("LiuyaoPPFrame", "当前时间", None))
        self.btnPaipan.setText(_translate("LiuyaoPPFrame", "起卦", None))
        self.label_2.setText(_translate("LiuyaoPPFrame", "占事", None))
        self.groupBox.setTitle(_translate("LiuyaoPPFrame", "起卦方法", None))
        self.radio_gua.setText(_translate("LiuyaoPPFrame", "卦码", None))
        self.radio_coin.setText(_translate("LiuyaoPPFrame", "铜钱", None))
        self.radio_number.setText(_translate("LiuyaoPPFrame", "数字", None))
        self.edit_mtd11.setInputMask(_translate("LiuyaoPPFrame", "99999; ", None))
        self.edit_mtd11.setText(_translate("LiuyaoPPFrame", "0", None))
        self.edit_mtd12.setInputMask(_translate("LiuyaoPPFrame", "99999; ", None))
        self.edit_mtd12.setText(_translate("LiuyaoPPFrame", "0", None))
        self.edit_mtd13.setInputMask(_translate("LiuyaoPPFrame", "99999; ", None))
        self.edit_mtd13.setText(_translate("LiuyaoPPFrame", "0", None))
        self.combo_mtd21.setItemText(0, _translate("LiuyaoPPFrame", "1(乾)", None))
        self.combo_mtd21.setItemText(1, _translate("LiuyaoPPFrame", "2(兑)", None))
        self.combo_mtd21.setItemText(2, _translate("LiuyaoPPFrame", "3(离)", None))
        self.combo_mtd21.setItemText(3, _translate("LiuyaoPPFrame", "4(震)", None))
        self.combo_mtd21.setItemText(4, _translate("LiuyaoPPFrame", "5(巽)", None))
        self.combo_mtd21.setItemText(5, _translate("LiuyaoPPFrame", "6(坎)", None))
        self.combo_mtd21.setItemText(6, _translate("LiuyaoPPFrame", "7(艮)", None))
        self.combo_mtd21.setItemText(7, _translate("LiuyaoPPFrame", "8(坤)", None))
        self.combo_mtd22.setItemText(0, _translate("LiuyaoPPFrame", "1(乾)", None))
        self.combo_mtd22.setItemText(1, _translate("LiuyaoPPFrame", "2(兑)", None))
        self.combo_mtd22.setItemText(2, _translate("LiuyaoPPFrame", "3(离)", None))
        self.combo_mtd22.setItemText(3, _translate("LiuyaoPPFrame", "4(震)", None))
        self.combo_mtd22.setItemText(4, _translate("LiuyaoPPFrame", "5(巽)", None))
        self.combo_mtd22.setItemText(5, _translate("LiuyaoPPFrame", "6(坎)", None))
        self.combo_mtd22.setItemText(6, _translate("LiuyaoPPFrame", "7(艮)", None))
        self.combo_mtd22.setItemText(7, _translate("LiuyaoPPFrame", "8(坤)", None))
        self.check_mtd21.setText(_translate("LiuyaoPPFrame", "1", None))
        self.check_mtd22.setText(_translate("LiuyaoPPFrame", "2", None))
        self.check_mtd23.setText(_translate("LiuyaoPPFrame", "3", None))
        self.check_mtd24.setText(_translate("LiuyaoPPFrame", "4", None))
        self.check_mtd25.setText(_translate("LiuyaoPPFrame", "5", None))
        self.check_mtd26.setText(_translate("LiuyaoPPFrame", "6", None))
        self.groupBox_4.setTitle(_translate("LiuyaoPPFrame", "背面个数", None))
        self.label_3.setText(_translate("LiuyaoPPFrame", "第一次", None))
        self.combo_mtd31.setItemText(0, _translate("LiuyaoPPFrame", "0", None))
        self.combo_mtd31.setItemText(1, _translate("LiuyaoPPFrame", "1", None))
        self.combo_mtd31.setItemText(2, _translate("LiuyaoPPFrame", "2", None))
        self.combo_mtd31.setItemText(3, _translate("LiuyaoPPFrame", "3", None))
        self.label_4.setText(_translate("LiuyaoPPFrame", "第二次", None))
        self.label_5.setText(_translate("LiuyaoPPFrame", "第三次", None))
        self.combo_mtd32.setItemText(0, _translate("LiuyaoPPFrame", "0", None))
        self.combo_mtd32.setItemText(1, _translate("LiuyaoPPFrame", "1", None))
        self.combo_mtd32.setItemText(2, _translate("LiuyaoPPFrame", "2", None))
        self.combo_mtd32.setItemText(3, _translate("LiuyaoPPFrame", "3", None))
        self.combo_mtd33.setItemText(0, _translate("LiuyaoPPFrame", "0", None))
        self.combo_mtd33.setItemText(1, _translate("LiuyaoPPFrame", "1", None))
        self.combo_mtd33.setItemText(2, _translate("LiuyaoPPFrame", "2", None))
        self.combo_mtd33.setItemText(3, _translate("LiuyaoPPFrame", "3", None))
        self.label_6.setText(_translate("LiuyaoPPFrame", "第四次", None))
        self.combo_mtd34.setItemText(0, _translate("LiuyaoPPFrame", "0", None))
        self.combo_mtd34.setItemText(1, _translate("LiuyaoPPFrame", "1", None))
        self.combo_mtd34.setItemText(2, _translate("LiuyaoPPFrame", "2", None))
        self.combo_mtd34.setItemText(3, _translate("LiuyaoPPFrame", "3", None))
        self.label_8.setText(_translate("LiuyaoPPFrame", "第五次", None))
        self.combo_mtd35.setItemText(0, _translate("LiuyaoPPFrame", "0", None))
        self.combo_mtd35.setItemText(1, _translate("LiuyaoPPFrame", "1", None))
        self.combo_mtd35.setItemText(2, _translate("LiuyaoPPFrame", "2", None))
        self.combo_mtd35.setItemText(3, _translate("LiuyaoPPFrame", "3", None))
        self.label_7.setText(_translate("LiuyaoPPFrame", "第六次", None))
        self.combo_mtd36.setItemText(0, _translate("LiuyaoPPFrame", "0", None))
        self.combo_mtd36.setItemText(1, _translate("LiuyaoPPFrame", "1", None))
        self.combo_mtd36.setItemText(2, _translate("LiuyaoPPFrame", "2", None))
        self.combo_mtd36.setItemText(3, _translate("LiuyaoPPFrame", "3", None))
        self.groupBox_2.setTitle(_translate("LiuyaoPPFrame", "起卦时间", None))
        self.radio_time1.setText(_translate("LiuyaoPPFrame", "公历", None))
        self.radio_time2.setText(_translate("LiuyaoPPFrame", "干支", None))
        self.label_9.setText(_translate("LiuyaoPPFrame", "月", None))
        self.label_10.setText(_translate("LiuyaoPPFrame", "日", None))
        self.combo_month.setItemText(0, _translate("LiuyaoPPFrame", "子", None))
        self.combo_month.setItemText(1, _translate("LiuyaoPPFrame", "丑", None))
        self.combo_month.setItemText(2, _translate("LiuyaoPPFrame", "寅", None))
        self.combo_month.setItemText(3, _translate("LiuyaoPPFrame", "卯", None))
        self.combo_month.setItemText(4, _translate("LiuyaoPPFrame", "辰", None))
        self.combo_month.setItemText(5, _translate("LiuyaoPPFrame", "巳", None))
        self.combo_month.setItemText(6, _translate("LiuyaoPPFrame", "午", None))
        self.combo_month.setItemText(7, _translate("LiuyaoPPFrame", "未", None))
        self.combo_month.setItemText(8, _translate("LiuyaoPPFrame", "申", None))
        self.combo_month.setItemText(9, _translate("LiuyaoPPFrame", "酉", None))
        self.combo_month.setItemText(10, _translate("LiuyaoPPFrame", "戌", None))
        self.combo_month.setItemText(11, _translate("LiuyaoPPFrame", "亥", None))
        self.combo_day.setItemText(0, _translate("LiuyaoPPFrame", "甲子", None))
        self.combo_day.setItemText(1, _translate("LiuyaoPPFrame", "甲寅", None))
        self.combo_day.setItemText(2, _translate("LiuyaoPPFrame", "甲辰", None))
        self.combo_day.setItemText(3, _translate("LiuyaoPPFrame", "甲午", None))
        self.combo_day.setItemText(4, _translate("LiuyaoPPFrame", "甲申", None))
        self.combo_day.setItemText(5, _translate("LiuyaoPPFrame", "甲戌", None))
        self.combo_day.setItemText(6, _translate("LiuyaoPPFrame", "乙丑", None))
        self.combo_day.setItemText(7, _translate("LiuyaoPPFrame", "乙卯", None))
        self.combo_day.setItemText(8, _translate("LiuyaoPPFrame", "乙巳", None))
        self.combo_day.setItemText(9, _translate("LiuyaoPPFrame", "乙未", None))
        self.combo_day.setItemText(10, _translate("LiuyaoPPFrame", "乙酉", None))
        self.combo_day.setItemText(11, _translate("LiuyaoPPFrame", "乙亥", None))
        self.combo_day.setItemText(12, _translate("LiuyaoPPFrame", "丙子", None))
        self.combo_day.setItemText(13, _translate("LiuyaoPPFrame", "丙寅", None))
        self.combo_day.setItemText(14, _translate("LiuyaoPPFrame", "丙辰", None))
        self.combo_day.setItemText(15, _translate("LiuyaoPPFrame", "丙午", None))
        self.combo_day.setItemText(16, _translate("LiuyaoPPFrame", "丙申", None))
        self.combo_day.setItemText(17, _translate("LiuyaoPPFrame", "丙戌", None))
        self.combo_day.setItemText(18, _translate("LiuyaoPPFrame", "丁丑", None))
        self.combo_day.setItemText(19, _translate("LiuyaoPPFrame", "丁卯", None))
        self.combo_day.setItemText(20, _translate("LiuyaoPPFrame", "丁巳", None))
        self.combo_day.setItemText(21, _translate("LiuyaoPPFrame", "丁未", None))
        self.combo_day.setItemText(22, _translate("LiuyaoPPFrame", "丁酉", None))
        self.combo_day.setItemText(23, _translate("LiuyaoPPFrame", "丁亥", None))
        self.combo_day.setItemText(24, _translate("LiuyaoPPFrame", "戊子", None))
        self.combo_day.setItemText(25, _translate("LiuyaoPPFrame", "戊寅", None))
        self.combo_day.setItemText(26, _translate("LiuyaoPPFrame", "戊辰", None))
        self.combo_day.setItemText(27, _translate("LiuyaoPPFrame", "戊午", None))
        self.combo_day.setItemText(28, _translate("LiuyaoPPFrame", "戊申", None))
        self.combo_day.setItemText(29, _translate("LiuyaoPPFrame", "戊戌", None))
        self.combo_day.setItemText(30, _translate("LiuyaoPPFrame", "己丑", None))
        self.combo_day.setItemText(31, _translate("LiuyaoPPFrame", "己卯", None))
        self.combo_day.setItemText(32, _translate("LiuyaoPPFrame", "己巳", None))
        self.combo_day.setItemText(33, _translate("LiuyaoPPFrame", "己未", None))
        self.combo_day.setItemText(34, _translate("LiuyaoPPFrame", "己酉", None))
        self.combo_day.setItemText(35, _translate("LiuyaoPPFrame", "己亥", None))
        self.combo_day.setItemText(36, _translate("LiuyaoPPFrame", "庚子", None))
        self.combo_day.setItemText(37, _translate("LiuyaoPPFrame", "庚寅", None))
        self.combo_day.setItemText(38, _translate("LiuyaoPPFrame", "庚辰", None))
        self.combo_day.setItemText(39, _translate("LiuyaoPPFrame", "庚午", None))
        self.combo_day.setItemText(40, _translate("LiuyaoPPFrame", "庚申", None))
        self.combo_day.setItemText(41, _translate("LiuyaoPPFrame", "庚戌", None))
        self.combo_day.setItemText(42, _translate("LiuyaoPPFrame", "辛丑", None))
        self.combo_day.setItemText(43, _translate("LiuyaoPPFrame", "辛卯", None))
        self.combo_day.setItemText(44, _translate("LiuyaoPPFrame", "辛巳", None))
        self.combo_day.setItemText(45, _translate("LiuyaoPPFrame", "辛未", None))
        self.combo_day.setItemText(46, _translate("LiuyaoPPFrame", "辛酉", None))
        self.combo_day.setItemText(47, _translate("LiuyaoPPFrame", "辛亥", None))
        self.combo_day.setItemText(48, _translate("LiuyaoPPFrame", "壬子", None))
        self.combo_day.setItemText(49, _translate("LiuyaoPPFrame", "壬寅", None))
        self.combo_day.setItemText(50, _translate("LiuyaoPPFrame", "壬辰", None))
        self.combo_day.setItemText(51, _translate("LiuyaoPPFrame", "壬午", None))
        self.combo_day.setItemText(52, _translate("LiuyaoPPFrame", "壬申", None))
        self.combo_day.setItemText(53, _translate("LiuyaoPPFrame", "壬戌", None))
        self.combo_day.setItemText(54, _translate("LiuyaoPPFrame", "癸丑", None))
        self.combo_day.setItemText(55, _translate("LiuyaoPPFrame", "癸卯", None))
        self.combo_day.setItemText(56, _translate("LiuyaoPPFrame", "癸巳", None))
        self.combo_day.setItemText(57, _translate("LiuyaoPPFrame", "癸未", None))
        self.combo_day.setItemText(58, _translate("LiuyaoPPFrame", "癸酉", None))
        self.combo_day.setItemText(59, _translate("LiuyaoPPFrame", "癸亥", None))
        self.dateTimeEdit.setDisplayFormat(_translate("LiuyaoPPFrame", "yyyy/MM/dd hh:mm:ss", None))

