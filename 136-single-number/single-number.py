class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c = Counter(nums)
        for k,v in c.items(): # use the dictionary (k=2,2,2) The method .items() returns a view object that displays a list of a dictionary's key-value tuple pairs. 
            if v == 1:
                return k  