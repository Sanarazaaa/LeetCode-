class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even = []
        odd = []
        
        for i in nums:
            if i % 2 == 0:
                even.append(i)  # Add even numbers to 'even' list
            else:
                odd.append(i)   # Add odd numbers to 'odd' list
        
        # Return a new list with even numbers followed by odd numbers
        return even + odd