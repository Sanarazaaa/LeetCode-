class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        while columnNumber > 0:
            columnNumber -= 1  # Adjust for 1-based indexing
            remainder = columnNumber % 26
            result.append(chr(remainder + ord('A')))  # Convert to corresponding letter
            columnNumber //= 26  # Move to the next "digit"
        return ''.join(reversed(result))  # Reverse the result for the correct order
        