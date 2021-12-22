import time
import pyperclip

print('press ENTER to begin. Then, press ENTER to click the stopwatch'
      'press Ctrl-c to quit')

input()
print('started')
start_time = time.time()
last_time = start_time
lap_num = 1

try:
    while True:
        input()
        lap_time = round(time.time() - last_time, 2)
        total_time = round(time.time() - start_time, 2)
        
        lap = 'lap # {} {} ({})'.format((str(lap_num) + ':').ljust(3),
                                        str(lap_num).ljust(5),
                                        str(lap_time).rjust(6))

        print(lap, end='')
        lap_num += 1
        last_time = time.time()
        pyperclip.copy(lap)
except KeyboardInterrupt:
    print('\nDone')