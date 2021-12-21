import time 

print('Press ENTER to begin. Then, press ENTER to "start" the stopwatch'
	'Press Ctrl-C to quit')
input()
print('started')
start_time = time.time()
last_time = start_time
lapNum = 1

try:
	while True:
		input()
		lapTime = round(time.time() - last_time, 2)
		total_time = round(time.time() - start_time, 2)
		print('Lap #%s: %s (%s)' % (lapNum, total_time, lapTime), end='')
		lapNum += 1 
		last_time = time.time()

except KeyboardInterrupt:
	print('\nDone.')
