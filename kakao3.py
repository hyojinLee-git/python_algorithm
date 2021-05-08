class Node(object):
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class DList(object):
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None, self.head)
        self.head.next = self.tail
        self.size = 0

    def listSize(self):
        return self.size

    def is_empty(self):
        if self.size != 0:
            return False
        else:
            return True

    def selectNode(self, idx):
        if idx > self.size:
            print("Overflow: Index Error")
            return None
        if idx == 0:
            return self.head
        if idx == self.size:
            return self.tail
        if idx <= self.size // 2:
            target = self.head
            for _ in range(idx):
                target = target.next
            return target
        else:
            target = self.tail
            for _ in range(self.size - idx):
                target = target.prev
            return target

    def appendleft(self, value):
        if self.is_empty():
            self.head = Node(value)
            self.tail = Node(None, self.head)
            self.head.next = self.tail
        else:
            tmp = self.head
            self.head = Node(value, None, self.head)
            tmp.prev = self.head
        self.size += 1

    def append(self, value):
        if self.is_empty():
            self.head = Node(value)
            self.tail = Node(None, self.head)
            self.head.next = self.tail
        else:
            tmp = self.tail.prev
            newNode = Node(value, tmp, self.tail)
            tmp.next = newNode
            self.tail.prev = newNode
        self.size += 1

    def insert(self, value, idx):
        if self.is_empty():
            self.head = Node(value)
            self.tail = Node(None, self.head)
            self.head.next = self.tail
        else:
            tmp = self.selectNode(idx)
            if tmp == None:
                return
            if tmp == self.head:
                self.appendleft(value)
            elif tmp == self.tail:
                self.append(value)
            else:
                tmp_prev = tmp.prev
                newNode = Node(value, tmp_prev, tmp)
                tmp_prev.next = newNode
                tmp.prev = newNode
        self.size += 1

    def delete(self, idx):
        if self.is_empty():
            print("Underflow Error")
            return
        else:
            tmp = self.selectNode(idx)
            if tmp == None:
                return
            elif tmp == self.head:
                tmp = self.head
                self.head = self.head.next
            elif tmp == self.tail:
                tmp = self.tail
                self.tail = self.tail.prev
            else:
                tmp.prev.next = tmp.next
                tmp.next.prev = tmp.prev
            del (tmp)
            self.size -= 1

    def printlist(self):
        target = self.head
        while target != self.tail:
            if target.next != self.tail:
                print(target.data, '<=> ', end='')
            else:
                print(target.data)
            target = target.next

n=int(input())
k=int(input())
cmd=["D 2","C","U 3","C","D 4","C","U 2"]
d=DList()

for i in range(n):
    d.append(i)
"""
present=d.selectNode(k)
#print(present)
delete=0

for order in cmd:
    if order[0]=='D':
        k+=int(order[2])
        present=d.selectNode(k)
    elif order[0]=='U':
        k-=int(order[2])
        present = d.selectNode(k)
    elif order[0]=='C':
        delete=present
        d.delete(k)
        if k==d.listSize():
            k-=1
        else:
            k+=1
        present=d.selectNode(k)
    #elif order[0]=='Z':
"""
t=int(input())
while t>0:
    t-=1
    order=input().split()
    op=order[0]
    if op=='D':
        k+=int(order[1])
    elif op=='U':
        k-=int(order[1])
    elif op=='C':
        d.delete(k)
        k-=1
    d.printlist()
