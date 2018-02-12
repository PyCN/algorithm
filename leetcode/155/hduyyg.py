# author:2632158294@qq.com
# github:https://github.com/PyCN/algorithm/tree/master/leetcode/155

class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)        

    def pop(self):
        """
        :rtype: void
        """
        if len(self.stack) < 1:
            print('no element in stack!!')
            return 
        if self.stack[-1] == self.min_stack[-1]: del self.min_stack[-1]
        del self.stack[-1]

    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) < 1:
            print('no element in stack!!')
            return None
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.stack) < 1:
            print('no element in stack!!')
            return None
        return self.min_stack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()