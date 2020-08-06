# anonymous pipes and threads, not processes; this version works on Windows
import os, time, threading

def child(pipeout):
    zzz = 0
    while True:
        #time.sleep(0.2) # make parent wait
        msg = ('Spam %03d' % zzz).encode() # pipes are binary bytes
        os.write(pipeout, msg) # send to parent
        zzz = (zzz+1) # goto 0 after 4
        if input() == 'q':
            os._exit(1)

def parent(pipein, code):
    while True:
        line = os.read(pipein, 32) # blocks until data sent
        print('Parent %d got [%s] at %s' % (code, line.decode(), time.time()))


def parentConc(pipein, code):
    while True:
        time.sleep(1)
        line = os.read(pipein, 32) # blocks until data sent
        print('Parent %d got [%s] at %s' % (code, line.decode(), time.time()))

pipein, pipeout = os.pipe()
threading.Thread(target=child, args=(pipeout,)).start()
threading.Thread(target=parentConc, args=(pipein, 1)).start()
threading.Thread(target=parent, args=(pipein, 2)).start()