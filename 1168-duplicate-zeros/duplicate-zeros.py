class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        n = len(arr)
        zeros = arr.count(0)  # Count how many zeros we need to duplicate
        
        # Start from the end and work backwards to avoid overwriting
        i = n - 1
        while i >= 0:
            if arr[i] == 0:
                # Shift the elements to the right
                if i + zeros < n:
                    arr[i + zeros] = 0
                zeros -= 1
                if i + zeros < n:
                    arr[i + zeros] = 0
            else:
                # Move the element to its new position
                if i + zeros < n:
                    arr[i + zeros] = arr[i]
            i -= 1
