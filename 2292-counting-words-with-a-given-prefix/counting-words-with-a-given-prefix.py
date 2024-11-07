class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        # No need to split the list, as it's already in list format.
        
        count = 0  # To count how many words start with 'pref'
        
        for i, word in enumerate(words):
            if word.startswith(pref):
                count += 1

        
        return count  # Return the total count of words that start with 'pref'
