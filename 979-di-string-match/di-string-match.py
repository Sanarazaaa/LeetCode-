class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        n = len(s)
        result = []
        low,high = 0,n
        for i in s:
            if i == 'I':
                result.append(low)
                low += 1
            else:
                result.append(high)
                high -= 1
        result.append(low)
        return result
