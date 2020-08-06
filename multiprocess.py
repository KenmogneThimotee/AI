import os
from multiprocessing import Process, Lock


def whoami(label, lk):
    msg = '%s: name:%s, pid:%s'
    with lk:
        print(msg % (label, __name__, os.getpid()))


if __name__ == '__main__':
    lock = Lock()
    whoami('function call', lock)

    p = Process(target=whoami, args=('child call', lock))
    p.start()
    p.join()

    for i in range(5):
        Process(target=whoami, args=(('run process %s' % i), lock)).start()

    with lock:
        print('main process exit ...')
