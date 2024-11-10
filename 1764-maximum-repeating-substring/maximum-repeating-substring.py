class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        count = 0
        repeated_word = word
        
        while repeated_word in sequence:
            count += 1
            repeated_word += word  # Extend repeated_word to check for more repetitions
            
        return count
