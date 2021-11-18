import java.lang.Math;
import java.util.ArrayList;

public class Primes {
	public static boolean isPrime(int n) {
		/* Easy results */
		if ((n == 2) || (n == 3)) {
			return true;
		}
		if ((n < 2) || (n % 2 == 0)) {
			return false;
		}
		if (n < 9) {
			return true;
		}
		if (n % 3 == 0) {
			return false;
		}

		/*
		 * Since all primes >3 are of the form 6n±1,
		 * start with i = 5 (which is prime) and test
		 * i, i+2 for being prime, then loop by 6
		 */
		
		float decimalH = Math.sqrt(n);
		int h = Math.round(decimalH);

		int i = 5;
		while (i <= h) {
			if (n % i == 0) {
				return false;
			}
			if (n % (i + 2) == 0) {
				return false;
			}
			i += 6;
		}

		return true;
	}


}