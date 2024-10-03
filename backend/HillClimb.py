from multiprocess import Pool, Pipe, Value

def init_pool_worker(tmp_best_fitness):
	global best_fitness
	best_fitness = tmp_best_fitness

def hill_climb(
		decrypt_function,
		cipher,
		copy_function,
		starting_key,
		output = None,
		modify_key = None,
		iterations = 10000,
		annealing = 1,
		shuffle_function = None,
		temperature = 30,
		end = 0,
		threaded = 0,
		fitness_mode = 0,
		spaces = 0,
		fitness_ngram = 4,
		adaptive_iterations = 0,
		nums = 1,
		pipe = None):
	if end:
		from nostril import nonsense

	from math import exp, inf
	import Fitness
	Fitness.init(fitness_ngram, spaces = spaces)
	fitness_function = lambda x:(Fitness.cal_avg_fitness if fitness_mode else Fitness.cal_fitness)(x, True, spaces, nums)
	from random import random
	i = 0
	if adaptive_iterations:
		last_improvement = 0

	max_key = copy_function(starting_key)
	key = copy_function(max_key)
#	max_decryption = decrypt_function(key, cipher)
	max_decryption = cipher
	max_fitness = -inf
#	max_fitness = fitness_function(max_decryption, 1, spaces)
	if threaded:
		global best_fitness

	else:
		from time import ctime
		best_fitness = max_fitness
		best_key = copy_function(max_key)

	if annealing:
		cooling = temperature/iterations

	try:
		while 1:
			key = modify_key(max_key)
#			if key == max_key:
#				continue
			decryption = decrypt_function(key, cipher)
#			print(decryption)
			fitness = fitness_function(decryption)
#			temperature=30-(cooling*i)
			difference = fitness-max_fitness
			if difference > 0:	# If the fitness has improved
				if adaptive_iterations:
					last_improvement = max(last_improvement - (0.3*difference*iterations), 0)

				max_decryption, max_fitness, max_key = decryption, fitness, copy_function(key)

				if threaded:
					if max_fitness > best_fitness.value:
						pipe.send((max_decryption, max_fitness, max_key, False))
				else:
					if max_fitness > best_fitness:	# If a better key was found, keep it
						best_decryption, best_fitness, best_key = max_decryption, max_fitness, copy_function(max_key)
						output(best_fitness, ctime(), best_key, best_decryption)

			elif difference < 0:	# If the fitness was gotten worse
				if annealing and (random() < exp(difference/temperature)):	# This equation with e was taken from the internet
					if adaptive_iterations:
						last_improvement = max(last_improvement-(0.3*iterations), 0)
					max_decryption, max_fitness, max_key = decryption, fitness, copy_function(key)
				else:
					if annealing and temperature-cooling > 0:
						temperature -= cooling
					i += 1
					if adaptive_iterations:
						last_improvement += 1
#			else:
#				print("ok")
			if ((not adaptive_iterations) and (i >= (iterations-1))) or \
			(adaptive_iterations and (last_improvement >= (iterations-1))):	# If hitting the limit of iterations before restarting
				i = 0
				if annealing:
					temperature = 30

				else:
					shuffle_function(max_key)

				if adaptive_iterations:
					last_improvement = 0

				# max_decryption, max_fitness, max_key = decryption, fitness, key
				if threaded:
					pipe.send((max_decryption, max_fitness, max_key, True))
	
				if (not threaded) and end and (not nonsense(max_decryption)):
					raise KeyboardInterrupt()
	except KeyboardInterrupt:
		if threaded:
			pipe.close()
		else:
			return best_decryption, best_key

def threaded_hill_climb(
		decrypt_function,
		cipher,
		copy_function,
		starting_keys,
		output = None,
		modify_key = None,
		iterations = 10000,
		annealing = 1,
		shuffle_function = None,
		temperature = 30,
		end = 0,
		fitness_mode = 0,
		spaces = 0,
		fitness_ngram = 4,
		adaptive_iterations = 0,
		nums = 1,
		same_key = 0,
		threads = None):
	from os import cpu_count
	from time import ctime, sleep
	from math import inf
	if end:
		from nostril import nonsense
	if threads == None:
		if same_key:
			threads = cpu_count()//2
		else:
			threads = len(starting_keys)
	best_decryption = decrypt_function(starting_keys if same_key else starting_keys[0], cipher if same_key else cipher[0])
	best_fitness = Value("d", -inf, lock = False)
	best_key = starting_keys if same_key else starting_keys[0]
	pipes = [Pipe(False) for i in range(threads)]
	pool = Pool(threads, init_pool_worker, (best_fitness,))
#	result = pool.starmap(hill_climb, ((
	result = pool.starmap_async(hill_climb, ((
			decrypt_function,
			(cipher if same_key else cipher[i]),
			copy_function,
			starting_keys if same_key else starting_keys[i],
			output,
			modify_key,
			iterations,
			annealing,
			shuffle_function,
			temperature,
			end,
			1,
			fitness_mode,
			spaces,
			fitness_ngram,
			adaptive_iterations,
			nums,
			pipes[i][1]
		)
		for i in range(threads)
	))
	try:
		while 1:
			sleep(0.5)
			if result.ready() and not result.successful():
				result.get()
				pool.terminate()
				break
			for i in range(len(pipes)):
				while pipes[i][0].poll():
					received = pipes[i][0].recv()
					if received[1] > best_fitness.value:
						best_decryption, best_fitness.value, best_key = received[:-1]
						output(best_fitness.value, ctime(), best_key, best_decryption)

					if end and received[3] and (not nonsense(received[0])):
						break
			else:
				continue
			break
	except KeyboardInterrupt:
		pass
	finally:	
		pool.terminate()
	return best_decryption, best_key