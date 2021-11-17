package main

import (
	//"fmt"
	"math"
)

func isPrime(n int) bool {
	/* Easy results */
	if (n == 2) || (n == 3) {
		return true
	}
	if (n < 2) || (n%2 == 0) {
		return false
	}
	if n < 9 {
		return true
	}
	if n%3 == 0 {
		return false
	}

	/* 
	 * Since all primes >3 are of the form 6n±1,
	 * start with i = 5 (which is prime) and test
	 * i, i+2 for being prime, then loop by 6
	 */
	h := int(math.Round(math.Sqrt(float64(n))))

	i := 5
	for i <= h {
		if n % i == 0 {
			return false
		}
		if n % (i + 2) == 0 {
			return false
		}
		i += 6
	}

	return true

}


