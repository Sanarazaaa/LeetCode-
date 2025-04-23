class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_row_sum = sum(accounts[0]) #max_row = accounts[0] -- this is how to get the first row
        for i in range(1, len(accounts)):
            current_sum = sum(accounts[i])
            if max_row_sum < current_sum:
                max_row_sum = current_sum
        return max_row_sum