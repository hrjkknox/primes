#include <stdio.h>
#include <math.h>

/* Returns 1 if an integer is prime, 0 if not */
int isPrime(int n) {

	if ((n == 2) || (n == 3)) {
		return 1;
	}
	if ((n < 2) || (n % 2 == 0)) {
		return 0;
	}
	if (n < 9) {
		return 1;
	}
	if (n % 3 == 0) {
		return 0;
	}

	double decimalh = sqrt((double) n);
	int h = (int) (decimalh + 0.5);

	int i = 5;
	while (i <= h)
	{
		if ((n % i) == 0) {
			return 0;
		}
		if (n % (i + 2) == 0) {
			return 0;
		}

		i += 6
	}

	return 1;
	
}
