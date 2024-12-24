class Solution:
    def reverseVowels(self, s: str) -> str:
        # Step 1: Find all vowels and store them in a list
        vowels = [i for i in s if i in 'aeiouAEIOU']
        
        # Step 2: Reverse the list of vowels
        vowels.reverse()
        
        # Step 3: Create the result by replacing vowels in original string with reversed vowels
        result = []
        for i in s:
            if i in 'aeiouAEIOU':  # If the character is a vowel
                result.append(vowels.pop(0))  # Replace it with the first vowel from the reversed list
            else:
                result.append(i)  # If it's not a vowel, keep it as is
        
        # Step 4: Join the list back into a string and return
        return ''.join(result)
