class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Base case: Any number to the power of 0 is 1
        if n == 0:
            return 1
        # If the exponent is negative, take the reciprocal of x and use the positive exponent
        elif n < 0:
            return 1 / self.myPow(x, -n)
        # If the exponent is even, use the optimized method (divide and conquer)
        elif n % 2 == 0:
            half = self.myPow(x, n // 2)
            return half * half
        # If the exponent is odd, reduce it by 1 (turn it into an even exponent)
        else:
            return x * self.myPow(x, n - 1)
