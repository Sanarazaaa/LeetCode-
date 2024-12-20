class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        # Create a Counter for even numbers
        even_count = Counter()
        for index, number in enumerate(nums):  # Using enumerate
            if number % 2 == 0:  # Check if the number is even
                even_count[number] += 1
        
        if not even_count:  # If no even numbers, return -1
            return -1
        
        # Find the most frequent even number
        most_frequent = sorted(even_count.items(), key=lambda x: (-x[1], x[0]))
        return most_frequent[0][0]
