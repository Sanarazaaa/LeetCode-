class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:

        # Step 1: Count the occurrences of each character
        counter = Counter(s)
        
        # Step 2: Extract the occurrence values
        occurrences = list(counter.values())
        
        # Step 3: Check if all occurrences are the same
        return len(set(occurrences)) == 1        