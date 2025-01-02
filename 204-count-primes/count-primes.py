class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0  # No primes less than 2
        
        primes = [True] * n  # Initialize the list up to n (exclusive)
        primes[0] = primes[1] = False  # 0 and 1 are not prime numbers

        for p in range(2, int(n**0.5) + 1):  # Loop up to √n
            if primes[p]:  # If p is still prime
                for multiple in range(p * p, n, p):  # Mark multiples of p
                    primes[multiple] = False

        # Count the number of primes less than n
        return sum(primes)
