class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        found = []
        n = sorted(nums)  # Sort the list
        for i in range(len(n)):  # Iterate over the sorted list
            if n[i] == target:
                found.append(i)
        return found
