class Solution:
    def isValid(self, s: str) -> bool:
        t = []
        for i in range(len(s)):
            if s[i] in '([{':
                t.append(s[i])  # Push opening bracket onto the stack
            elif s[i] in ')]}':
                if len(t)==0 :  # If stack is empty, there's no opening bracket to match
                    return False
                # Check if the current closing bracket matches the last opening bracket
                if (s[i] == ')' and t[-1] != '(') or \
                   (s[i] == ']' and t[-1] != '[') or \
                   (s[i] == '}' and t[-1] != '{'):
                    return False
                t.pop()  # Pop the last opening bracket after a match
        return len(t) == 0  # Return True if all brackets were matched (stack should be empty)
