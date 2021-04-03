import threading, time
print('Start of program')

def take_nap(sleep, number):
    time.sleep(sleep)
    print('End of thread %s.' % number)

thread1 = threading.Thread(target=take_nap, kwargs={'sleep': 8, 'number': 1})
thread2 = threading.Thread(target=take_nap, kwargs={'sleep': 12, 'number': 2})
thread3 = threading.Thread(target=take_nap, kwargs={'sleep': 3, 'number': 3})
thread1.start()
thread2.start()
thread3.start()

print('End of program.')