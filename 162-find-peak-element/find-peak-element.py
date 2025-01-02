class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums)<3):
            return(nums.index(max(nums)))
            
        for i in range(1,len(nums)-1):
            if(nums[i]>nums[i-1] and nums[i]>nums[i+1]):
                return i
            else:
                if(i==len(nums)-2):
                    return (nums.index(max(nums)))
                    
        

        