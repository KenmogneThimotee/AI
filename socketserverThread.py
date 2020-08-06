import socketserver, time # get socket server, handler objects

myHost = '' # server machine, '' means local host
myPort = 50007 # listen on a non-reserved port number


def now():
    return time.ctime(time.time())


class MyClientHandler(socketserver.BaseRequestHandler):
    def handle(self): # on each client connect
        print(self.client_address, now())#show this client's address
        time.sleep(5) # simulate a blocking activity
        while True: # self.request is a client socket
            data = self.request.recv(1024) # read, write a client socket
            if not data: break
            reply = 'Echo=>%s at %s' % (data, now())
            self.request.send(reply.encode())
            self.request.close()
    def finish(self) -> None:
        self.request.close()


#make a threaded server, listen/handle clients forever
myaddr = (myHost, myPort)
server = socketserver.ThreadingTCPServer(myaddr, MyClientHandler)
server.serve_forever()

