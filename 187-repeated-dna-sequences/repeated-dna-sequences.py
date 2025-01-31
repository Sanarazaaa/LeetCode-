class Solution:
    def findRepeatedDnaSequences(self, s: str):
        # Dictionary to store the count of each substring
        substring_count = {}
        result = set()  # Using a set to store repeated substrings
        
        # Loop through the string and extract 10-length substrings
        for i in range(len(s) - 9):  # len(s) - 9 to ensure we get 10 characters
            substring = s[i:i+10]
            if substring in substring_count:
                # If substring already appeared once, add it to result
                result.add(substring)
            else:
                substring_count[substring] = 1
        
        return list(result)  # Convert set to list before returning
