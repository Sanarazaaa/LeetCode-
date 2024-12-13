class Solution:
    def shortestPalindrome(self, s: str) -> str:
        reversed_s = s[::-1]
        for i in range(len(s)):
            if s[:len(s) - i] == reversed_s[i:]:
                return reversed_s[:i] + s
        return reversed_s + s


