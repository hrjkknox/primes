import multiprocessing as mp
import math

def isPrime(n):
	# Easy results
	if (n == 2) or (n == 3):
		return True
	if (n < 2) or (n % 2 == 0):
		return False
	if n < 9:
		return True
	if n % 3 == 0:
		return False
	# Since all primes > 3 are of the form 6n±1,
	# start with i = 5 (which is prime) and test
	# i, i+2 for being prime, then loop by 6
	h = int(n**0.5)

	i = 5
	while i <= h:
		if n % i == 0:
			return False
		if n % (i + 2) == 0:
			return False
		i += 6
	
	return True

# Returns a list of prime numbers fom min to max (inclusive)
def getPrimesFromRange(min, max):
	output = []
	for i in range(min, max+1):
		if isPrime(i):
			output.append(i)
	return output

# A version of getPrimesFromRange with a single argument
# (this is the only way I've figured out so far to make it parallel-able)
def p_getPrimesFromRange(p):
	return getPrimesFromRange(p[0], p[1])

# Creates a list of ranges for each process to use
def getRanges(min, max):
	# The max number of cores we can use
	noOfProcessors = mp.cpu_count()
	# The number of numbers we have to process
	noOfNumbers = max - min + 1
	# The size of chunk each core has to process
	# (if it doesn't divide equally, one core will have to do slightly more)
	chunkSize = round(noOfNumbers / noOfProcessors)

	# The data to be output
	ranges = []

	# Turn the chunk size into an array of ranges
	i = min
	j = min + math.floor(chunkSize)
	while i <= max:
		ranges.append([i, j-1])
		i += math.floor(chunkSize)
		j += math.floor(chunkSize)

	# Make sure we dont process any more or less than we need to
	ranges[-1][1] = max

	return ranges
		
# Divides the workload of finding primes, and finds them
def findPrimesInParallel(min, max):
	ranges = getRanges(min, max)
	
	pool = mp.Pool()
	# Spawn an adequate number of processes
	pool = mp.Pool(processes=len(ranges))
	# Map the functions to the processes
	results = pool.map(p_getPrimesFromRange, ranges)
	output = []
	# Loop through the processes and combine their outputs
	for i in results:
		output += i
	return output

if __name__ == "__main__":
	print(findPrimesInParallel(1, 100))
