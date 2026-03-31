class MinStack:

    def __init__(self):
       self.stack = []
       self.min = []

    def push(self, val: int) -> None:
        if not self.min or val < self.min[-1]:
            self.min.append(val)
        else:
            self.min.append(self.min[-1])
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack != []:
            self.stack.pop()
            self.min.pop()

    def top(self) -> int:
        el = self.stack.pop()
        self.stack.append(el)
        return el

    def getMin(self) -> int:
        m = self.min.pop()
        self.min.append(m)
        return m