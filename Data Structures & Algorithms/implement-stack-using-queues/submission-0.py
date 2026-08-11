class MyStack:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        n = len(self.queue)
        for i in range(n-1):
            val = self.queue[0]
            del self.queue[0]
            self.queue.append(val)

        val = self.queue[0]
        del self.queue[0]

        return val
        

    def top(self) -> int:
        n = len(self.queue)
        for i in range(n):
            val = self.queue[0]
            del self.queue[0]
            self.queue.append(val)

        return val
        

    def empty(self) -> bool:
        if len(self.queue) == 0:
            return True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()