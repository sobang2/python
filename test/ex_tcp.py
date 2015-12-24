#!/usr/bin/env python3
#tcp server
from socket import *
import asyncore

class AsyncServer(asyncore.dispatcher):
    def __init__(self,port):
        asyncore.dispatcher.__init__(self)
        self.port = port
        self.create_socket(AF_INET,SOCK_STREAM)
        self.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.bind(('localhost',port))
        self.listen(5)
        print("listening on port",self.port)

    def handle_accepted(selfself, csock, addr):
        print("accepted",addr)
        return EchoHandler(sock=csock)

class EchoHandler(asyncore.dispatcher):
    def __init__(self,sock=None):
        asyncore.dispatcher.__init__(self,sock)
        self.incom_data = b''
        self.write_queue = []

    def handle_read(self):
        data = self.recv(512)
        self.incom_data =data
        self.write_queue.append(data)
        print('got message',data.decode())

    def writable(self):
        return self.write_queue

    def handle_write(self):
        if self.write_queue:
            msg = self.write_queue.pop(0)
            print('sending..',msg.decode())
            sent = self.send(msg)
        # if not self.write_queue:
        #     print('closing..')
        #     self.close()

class Client(asyncore.dispatcher):
    def __init__(self,host,port,data):
        asyncore.dispatcher.__init__(self)
        if(data=="START"):
            self.create_socket(AF_INET, SOCK_STREAM)
            self.connect((host,port))
        self.message = data
    def handle_connect(self):
        print('connect')
        pass
    def handle_expt(self):
        self.close()

    def writable(self):
        return self.message
    def handle_write(self):
        if self.message:
            self.sendall(self.message.encode())
            self.message = 0
    def handle_read(self):
        global gdata
        s=self.recv(20)
        if s:
            print(s.decode())
            gdata=s.decode()

    def handle_close(self):
        print('close')
        self.close()

server = AsyncServer(5555)
asyncore.loop()