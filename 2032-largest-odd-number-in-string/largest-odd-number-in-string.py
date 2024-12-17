class Solution:
    def largestOddNumber(self, num: str) -> str:
        """
        Finds the largest odd-numbered substring in the given string 'num'.
        """
        # Start iterating from the end of the string
        for index in range(len(num) - 1, -1, -1):  # Backward loop
            current_digit = int(num[index])  # Convert current character to an integer
            
            # Check if the current digit is odd
            if current_digit % 2 != 0:
                # Return the substring from the start to the current position (inclusive)
                return num[:index + 1]
        
        # If no odd digits are found, return an empty string
        return ""
