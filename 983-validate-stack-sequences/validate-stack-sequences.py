class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i = 0
        for n in pushed: # first of all add the elements from the pushed to the stack
            stack.append(n)
            while stack and stack[-1] == popped[i]: #if the stack is not empty and the last element in the stack is equal to the popped[i] then remove that element from the stack (next line of code) and after that increase i. in the first case, that i will move to 5 now in the popped. 
                stack.pop()
                i +=1
        return not stack

