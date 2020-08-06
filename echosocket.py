from socket import *
import threading

myHost = ''
myPort = 5007

sockObj = socket(AF_INET, SOCK_STREAM)
sockObj.bind((myHost, myPort))
sockObj.listen(5)


def handleclient(connection):
    while True:
        data = connection.recv(10)
        if not data:
            break
        connection.send(b'echo => '+data)
    connection.close()


print('listenning ...')
while True:
    socket, address = sockObj.accept()
    print('Server connected by ', address)
    threading.Thread(target=handleclient, args=(socket,)).start()

