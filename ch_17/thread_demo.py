import threading, time
print('Start of program')

def take_nap():
    time.sleep(5)
    print('Wake up!!!')

threadObj = threading.Thread(target=take_nap)
threadObj.start()

print('End of program.')