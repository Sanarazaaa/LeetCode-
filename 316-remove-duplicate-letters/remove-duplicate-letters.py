class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        seen = set()
        last_occurrence = {char: i for i, char in enumerate(s)}

        for i, char in enumerate(s):
            if char in seen:
                continue
            
            while stack and stack[-1] > char and last_occurrence[stack[-1]] > i:
                seen.remove(stack.pop())

            stack.append(char)
            seen.add(char)

        return ''.join(stack)  # Do not reverse the stack

# 'b' is added to the stack: stack = ['b']
# 'c' is added: stack = ['b', 'c']
# 'a' is encountered. Since 'a' is less than 'c', you pop 'c' from the stack. Now you would also pop 'b' if needed (but in this example, you keep 'b' because 'a' appears first). You add 'a': stack = ['a']
# Next, 'b' is added back: stack = ['a', 'b']