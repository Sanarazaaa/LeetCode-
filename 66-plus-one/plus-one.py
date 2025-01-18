class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Convert the list of digits to an integer
        n = int(''.join(map(str, digits)))
        
        # Add one to the number
        n += 1
        
        # Convert the result back to a list of digits
        return [int(digit) for digit in str(n)]
