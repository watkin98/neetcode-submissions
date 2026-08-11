class MyQueue:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        tempStack = []

        for _ in range(len(self.stack)):
            tempStack.append(self.stack.pop())
        
        res = tempStack.pop()

        for _ in range(len(tempStack)):
            self.stack.append(tempStack.pop())

        return res


    def peek(self) -> int:
        tempStack = []

        for _ in range(len(self.stack)):
            tempStack.append(self.stack.pop())
        
        res = tempStack[len(tempStack) - 1]

        for _ in range(len(tempStack)):
            self.stack.append(tempStack.pop())

        return res
        

    def empty(self) -> bool:
        return len(self.stack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()