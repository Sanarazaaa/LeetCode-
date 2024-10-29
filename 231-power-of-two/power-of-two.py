class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
# class Solution:
#     def isPowerOfThree(self, n: int) -> bool:
#         # Check if n is a positive integer
        if n < 1:
            return False 
        while n % 2 == 0:    # Divide n by 3 as long as it is divisible by 3
            n = n// 2                 
        return n == 1 # If n equals 1, it is a power of 3