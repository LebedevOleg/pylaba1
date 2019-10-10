class Stack:
    def __init__(self):
        self.items = []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def __str__(self):
        out = ""
        for i in self.items:
            out += i + ' '
        return out
    def is_empty(self):
        return (self.items == [])
    def clear(self):
        self.items = []
    def task1(self):
        list = []
        for i in self.items:
            x = len(i)- 1
            y = 0
            k = 0
            while x- y >= y:
                if i[x- y] == i[y]:
                    y+=1
                else:
                    k = 1
                    break
            if k == 0:
                list.append(i)
        return list