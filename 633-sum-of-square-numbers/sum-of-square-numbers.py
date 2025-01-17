import math

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        b = int(math.isqrt(c))  # Fixed method for integer square root
        while a <= b:  # Loop until a exceeds b
            current_sum = a**2 + b**2
            if current_sum == c:  # Check if the sum matches c
                return True
            elif current_sum < c:  # If sum is too small, increase a
                a += 1
            else:  # If sum is too large, decrease b
                b -= 1
        return False  # If no pair is found, return False
 

# sum function takes iterable, not two separate arguments. it should be a**2+b**2
# 