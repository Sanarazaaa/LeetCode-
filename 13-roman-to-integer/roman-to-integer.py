# the idea is to subtract the previous with the current (e.g: 9 --> X - I = IX = 9)
# when we want to substract something, then we need to have one value in -1; this is to ensure that we can subtract.
# s = 10 ; i = 0  ; line # 15 -> 0 < 10; line 16 --> if 0  
# Iteration with i = 0:
# If I just wrote roman_values[s[i]] < roman_values[s[i + 1]] without the length check:
# It would attempt to access s[1], which does not exist. Result? IndexError.

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_values = {
    'I': 1, 'V': 5, 'X': 10, 'L': 50,
    'C': 100, 'D': 500, 'M': 1000
}
        total = 0
        i = 0 
        
        while i < len(s): # this condition is essential because we dont want to have an index error. for instance, s = IX, here, len = 2, so i = 0, and i = 1 should be used. if we use don't mention this relation, then i would then become (2+1) which is something that aint present here (next line)
            if i < len(s) - 1 and roman_values[s[i]] < roman_values[s[i + 1]]:
                total -= roman_values[s[i]]  # Subtract current value
            else:
                total += roman_values[s[i]]  # Add current value
            
            i += 1  # Move to the next character

        return total
