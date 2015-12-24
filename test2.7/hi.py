#!/bin/python

import socket;
import sys;
import Tkinter;

def Connect():
	global Connected, Socket;

	if( Connected == False ):
		Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
		Socket.connect(('127.0.0.1', 5555));
		print "Connected to server";
		Connected = True;
	else:
		print "Allready connected to server";

def Disconnect():
	global Connected, Socket;

	if( Connected == True ):
		Socket.shutdown(2);
		Socket.close();
		Socket = "";
		print "Disconnected from server";
		Connected = False;
	else:
		print "Not connected to server";

def Exit():
	global Connected, Socket;

	if( Connected == True ):
		Socket.close();
	print "We zijn klaar";
	sys.exit();

def Receive():
	global Connected, Socket;

	if( Connected == True ):
		Received = Socket.recv(1024);
		print "Received: ", Received;
	else:
		print "Not connected to server";

Socket = "";
Connected = False;
Tkinter.Label(text = "Welcome!").pack();
Tkinter.Button(text = "Connect", command = Connect).pack();
Tkinter.Button(text = "Disconnect", command = Disconnect).pack();
Tkinter.Button(text = "Receive", command = Receive).pack();
Tkinter.Button(text = "Exit", command = Exit).pack();
Tkinter.mainloop();

