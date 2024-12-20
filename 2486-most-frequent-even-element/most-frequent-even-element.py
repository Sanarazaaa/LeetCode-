class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        d ={}
        for i in nums:
            if i%2==0:
                d[i] = d.get(i,0)+1
        
        if d=={}:
            return -1
        x= max(d.values())
        mn = float('inf')
        for k,v in d.items():
            if v==x:
                mn = min(k,mn)
        return mn