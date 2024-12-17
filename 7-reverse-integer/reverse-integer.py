class Solution:
    def reverse(self, x: int) -> int:
        # Step 1: Determine the sign of the number
        sign = -1 if x < 0 else 1
        
        # Step 2: Reverse the absolute value of x
        reversed_x = int(str(abs(x))[::-1])
        
        # Step 3: Restore the sign
        reversed_x = sign * reversed_x
        
        # Step 4: Check for overflow (32-bit integer limits)
        if reversed_x < -2**31 or reversed_x > 2**31 - 1:
            return 0
        
        # Step 5: Return the valid reversed integer
        return reversed_x
