class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def get_value(word):
            return int(''.join(str(ord(i) - ord('a')) for i in word))
        
        # Get the numerical values of the three words
        first_value = get_value(firstWord)
        second_value = get_value(secondWord)
        target_value = get_value(targetWord)
        
        # Check if the sum of first and second equals target
        return first_value + second_value == target_value        