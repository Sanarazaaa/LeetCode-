class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # First, find the first odd number greater than or equal to low
        if low % 2 == 0:
            low += 1
        
        # Then find the last odd number less than or equal to high
        if high % 2 == 0:
            high -= 1
        
        # If low is greater than high after adjustment, return 0
        if low > high:
            return 0
        
        # Count the number of odd numbers between low and high
        return (high - low) // 2 + 1
