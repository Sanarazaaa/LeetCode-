class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):  # Iterate backwards
            if digits[i] < 9:
                digits[i] += 1  # Simply add 1
                return digits  # Return if no carry
            digits[i] = 0  # Set to 0 if it was 9
        
        # If we finish the loop, all digits were 9
        return [1] + digits  # Prepend 1
