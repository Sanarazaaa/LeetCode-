class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # Function to process a string and simulate the typing with backspaces
        def process_string(string: str) -> str:
            result = []
            for i in string:
                if i != '#':
                    result.append(i)  # Append the character to the result list
                else:
                    if result:
                        result.pop()  # Backspace: pop the last character
            return ''.join(result)  # Convert the list to a string and return it
        
        # Process both strings and compare the results
        return process_string(s) == process_string(t)
