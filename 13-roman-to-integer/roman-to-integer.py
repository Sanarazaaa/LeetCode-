class Solution:
    def romanToInt(self, s: str) -> int:
        roman_values = {
    'I': 1, 'V': 5, 'X': 10, 'L': 50,
    'C': 100, 'D': 500, 'M': 1000
}
        total = 0
        i = 0
        
        while i < len(s):
            if i < len(s) - 1 and roman_values[s[i]] < roman_values[s[i + 1]]:
                total -= roman_values[s[i]]  # Subtract current value
            else:
                total += roman_values[s[i]]  # Add current value
            
            i += 1  # Move to the next character

        return total
