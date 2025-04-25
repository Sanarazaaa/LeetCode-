class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        num_set = set(nums)
        visited = set()
        res = []

        for i in nums:
            if i in visited:
                continue

            visited.add(i)
            length = 1
            j = i + 1
            k = i - 1

            while j in num_set:
                visited.add(j)
                length += 1
                j += 1

            while k in num_set:
                visited.add(k)
                length += 1
                k -= 1

            res.append(length)

        return max(res)
