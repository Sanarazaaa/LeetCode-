# we can use enumerate. but why? it can acess value as well as the index number.
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool: #this will take in the nums as list in integers and k is also in integers. the result will in boolean
        num_indices = {}
        for i, num in enumerate(nums):
            if num in num_indices and i - num_indices[num] <= k:
                return True
            num_indices[num] = i
        return False