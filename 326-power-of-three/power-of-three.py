class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # Check if n is a positive integer
        if n < 1:
            return False 
        while n % 3 == 0:    # Divide n by 3 as long as it is divisible by 3
            n = n// 3                 
        return n == 1 # If n equals 1, it is a power of 3