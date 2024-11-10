class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # Check if repeating the string (excluding the first and last characters) 
        # results in the same string as `s`
        return s in (s + s)[1:-1]
