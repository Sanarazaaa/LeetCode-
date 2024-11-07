class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split()  # Splits the sentence into a list of words
        
        for index, word in enumerate(words, 1):  # Iterating through the words
            if word.startswith(searchWord):  # Check if word starts with searchWord
                return index  # Returns 1-based index of the first match
            
        return -1  # If no word starts with searchWord
