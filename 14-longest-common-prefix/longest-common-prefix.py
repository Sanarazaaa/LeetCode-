class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        
        # Step 2: Get the first and last string from the sorted list
        first = strs[0]
        last = strs[-1]
        
        # Step 3: Compare characters in first and last strings
        i = 0
        while i < len(first) and i < len(last) and first[i] == last[i]:
            i += 1
        
        # Step 4: Return the common prefix found
        return first[:i]
