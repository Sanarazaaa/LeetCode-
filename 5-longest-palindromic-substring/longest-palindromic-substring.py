class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Transform the string by inserting '#' between every character and at the ends
        T = '#'.join('^{}$'.format(s))  # Add sentinel characters to avoid bounds checking
        n = len(T)
        P = [0] * n  # Array to store the radius of the palindrome around each center
        C = R = 0  # Center and right edge of the rightmost palindrome
        
        for i in range(1, n - 1):
            # Mirror of i with respect to center C
            P[i] = (R > i) and min(R - i, P[2 * C - i])  # Avoid expanding beyond right edge
            
            # Expand the palindrome around i
            while T[i + P[i] + 1] == T[i - P[i] - 1]:
                P[i] += 1
            
            # Update the center and right edge if needed
            if i + P[i] > R:
                C, R = i, i + P[i]
        
        # Find the maximum palindrome radius and its center
        max_len, center_index = max((n, i) for i, n in enumerate(P))
        
        # Return the longest palindromic substring
        return s[(center_index - max_len)//2 : (center_index + max_len)//2]
