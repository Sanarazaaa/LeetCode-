class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = set()  # Use a set to avoid duplicate entries
        
        # Iterate over each word with index i
        for i in range(len(words)):
            # Check if words[i] is a substring in any other word
            for j in range(len(words)):
                if i != j and words[i] in words[j]:  # Ensure we aren't comparing the word to itself
                    result.add(words[i])  # Add to the set if it's found as a substring
        
        return list(result)  # Convert set back to list before returning

#use set to prevent duplicates automatically, so if a word is found as a substring multiple times, it’s only added once.