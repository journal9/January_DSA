# List
class Queue:
    def __init__(self):
        self.queue = []
        self.rear = -1
        self.front = 0

    def isEmpty(self):
        return self.rear == -1

    def enqueue(self,data):
        self.rear+=1
        self.queue.append(data)

    def dequeue(self):
        if self.isEmpty():
            return None
        val = self.queue[self.front]
        self.front+=1
        return val

    def printQueue(self):
        list = []
        for i in range(self.front, self.rear+1):
            list.append(self.queue[i])
        return list

q = Queue()
q.dequeue()
q.enqueue(1)
q.enqueue(3)
q.enqueue(5)
q.enqueue(7)
q.enqueue(9)
q.enqueue('g')
q.dequeue()
z = q.printQueue()
print(z)

# --------------------------------------------------------------------------------------------------
# Linked List
class Node:
    def __init__(self,data):
        self.val = data
        self.next = None
        self.prev = None

class LinkedListQueue:

    def __init__(self):
        self.head = None
        self.rear = self.head
        self.front = self.head

    def isEmpty(self):
        return not self.head

    def enqueue(self,data):
        node = Node(data)
        if self.head==None:
            self.head = node
            self.rear = self.head
            self.front = self.head
        else:
            self.rear.next = node
            self.rear = self.rear.next

    def dequeue(self):
        if self.isEmpty():
            return None
        val = self.front.val
        self.front = self.front.next
        self.head = self.head.next
        return val

    def printQueue(self):
        if self.head==None:
            return []
        lis = []
        curr = self.head
        while curr:
            lis.append(curr.val)
            curr = curr.next
        return lis
    
lq = LinkedListQueue()
lq.enqueue(100)
lq.enqueue(200)
lq.enqueue(300)
lq.enqueue(400)
lq.dequeue()
lq.enqueue(500)
cx = lq.printQueue()
print(cx)

# -------------------------------------------------------------------------------------------------------
# Stack
class Stack:
    def __init__(self):
        self.stack = ['_']*100
        self.top = -1

    def stackPush(self,data):
        self.top+=1
        self.stack[self.top] = data

    def stackPop(self):
        if self.stackEmpty():
            return None
        val = self.stack[self.top]
        self.top-=1
        return val

    def stackEmpty(self):
        
        return self.top<0
    
    # TODO: add printQueue()
    
class QueueStacks:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()
    
    def s_move(self,s1,s2):
        n = s1.top+1
        while n>0:
            val = s1.stackPop()
            s2.stackPush(val)
            n -= 1

    def s_push(self,data):
        self.stack1.stackPush(data)

    def s_pop(self):
        if not self.s_empty():
            self.s_move(self.stack1,self.stack2)
            val = self.stack2.stackPop()
            self.s_move(self.stack2,self.stack1)
            return val
        else:
            return None

    def s_empty(self):
        return self.stack1.stackEmpty()
    
qs = QueueStacks()
qs.s_push(11)
qs.s_push(22)
cc = qs.s_pop()
print(cc)

# s = Stack()
# s.stackPush(2)
# s.stackPush(7)
# x = s.stackPop()
# print(x)