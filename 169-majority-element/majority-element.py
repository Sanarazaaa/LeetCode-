class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0 # initiate a counter element
        majority_ele = None
# Used Boyer-Moore Voting Algorithm 
        for num in nums:
            if count == 0:
                majority_ele = num #nums = [3,2,3]. num = 3, count = 1 and majority_ele to 3.
            if num == majority_ele: 
                count += 1
            else:
                count -= 1
        if nums.count(majority_ele) > len(nums) // 2:
            return majority_ele
        else:
            return -1
