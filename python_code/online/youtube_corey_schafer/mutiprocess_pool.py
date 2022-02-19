import concurrent.futures
import time 


def do_something(seconds):
	print(f'sleeping {seconds} second...')
	time.sleep(seconds)
	return f'done sleeping...{seconds}'

if __name__ == "__main__":
	start  = time.perf_counter()

	# do_something()
	# do_something()
	# p1 = multiprocessing.Process(target=do_something)
	# p2 = multiprocessing.Process(target=do_something)
	
	# p1.start()
	# p2.start()

	# p1.join()
	# p2.join()

	# processes = []
	# for _ in range(10):
	# 	p = multiprocessing.Process(target=do_something, args=[1.5])
	# 	p.start()
	# 	processes.append(p)

	# for processe in processes:
	# 	processe.join()


	with concurrent.futures.ProcessPoolExecutor() as executor:
		
		# ---------- method 1 -------
		# f1 = executor.submit(do_something, 1)
		# f2 = executor.submit(do_something, 1)
		# print(f1.result())
		# print(f2.result()) 


		# ---------method 2 ---------
		secs = [5, 4, 3, 2, 1]
		# results = [executor.submit(do_something, sec) for sec in secs]
		# for f in concurrent.futures.as_completed(results):
		# 	print(f.result())


		# --------------- use map -----------
		results = executor.map(do_something, secs) # map returns the results
		for result in results:
			print(result)

	finish = time.perf_counter()
	print(f'finished in {round(finish - start, 2)} seconds(s)')




