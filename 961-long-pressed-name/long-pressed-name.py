class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i, j = 0, 0  # Pointers for name and typed
        while j < len(typed):
            if i < len(name) and name[i] == typed[j]:
                # Move both pointers if characters match
                i += 1
            elif j == 0 or typed[j] != typed[j - 1]:
                # If no match and the current character is not a long press
                return False
            # Move the typed pointer
            j += 1
        # Ensure all characters in name are matched
        return i == len(name)


