#!/usr/bin/env python3
import sys
from PyQt4 import QtCore, QtGui
from testgui import Ui_Dialog
from socket import *
import asyncore
con_flag = 0


class MyWindow(QtGui.QDialog):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.conPushBtn.clicked.connect(self.conbtn_clicked)
        self.ui.openBtn.clicked.connect(self.openbtn_clicked)
        self.ui.QuitPushBtn.clicked.connect(self.close)
        self.Socket = ""
    def openbtn_clicked(self):
        global con_flag
        if(con_flag==1):
            con_flag = 0
            self.ui.clientPortEdit.setEnabled(True)
            self.ui.IpAddrEdit.setEnabled(True)
            self.ui.conPushBtn.setText("connect")
            self.Socket.close()
            self.Socket=""
        else:
            print("Not connected to server")
    def conbtn_clicked(self):
        global con_flag
        send_data = self.ui.sendEdit.toPlainText()
        cliIp = self.ui.IpAddrEdit.text()
        cliPort = int(self.ui.clientPortEdit.text())
        if(con_flag==0):
            con_flag=1
            self.ui.IpAddrEdit.setEnabled(False)
            self.ui.clientPortEdit.setEnabled(False)
            self.ui.conPushBtn.setText("Send")
            self.ui.openBtn.setText("Disconnect")
            self.Socket=socket(AF_INET, SOCK_STREAM)
            self.Socket.connect((cliIp,cliPort))
        else:
            self.Socket.send(send_data.encode())
            s=self.Socket.recv(30)
            print(s)
            self.ui.rcvEdit.setPlainText(s.decode())
            s=""
        self.ui.sendEdit.setPlainText('')
    def close(self,event):
        global  con_flag
        if(con_flag==1):
            self.Socket.close()
        self.destroy()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    sys.exit(app.exec_())

