class MinStack:

    def __init__(self):
        self.stack=[]
        self.minimum=[pow(2,31)-1]

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minimum[-1]>=val:
            self.minimum.append(val)

    def pop(self) -> None:
        x=self.stack.pop()
        if self.minimum[-1]==x:
            self.minimum.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
       return self.minimum[-1] 


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()



# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
