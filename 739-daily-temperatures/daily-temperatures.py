class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []  # stack to store indices of temperatures
        ans = [0] * len(temperatures)  # answer array initialized with 0

        for i, temp in enumerate(temperatures):
            # Check if we can pop from the stack (i.e., find a greater temperature)
            while stack and temperatures[stack[-1]] < temp:
                idx = stack.pop()
                ans[idx] = i - idx  # calculate the distance to the next greater temperature
            stack.append(i)  # push the current index onto the stack

        return ans
