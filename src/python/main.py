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
	# f, f+2 for being prime, then loop by 6
	halfway = int(n**0.5)

	i = 5
	while i <= halfway:
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

