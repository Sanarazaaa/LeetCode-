class Solution:
    def removeStars(self, s: str) -> str:
        result = []
        for char in s:
            if char == '*':
                if result:
                    result.pop()  # Remove the last character if '*' is found
            else:
                result.append(char)  # Add characters to result if not '*'
        return ''.join(result)  # Join the list back into a string
