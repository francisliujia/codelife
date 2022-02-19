import concurrent.futures 
import time 

start = time.perf_counter()

def do_something(seconds):
	print(f'sleeping {seconds} second...')
	time.sleep(seconds)
	# print('Done sleeping...')
	return f'done sleeping... {seconds}'

with concurrent.futures.ThreadPoolExecutor() as executor:

	# ----------traditional method -------
	# f1 = executor.submit(do_something, 1)
	# f2 = executor.submit(do_something, 1)
	# print(f1.result())
	# print(f2.result())
	

	secs = [5,4,3,2,1]

	#----------- use submit ---------
	# results = [executor.submit(do_something, sec) for sec in secs] # submit returns a futurn object
	# for f in concurrent.futures.as_completed(results):
	# 	print(f.result())

	# --------------- use map -----------
	results = executor.map(do_something, secs) # map returns the results
	for result in results:
		print(result)


	


finish = time.perf_counter()

print('finished in {} seconds'.format(round(finish - start, 2)))


