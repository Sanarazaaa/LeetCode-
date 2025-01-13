class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()          # Step 1: Split the string into words
        reversed_words = [word[::-1] for word in words]  # Step 2: Reverse each word
        result = ' '.join(reversed_words)  # Step 3: Join the reversed words into a string
        return result
