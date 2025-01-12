class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        isdecreasing = False
        isincreasing = False 
        for i in range(1, len(nums)):  
            if nums[i] > nums[i - 1]:  
                isincreasing = True
            elif nums[i] < nums[i - 1]:  
                isdecreasing = True
        
        return not (isincreasing and isdecreasing)  # Monotonic if not both increasing and decreasing
