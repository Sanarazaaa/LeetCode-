class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for char in s:
            if char.isdigit():  # Check if current character is a digit
                # Remove the closest previous non-digit character if it exists
                if stack and not stack[-1].isdigit():
                    stack.pop()  # Remove the last non-digit from stack
            else:
                # Otherwise, just add the character to the stack
                stack.append(char)
        
        return "".join(stack)
