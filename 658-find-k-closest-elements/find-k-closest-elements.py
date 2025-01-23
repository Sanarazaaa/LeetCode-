from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Sort the array based on the absolute difference with x
        arr.sort(key=lambda num: (abs(num - x), num))
        
        # Get the first k closest elements
        return sorted(arr[:k])
