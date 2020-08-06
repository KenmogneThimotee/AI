from socket import *
import sys

serverHost = 'localhost'
serverPort = 50007

message = [b'hello network world']

if len(sys.argv) > 1:
    serverHost = sys.argv[1]# server from cmd line arg 1
    if len(sys.argv) > 2: # text from cmd line args 2..n
        message = (x.encode() for x in sys.argv[2:])

def client(msg):
    sockObj = socket(AF_INET, SOCK_STREAM)
    sockObj.connect((serverHost, serverPort))

    sockObj.send(line)
    data = sockObj.recv(1024)
    print('server response => ', data.decode())

    sockObj.close()

for line in message:
    client(line)