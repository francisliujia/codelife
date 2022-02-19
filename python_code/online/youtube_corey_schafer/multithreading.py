# threading ==> for i/o bound tasks: reading and writing files
# mutiprocessing ==> cpu bound: doing data crunching 
import threading
import time 

start = time.perf_counter()

def do_something(seconds):
	print(f'sleeping {seconds} second...')
	time.sleep(seconds)
	print('Done sleeping...')

# do_something()
# do_something()

# t1 = threading.Thread(target=do_something)
# t2 = threading.Thread(target=do_something)

# t1.start()
# t2.start()

# t1.join()
# t2.join()

threads = []
for _ in range(10): # _ is a throw-away variable, we don't use anything within the loop 
	t = threading.Thread(target=do_something, args=[1.5])
	t.start()
	threads.append(t)

for thread in threads:
	thread.join()



finish = time.perf_counter()

print('finished in {} seconds'.format(round(finish - start, 2)))






