# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tcp.ui'
#
# Created: Wed Dec 23 15:38:43 2015
#      by: PyQt4 UI code generator 4.10.4
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(359, 397)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.server = QtGui.QLabel(Dialog)
        self.server.setObjectName(_fromUtf8("server"))
        self.horizontalLayout.addWidget(self.server)
        self.IpAddrEdit = QtGui.QLineEdit(Dialog)
        self.IpAddrEdit.setObjectName(_fromUtf8("IpAddrEdit"))
        self.horizontalLayout.addWidget(self.IpAddrEdit)
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.clientPortEdit = QtGui.QLineEdit(Dialog)
        self.clientPortEdit.setObjectName(_fromUtf8("clientPortEdit"))
        self.horizontalLayout.addWidget(self.clientPortEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.sendEdit = QtGui.QPlainTextEdit(Dialog)
        self.sendEdit.setObjectName(_fromUtf8("sendEdit"))
        self.horizontalLayout_2.addWidget(self.sendEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_4.addWidget(self.label_3)
        self.rcvEdit = QtGui.QPlainTextEdit(Dialog)
        self.rcvEdit.setObjectName(_fromUtf8("rcvEdit"))
        self.horizontalLayout_4.addWidget(self.rcvEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.conPushBtn = QtGui.QPushButton(Dialog)
        self.conPushBtn.setObjectName(_fromUtf8("conPushBtn"))
        self.verticalLayout_2.addWidget(self.conPushBtn)
        self.openBtn = QtGui.QPushButton(Dialog)
        self.openBtn.setObjectName(_fromUtf8("openBtn"))
        self.verticalLayout_2.addWidget(self.openBtn)
        self.QuitPushBtn = QtGui.QPushButton(Dialog)
        self.QuitPushBtn.setObjectName(_fromUtf8("QuitPushBtn"))
        self.verticalLayout_2.addWidget(self.QuitPushBtn)
        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.server.setText(_translate("Dialog", "IP", None))
        self.label.setText(_translate("Dialog", "Port", None))
        self.label_2.setText(_translate("Dialog", "send", None))
        self.label_3.setText(_translate("Dialog", "receive", None))
        self.conPushBtn.setText(_translate("Dialog", "Connect", None))
        self.openBtn.setText(_translate("Dialog", "Open", None))
        self.QuitPushBtn.setText(_translate("Dialog", "Quit", None))

