class Solution:
    def findRepeatedDnaSequences(self, s: str):
        # Dictionary to store the count of each substring
        substring_count = defaultdict(int)
        result = []
        
        # Loop through the string and extract 10-length substrings
        for i in range(len(s) - 9):  # len(s) - 9 to ensure we get 10 characters
            substring = s[i:i+10]
            substring_count[substring] += 1
        
        # Check the dictionary and collect substrings that appear more than once
        for substring, count in substring_count.items():
            if count > 1:
                result.append(substring)
        
        return result
