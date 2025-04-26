# 1d list is a simple list. not a list inside a list
# 0-indexed means: First element is at index 0, second at index 1, third at index 2, etc.
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        result = []
        if m*n == len(original):
            for i in range(0,len(original),n):
                result.append(original[i:i+n])
        return result


