import time

print('Press ENETER to begin. Afterward, press ENTER to click the stopwatch. Press CTRL-C to quit.')
input()
print('Started')
start_time = time.time()
last_time = start_time
lap = 1

try:
    while True:
        input()
        lap_time = round(time.time() - last_time, 2)
        total_time = round(time.time() - start_time, 2)
        print('Lap %s: %s (%s)' % (lap, total_time, lap_time), end = '')
        lap += 1
        last_time = time.time()
except KeyboardInterrupt:
    print('\nDone.')