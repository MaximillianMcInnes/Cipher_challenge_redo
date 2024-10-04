def hill_climb(decrypt_function, cipher, copy_function, starting_key, output, modify_key, iterations = 10000, end = False, threaded = False, fitness_mode = 0, spaces = False):
	if threaded:
		global best_decryption, best_fitness, best_key, exp, ctime, Fitness, fitness_function, random, lock, stop#, Decimal
		if end:
			global nonsense
	else:
		if end:
			from nostril import nonsense
#		from decimal import Decimal, getcontext
		from math import exp
		from time import ctime
		import Fitness
#		getcontext().prec = 20
		Fitness.init(spaces = spaces)
		fitness_function = Fitness.cal_avg_fitness if fitness_mode else Fitness.cal_fitness
		from random import random
		stop = False
	i = 0
	max_key = copy_function(starting_key)
	key = copy_function(max_key)
	max_decryption = decrypt_function(key, cipher)
	max_fitness = fitness_function(max_decryption, True, spaces)
	if not threaded:
		best_fitness = max_fitness
		best_key = copy_function(max_key)
	cooling = 30/iterations
	try:
		while not stop:
			key = modify_key(max_key)
			if key==max_key:
				continue
			decryption = decrypt_function(key, cipher)
			fitness = fitness_function(decryption, True, spaces)
			temperature=30-(cooling*i)
			dF = fitness-max_fitness
			if dF > 0:	# If the fitness has improved
				max_decryption, max_fitness, max_key = decryption, fitness, key
				if threaded:
					lock.acquire()
				if max_fitness>best_fitness:	# If a better key was found, use it
					best_decryption, best_fitness, best_key = max_decryption, max_fitness, copy_function(max_key)
					output(best_fitness, ctime(), best_key, best_decryption)
				if threaded:
					lock.release()
			elif dF < 0:	# If the fitness was gotten worse
				if random() < exp(dF/temperature):	# This equation with e was taken from the internet
					max_decryption, max_fitness, max_key = decryption, fitness, key
					if threaded:
						lock.acquire()
					if max_fitness>best_fitness:	# If a better key was found, use it
						best_decryption, best_fitness, best_key = max_decryption, max_fitness, copy_function(max_key)
						output(best_fitness, ctime(), best_key, best_decryption)
					if threaded:
						lock.release()
				else:
					i+=1
			elif threaded:	# If a better key was used and made the same best result, take note
				lock.acquire()
				if len(max_key)<len(best_key):
					best_decryption, best_fitness, best_key = decryption, fitness, copy_function(key)
					output(best_fitness, ctime(), best_key, best_decryption)
				lock.release()
			if i>=iterations-1:
				max_fitness, max_key = fitness, key
				i = 0
				if threaded:
					lock.acquire()
				if max_fitness>best_fitness:	# If a better key was found in this climb take note of the key
					best_decryption, best_fitness, best_key = max_decryption, max_fitness, copy_function(max_key)
					output(best_fitness, ctime(), best_key, best_decryption)
				if end and (not nonsense(max_decryption)):
					if threaded:
						lock.release()
					break
				if threaded:
					lock.release()
	except KeyboardInterrupt:
		pass
	finally:
		if threaded and lock.locked():
			lock.release()
	if not threaded:
		return best_decryption, best_key
def threaded_hill_climb(decrypt_function, cipher, copy_function, starting_keys, output, modify_key, iterations = 10000, end = False, fitness_mode = 0, spaces = False):
	global best_decryption, best_fitness, best_key, threading, exp, ctime, Fitness, fitness_function, random, lock, stop#, Decimal
	if end:
		global nonsense
		from nostril import nonsense
	import threading
	from math import exp
	from time import ctime, sleep
	import Fitness
#	from decimal import Decimal, getcontext
#	getcontext().prec = 50
	Fitness.init(spaces = spaces)
	fitness_function = Fitness.cal_avg_fitness if fitness_mode else Fitness.cal_fitness
	from random import random
	best_decryption = decrypt_function(starting_keys[0], cipher[0] if isinstance(cipher, list) else cipher)
	best_fitness = Fitness.cal_fitness(best_decryption)
	best_key = starting_keys[0]
	stop = False
	lock = threading.Lock()
	threads = [threading.Thread(target=hill_climb, args=(
		decrypt_function,
		cipher[i] if isinstance(cipher, list) else cipher,
		copy_function,
		starting_keys[i],
		output,
		modify_key,
		iterations,
		end,
		True,
		spaces)) for i in range(len(starting_keys))]
	for i in range(len(threads)):
		threads[i].start()
	try:
		if end:
			while 1:
				for i in range(len(threads)):
					if not threads[i].is_alive():
						break
					sleep(1/(len(threads)))
				else:
					continue
				break
		else:
			while 1:
				sleep(10)
	except KeyboardInterrupt:
		pass
	stop = True
	for i in range(len(threads)):
		threads[i].join()
	return best_decryption, best_key
# def threaded_hill_climb(decrypt_function: function, cipher, copy_function: function, starting_keys: list, output: function, modify_key: function, iterations = 10000, end = True, fitness_mode = 0, spaces = False):
# 	global best_decryption, best_fitness, best_key, exp, ctime, Fitness, fitness_function, random, lock, stop
# 	from multiprocessing import Process, Lock
# 	if end:
# 		global nonsense
# 		from nostril import nonsense
# 	from math import exp
# 	from time import ctime, sleep
# 	import Fitness
# 	Fitness.init(spaces = spaces)
# 	fitness_function = Fitness.cal_avg_fitness if fitness_mode else Fitness.cal_fitness
# 	from random import random
# 	best_decryption = decrypt_function(starting_keys[0], cipher[0] if isinstance(cipher, list) else cipher)
# 	best_fitness = Fitness.cal_fitness(best_decryption)
# 	best_key = starting_keys[0]
# 	stop = False
# 	lock = Lock()
# 	processes = [Process(target=hill_climb, args=(decrypt_function, cipher[i] if isinstance(cipher, list) else cipher, copy_function, starting_keys[i], output, modify_key, iterations, end, fitness_mode, spaces)) for i in range(len(starting_keys))]
# 	for i in range(len(processes)):
# 		processes[i].start()
# 	try:
# 		if end:
# 			while 1:
# 				for i in range(len(processes)):
# 					if not processes[i].is_alive():
# 						break
# 					sleep(1/(len(processes)))
# 				else:
# 					continue
# 				break
# 		else:
# 			while 1:
# 				sleep(10)
# 	except KeyboardInterrupt:
# 		pass
# 	stop = True
# 	for i in range(len(processes)):
# 		processes[i].join()