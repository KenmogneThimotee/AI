import _thread as thread, time

stdoutmutex = thread.allocate_lock()
exitmutex = [thread.allocate_lock() for _ in range(5)]

def counter(myId, count): # function run in threads
    stdoutmutex.acquire()
    for i in range(count):
        time.sleep(1)  # simulate real work
        print('[%s] => %s' % (myId, i))
    stdoutmutex.release()
    exitmutex[myId].acquire()


mutex = thread.allocate_lock()
for i in range(5):# spawn 5 threads
    thread.start_new_thread(counter, (i, 5)) # each thread loops 5 times
    time.sleep(2)

for mutex in exitmutex:
    while not mutex.locked():
        pass
print('Main thread exiting.')


