import os

def child():
    print('Hello from child ', os.getpid())
    os._exit(0) #else goes back to the parent

print(dir(os))


def parent():
    while True:
        new_pid = os.fork()
        if new_pid == 0:
            child()
        else:
            print('Hello from parent ', os.getpid(), new_pid)
            if input() == 'q':
                break


parent()