class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return True if word.islower() or word.isupper() or word.istitle() else False        