class Solution:
    def reverseVowels(self, s: str) -> str:
        a = []  # List to store vowels
        for i in s:
            if i in 'aeiouAEIOU':  # Check if character is a vowel
                a.append(i)  # Append vowel to list
        
        result = []  # List to store the final result
        for i in s:
            if i in 'aeiouAEIOU':  # If it's a vowel, replace with the last vowel from 'a'
                result.append(a.pop())  # Use the reversed vowels
            else:
                result.append(i)  # Keep non-vowels as they are
        
        return ''.join(result)  # Convert list back to string
