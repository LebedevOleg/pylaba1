class Queue:
    def __init__(self):
        self.queue = []
        self.max = 50
    def __str__(self):
        out = ""
        for i in self.queue:
            out +=str(i) + " "
        return out
    def clear(self):
        self.queue[:] = []

    def add(self, x):
        if len(self.queue) == self.max:
            return None
        self.queue.append(x)
    def dequeue(self):
        if not self.queue:
            return (None)
        return self.queue.pop(0)
    def task(self):
        task = 0
        for i in self.queue:
            s =0
            for j in range(1,i):
                if i%j==0:
                    s+=j
            if s == i or i == 1:
                task +=1
                print (i)
        return task
