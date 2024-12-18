class Solution:
    def finalString(self, s: str) -> str:
        i = 0
        while i < len(s):
            if s[i] == "i":
                s = s[:i][::-1] + s[i+1:]
                i = 0  # Restart checking from the beginning after modification
            else:
                i += 1
        return s
   