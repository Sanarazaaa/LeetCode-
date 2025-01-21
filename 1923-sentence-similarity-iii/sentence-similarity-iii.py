class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        tokens1 = sentence1.split()
        tokens2 = sentence2.split()
        left = 0
        right1 = len(tokens1) - 1
        right2 = len(tokens2) - 1
        
        # Increment left pointer while tokens are matching from the start
        while left < len(tokens1) and left < len(tokens2) and tokens1[left] == tokens2[left]:
            left += 1
        
        # Decrement right pointers while tokens are matching from the end
        while right1 >= left and right2 >= left and tokens1[right1] == tokens2[right2]:
            right1 -= 1
            right2 -= 1

        # Return True if all remaining tokens can be considered matched
        return left > right1 or left > right2
