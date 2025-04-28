class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr_sum = sum(nums[:k]) # take first the sum
        max_avg = sum(nums[:k]) / k # find the average of that first sum
        for i in range(k,len(nums)):
            curr_sum = curr_sum - nums[i-k]+nums[i] # slide the window. the first window is 1,12,-5,-6,50,3
            max_avg = max(max_avg, curr_sum / k)  #take the average
        return max_avg