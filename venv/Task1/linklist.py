import random
class Node:
    def __init__(self,value = None, next = None):
        self.value= value
        self.next = next

class LinkList:
    def __init__(self):
        self.first = None
        self.last = None
        self.lenght = 0

    def __str__(self):
        if self.first != None:
            current = self.first
            out = 'List [' + str(current.value) + ' '
            while current.next != None:
                current = current.next
                out += str(current.value) + ' '
            return  out + ']'
        return 'List []'

    def clear(self):
        self.__init__()

    def add(self,x):
        self.lenght+=1
        if self.first ==None:
            self.first= self.last=Node(x,None)
        else:
            self.last.next =self.last =Node(x,None)

    def sort(self):
        a = Node(0, None)
        b = Node(0, None)
        c = Node(0, None)
        e = Node(0, None)
        tmp = Node(0, None)

        while (e != self.first.next):
            c = a = self.first
            b = a.next

            while a != e:
                if a and b:
                    if a.value > b.value:
                        if a == self.first:
                            tmp = b.next
                            b.next = a
                            a.next = tmp
                            self.first = b
                            c = b
                        else:
                            tmp = b.next
                            b.next = a
                            a.next = tmp
                            c.next = b
                            c = b
                    else:
                        c = a
                        a = a.next
                    b = a.next
                    if b == e:
                        e = a
                else:
                    e = a

    def lenght(self):
        return (lenght)

    def createList(self):
        temp = self.first
        list1 = []
        while (temp != None):
            list1.append(temp.value)
            temp = temp.next
        return list1
