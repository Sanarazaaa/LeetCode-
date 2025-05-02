class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        
        # Base case: If the array has only one element, return that element.
        if l == r:
            return nums[l]
        
        while l <= r:
            mid = (l + r) // 2
            
            # Check if mid is greater than the next element
            if mid + 1 < len(nums) and nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            
            # Check if mid is smaller than the previous element
            if mid - 1 >= 0 and nums[mid] < nums[mid - 1]:
                return nums[mid]
            
            # If the left part is sorted, search in the right half
            if nums[mid] >= nums[l]:
                l = mid + 1
            # If the right part is sorted, search in the left half
            else:
                r = mid - 1
        
        # If the loop ends, it means the array is not rotated and the minimum is nums[0]
        return nums[0]
