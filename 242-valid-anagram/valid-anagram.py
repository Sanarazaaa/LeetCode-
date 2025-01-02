class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Check if lengths are the same
        if len(s) != len(t):
            return False
        
        # Compare the frequency counts of characters in both strings
        return Counter(s) == Counter(t)

        
        