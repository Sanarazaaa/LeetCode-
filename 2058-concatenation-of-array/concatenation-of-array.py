class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return [*nums, *nums]  # Unpack and concatenate nums to itself
