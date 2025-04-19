class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pointer = 0
        for char in t: # If the current character from t is equal to the current character in s
            if pointer == len(s):
                return True
            if char == s[pointer]:
                pointer +=1
        return pointer == len(s)
                