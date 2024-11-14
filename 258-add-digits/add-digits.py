class Solution:
    def addDigits(self, num: int) -> int:
        # Add digits until the number is a single digit
        while num >= 10:  # Continue until the number is a single digit
            digit_sum = 0  # Reset the sum for each iteration
            while num > 0:
                digit_sum += num % 10  # Add the last digit to the sum
                num = num // 10  # Remove the last digit
            num = digit_sum  # Update num with the new sum of digits
        return num  # Return the single digit result
