class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        # First, count how many zeros are in the list
        zeros = arr.count(0)
        n = len(arr)
        
        # Start from the end of the list and work backwards
        i = n - 1
        
        # We will shift elements and duplicate zeros as we go
        while i >= 0:
            if arr[i] == 0:
                # Shift the zero
                if i + zeros < n:
                    arr[i + zeros] = 0
                # Decrease the count of zeros left to duplicate
                zeros -= 1
                if i + zeros < n:
                    arr[i + zeros] = 0
            else:
                # Just move the element to the right
                if i + zeros < n:
                    arr[i + zeros] = arr[i]
            i -= 1
