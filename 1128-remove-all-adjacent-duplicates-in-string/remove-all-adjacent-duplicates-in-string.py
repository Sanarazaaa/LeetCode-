class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []  # Use a stack to keep track of characters
        for char in s:  # Iterate through each character in the string
            if stack and stack[-1] == char:  # If the last character in the stack is the same as the current character
                stack.pop()  # Remove the last character from the stack (remove duplicates)
            else:
                stack.append(char)  # Otherwise, add the current character to the stack
        return ''.join(stack)  # Convert the stack back to a string and return it
