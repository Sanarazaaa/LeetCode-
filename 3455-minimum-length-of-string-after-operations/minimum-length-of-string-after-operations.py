class Solution:
    def minimumLength(self, s: str) -> int:
        from collections import Counter
        dict_s = dict(Counter(s))
        return sum((1 if val % 2 == 1 else 2) for key, val in dict_s.items())   