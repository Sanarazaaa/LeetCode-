class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # Check if n is a positive integer
        if n < 1:
            return False 
        while n % 4 == 0:    # Divide n by 4 as long as it is divisible by 4
            n = n// 4                 
        return n == 1 # If n equals 1, it is a power of 4