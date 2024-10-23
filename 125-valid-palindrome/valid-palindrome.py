# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         for i in s:
#             clean_s = ''.join(filter(str.isalnum, s)).lower()   # Check if the cleaned string is a palindrome. this basically cleans the string. it removes alphanumeric. the purpose of filter is to removes all non-alphanumeric characters from the string s, leaving only letters and numbers. the purpose of join is to join the remaining characters into a single continuous string. the purpose of lowercae is to changes all characters in the resulting string to lowercase. 
#         return clean_s == clean_s[::-1]

# the above code doesn't work because of the time limit exceed. i am interating over i, whihc is not essential. 

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Clean the string only once
        clean_s = ''.join(filter(str.isalnum, s)).lower()
        # Check if the cleaned string is a palindrome
        return clean_s == clean_s[::-1]
