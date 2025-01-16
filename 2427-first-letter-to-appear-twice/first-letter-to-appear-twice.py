class Solution:
    def repeatedCharacter(self, s: str) -> str:
       seen = []
       for char in s:
           if char in seen:
               return char  # Return the character directly
           seen.append(char)
