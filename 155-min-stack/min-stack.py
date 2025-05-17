class MinStack:
    def __init__(self):
        self.stack = []
        self.mini = float('inf')

    def push(self, val):
        if not self.stack:
            self.mini = val
            self.stack.append(val)
        else:
            if val < self.mini:
                encoded_val = 2 * val - self.mini
                self.stack.append(encoded_val)
                self.mini = val
            else:
                self.stack.append(val)

    def pop(self):
        if not self.stack:
            return
        top = self.stack.pop()
        if top < self.mini:
            self.mini = 2 * self.mini - top
        if not self.stack:
            self.mini = float('inf')  # Reset when stack becomes empty

    def top(self):
        if not self.stack:
            return -1
        top = self.stack[-1]
        if top < self.mini:
            return self.mini
        return top

    def getMin(self):
        if not self.stack:
            return -1
        return self.mini
