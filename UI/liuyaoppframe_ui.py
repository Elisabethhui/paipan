# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'liuyaoppframe.ui'
#
# Created: Thu Jul 18 22:19:16 2013
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
        LiuyaoPPFrame.resize(317, 580)
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
        self.groupBox_2 = QtGui.QGroupBox(LiuyaoPPFrame)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.calendar = QtGui.QCalendarWidget(self.groupBox_2)
        self.calendar.setObjectName(_fromUtf8("calendar"))
        self.verticalLayout.addWidget(self.calendar)
        self.time = QtGui.QTimeEdit(self.groupBox_2)
        self.time.setAlignment(QtCore.Qt.AlignCenter)
        self.time.setTime(QtCore.QTime(12, 0, 0))
        self.time.setObjectName(_fromUtf8("time"))
        self.verticalLayout.addWidget(self.time)
        self.formLayout.setWidget(3, QtGui.QFormLayout.SpanningRole, self.groupBox_2)
        self.groupBox_3 = QtGui.QGroupBox(LiuyaoPPFrame)
        self.groupBox_3.setTitle(_fromUtf8(""))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.btnNow = QtGui.QPushButton(self.groupBox_3)
        self.btnNow.setObjectName(_fromUtf8("btnNow"))
        self.horizontalLayout_2.addWidget(self.btnNow)
        self.btnPaipan = QtGui.QPushButton(self.groupBox_3)
        self.btnPaipan.setEnabled(True)
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
        self.edit_mtd12 = QtGui.QLineEdit(self.groupBox)
        self.edit_mtd12.setMinimumSize(QtCore.QSize(60, 20))
        self.edit_mtd12.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.edit_mtd12.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.edit_mtd12.setText(_fromUtf8(""))
        self.edit_mtd12.setMaxLength(5)
        self.edit_mtd12.setObjectName(_fromUtf8("edit_mtd12"))
        self.gridLayout.addWidget(self.edit_mtd12, 0, 2, 1, 1)
        self.radio_gua = QtGui.QRadioButton(self.groupBox)
        self.radio_gua.setObjectName(_fromUtf8("radio_gua"))
        self.gridLayout.addWidget(self.radio_gua, 1, 0, 1, 1)
        self.radio_coin = QtGui.QRadioButton(self.groupBox)
        self.radio_coin.setObjectName(_fromUtf8("radio_coin"))
        self.gridLayout.addWidget(self.radio_coin, 2, 0, 1, 1)
        self.edit_mtd2 = QtGui.QLineEdit(self.groupBox)
        self.edit_mtd2.setEnabled(False)
        self.edit_mtd2.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.edit_mtd2.setMaxLength(8)
        self.edit_mtd2.setObjectName(_fromUtf8("edit_mtd2"))
        self.gridLayout.addWidget(self.edit_mtd2, 1, 1, 1, 3)
        self.radio_number = QtGui.QRadioButton(self.groupBox)
        self.radio_number.setChecked(True)
        self.radio_number.setObjectName(_fromUtf8("radio_number"))
        self.gridLayout.addWidget(self.radio_number, 0, 0, 1, 1)
        self.edit_mtd13 = QtGui.QLineEdit(self.groupBox)
        self.edit_mtd13.setMinimumSize(QtCore.QSize(60, 20))
        self.edit_mtd13.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.edit_mtd13.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.edit_mtd13.setMaxLength(5)
        self.edit_mtd13.setObjectName(_fromUtf8("edit_mtd13"))
        self.gridLayout.addWidget(self.edit_mtd13, 0, 3, 1, 1)
        self.edit_mtd11 = QtGui.QLineEdit(self.groupBox)
        self.edit_mtd11.setMinimumSize(QtCore.QSize(60, 20))
        self.edit_mtd11.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.edit_mtd11.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.edit_mtd11.setMaxLength(5)
        self.edit_mtd11.setObjectName(_fromUtf8("edit_mtd11"))
        self.gridLayout.addWidget(self.edit_mtd11, 0, 1, 1, 1)
        self.edit_mtd31 = QtGui.QLineEdit(self.groupBox)
        self.edit_mtd31.setEnabled(False)
        self.edit_mtd31.setMinimumSize(QtCore.QSize(20, 20))
        self.edit_mtd31.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.edit_mtd31.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.edit_mtd31.setMaxLength(1)
        self.edit_mtd31.setObjectName(_fromUtf8("edit_mtd31"))
        self.gridLayout.addWidget(self.edit_mtd31, 2, 3, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 1, 1, 2)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 1, 1, 2)
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 4, 1, 1, 2)
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 5, 1, 1, 2)
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 6, 1, 1, 2)
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 7, 1, 1, 2)
        self.edit_mtd32 = QtGui.QLineEdit(self.groupBox)
        self.edit_mtd32.setEnabled(False)
        self.edit_mtd32.setMinimumSize(QtCore.QSize(20, 20))
        self.edit_mtd32.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.edit_mtd32.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.edit_mtd32.setMaxLength(1)
        self.edit_mtd32.setObjectName(_fromUtf8("edit_mtd32"))
        self.gridLayout.addWidget(self.edit_mtd32, 3, 3, 1, 1)
        self.edit_mtd33 = QtGui.QLineEdit(self.groupBox)
        self.edit_mtd33.setEnabled(False)
        self.edit_mtd33.setMinimumSize(QtCore.QSize(20, 20))
        self.edit_mtd33.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.edit_mtd33.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.edit_mtd33.setMaxLength(1)
        self.edit_mtd33.setObjectName(_fromUtf8("edit_mtd33"))
        self.gridLayout.addWidget(self.edit_mtd33, 4, 3, 1, 1)
        self.edit_mtd34 = QtGui.QLineEdit(self.groupBox)
        self.edit_mtd34.setEnabled(False)
        self.edit_mtd34.setMinimumSize(QtCore.QSize(20, 20))
        self.edit_mtd34.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.edit_mtd34.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.edit_mtd34.setMaxLength(1)
        self.edit_mtd34.setObjectName(_fromUtf8("edit_mtd34"))
        self.gridLayout.addWidget(self.edit_mtd34, 5, 3, 1, 1)
        self.edit_mtd35 = QtGui.QLineEdit(self.groupBox)
        self.edit_mtd35.setEnabled(False)
        self.edit_mtd35.setMinimumSize(QtCore.QSize(20, 20))
        self.edit_mtd35.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.edit_mtd35.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.edit_mtd35.setMaxLength(1)
        self.edit_mtd35.setObjectName(_fromUtf8("edit_mtd35"))
        self.gridLayout.addWidget(self.edit_mtd35, 6, 3, 1, 1)
        self.edit_mtd36 = QtGui.QLineEdit(self.groupBox)
        self.edit_mtd36.setEnabled(False)
        self.edit_mtd36.setMinimumSize(QtCore.QSize(20, 20))
        self.edit_mtd36.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.edit_mtd36.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.edit_mtd36.setMaxLength(1)
        self.edit_mtd36.setObjectName(_fromUtf8("edit_mtd36"))
        self.gridLayout.addWidget(self.edit_mtd36, 7, 3, 1, 1)
        self.formLayout.setWidget(2, QtGui.QFormLayout.SpanningRole, self.groupBox)
        self.label.setBuddy(self.edit_name)
        self.label_2.setBuddy(self.edit_question)

        self.retranslateUi(LiuyaoPPFrame)
        QtCore.QObject.connect(self.btnNow, QtCore.SIGNAL(_fromUtf8("clicked()")), LiuyaoPPFrame.onBtnNow)
        QtCore.QObject.connect(self.radio_number, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), LiuyaoPPFrame.onMethodToggled)
        QtCore.QObject.connect(self.radio_gua, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), LiuyaoPPFrame.onMethodToggled)
        QtCore.QObject.connect(self.radio_coin, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), LiuyaoPPFrame.onMethodToggled)
        QtCore.QObject.connect(self.btnPaipan, QtCore.SIGNAL(_fromUtf8("clicked()")), LiuyaoPPFrame.onBtnPaipan)
        QtCore.QMetaObject.connectSlotsByName(LiuyaoPPFrame)
        LiuyaoPPFrame.setTabOrder(self.edit_name, self.edit_question)
        LiuyaoPPFrame.setTabOrder(self.edit_question, self.radio_number)
        LiuyaoPPFrame.setTabOrder(self.radio_number, self.edit_mtd11)
        LiuyaoPPFrame.setTabOrder(self.edit_mtd11, self.edit_mtd12)
        LiuyaoPPFrame.setTabOrder(self.edit_mtd12, self.edit_mtd13)
        LiuyaoPPFrame.setTabOrder(self.edit_mtd13, self.radio_gua)
        LiuyaoPPFrame.setTabOrder(self.radio_gua, self.edit_mtd2)
        LiuyaoPPFrame.setTabOrder(self.edit_mtd2, self.radio_coin)
        LiuyaoPPFrame.setTabOrder(self.radio_coin, self.edit_mtd31)
        LiuyaoPPFrame.setTabOrder(self.edit_mtd31, self.edit_mtd32)
        LiuyaoPPFrame.setTabOrder(self.edit_mtd32, self.edit_mtd33)
        LiuyaoPPFrame.setTabOrder(self.edit_mtd33, self.edit_mtd34)
        LiuyaoPPFrame.setTabOrder(self.edit_mtd34, self.edit_mtd35)
        LiuyaoPPFrame.setTabOrder(self.edit_mtd35, self.edit_mtd36)
        LiuyaoPPFrame.setTabOrder(self.edit_mtd36, self.calendar)
        LiuyaoPPFrame.setTabOrder(self.calendar, self.time)
        LiuyaoPPFrame.setTabOrder(self.time, self.btnNow)
        LiuyaoPPFrame.setTabOrder(self.btnNow, self.btnPaipan)

    def retranslateUi(self, LiuyaoPPFrame):
        LiuyaoPPFrame.setWindowTitle(_translate("LiuyaoPPFrame", "Frame", None))
        self.label.setText(_translate("LiuyaoPPFrame", "Name", None))
        self.groupBox_2.setTitle(_translate("LiuyaoPPFrame", "Birthday", None))
        self.time.setDisplayFormat(_translate("LiuyaoPPFrame", "hh:mm", None))
        self.btnNow.setText(_translate("LiuyaoPPFrame", "Current Time", None))
        self.btnPaipan.setText(_translate("LiuyaoPPFrame", "PaiPan", None))
        self.label_2.setText(_translate("LiuyaoPPFrame", "Question", None))
        self.groupBox.setTitle(_translate("LiuyaoPPFrame", "Method", None))
        self.edit_mtd12.setInputMask(_translate("LiuyaoPPFrame", "99999; ", None))
        self.radio_gua.setText(_translate("LiuyaoPPFrame", "Gua code", None))
        self.radio_coin.setText(_translate("LiuyaoPPFrame", "Coins", None))
        self.edit_mtd2.setInputMask(_translate("LiuyaoPPFrame", "99999999; ", None))
        self.radio_number.setText(_translate("LiuyaoPPFrame", "Numbers", None))
        self.edit_mtd13.setInputMask(_translate("LiuyaoPPFrame", "99999; ", None))
        self.edit_mtd11.setInputMask(_translate("LiuyaoPPFrame", "99999; ", None))
        self.edit_mtd31.setInputMask(_translate("LiuyaoPPFrame", "9; ", None))
        self.label_3.setText(_translate("LiuyaoPPFrame", "First Time", None))
        self.label_4.setText(_translate("LiuyaoPPFrame", "Second Time", None))
        self.label_5.setText(_translate("LiuyaoPPFrame", "Third Time", None))
        self.label_6.setText(_translate("LiuyaoPPFrame", "Forth Time", None))
        self.label_8.setText(_translate("LiuyaoPPFrame", "Fifth Time", None))
        self.label_7.setText(_translate("LiuyaoPPFrame", "Sixth Time", None))
        self.edit_mtd32.setInputMask(_translate("LiuyaoPPFrame", "9; ", None))
        self.edit_mtd33.setInputMask(_translate("LiuyaoPPFrame", "9; ", None))
        self.edit_mtd34.setInputMask(_translate("LiuyaoPPFrame", "9; ", None))
        self.edit_mtd35.setInputMask(_translate("LiuyaoPPFrame", "9; ", None))
        self.edit_mtd36.setInputMask(_translate("LiuyaoPPFrame", "9; ", None))

