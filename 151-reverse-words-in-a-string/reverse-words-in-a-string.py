class Solution:
    def reverseWords(self, s: str) -> str:
        if s == "": #check whether the variable is an empty string or not.
            return ""
        else:
            return ' '.join(reversed(s.split()))        