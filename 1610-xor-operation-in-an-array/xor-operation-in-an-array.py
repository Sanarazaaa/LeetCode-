class Solution:
   def xorOperation(self, n: int, start: int) -> int:
   #     def xorOperation(n, start):
        result = 0
        for i in range(n):
            result ^= start + 2 * i
        return result
