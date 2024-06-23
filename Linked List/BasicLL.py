class Node:
    def __init__(self,data,next=None) -> None:
        self.data = data
        self.next = next

class MyLinkedList:
    def __init__(self) -> None:
        self.head = None

    #insert at trail
    def insert(self,data):
        newNode = Node(data)
        if self.head:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = newNode
        else:
            self.head = newNode

    #insert at head
    def insertHead(self,data):
        newNode = Node(data) 
        if self.head:
            newNode.next = self.head
        self.head = newNode

    #print a linked list
    def getLL(self):
        if self.head:
            curr = self.head
            while curr:
                print(curr.data)
                curr = curr.next
        else:
            print('')
    
    #delete from trail
    def deleteTrail(self):
        if self.head==None:
            print("Nothing to delete")
        else:
            curr = self.head
            while curr.next.next:
                curr = curr.next
            curr.next = None
    
    #delete from head
    def deleteHead(self):
        if self.head==None:
            print("Nothing to delete")
        else:
            if self.head.next:
                self.head = self.head.next

    #find size of linked list
    def length(self)-> int:
        length = 0
        if self.head:
            curr = self.head
            while curr:
                length+=1
                curr = curr.next
        return length
    
    # Get node data at an index
    def atIndex(self,idx):
        if idx > self.length():
            raise(IndexError)
        else:
            curr = self.head
            for i in range(idx):
                curr = curr.next
            return curr.data

    # Check if a value exists    
    def exists(self,value):
        curr = self.head
        while curr:
            if curr.data == value:
                return True
            curr = curr.next 
        return False
    
    #insert node at i index
    def insertAt(self,idx,data):
        newNode = Node(data)
        if idx ==0:
            newNode.next = self.head
            self.head = newNode
        else:
            curr = self.head
            for _ in range(idx-1):
                curr = curr.next
            newNode.next = curr.next
            curr.next = newNode      

    # remove node from an index
    def removeAt(self,idx):
        curr = self.head
        for _ in range(idx-1):
            curr = curr.next
        curr.next = curr.next.next

    def remove(self,value):
        if self.head == None:
            print('Linked List is empty')
            return
        else:
            curr = self.head
            if curr.data == value:
                self.head = curr.next
                return
            while curr:
                if curr.next.data == value:
                    curr.next = curr.next.next
                    return
                curr = curr.next

    # Reverse a linked list
    def reverse(self):
        if not self.head:
            return 
        prev = self.head
        curr = prev.next
        prev.next = None
        while curr:
            nexx = curr.next
            curr.next = prev
            prev = curr
            curr = nexx
        self.head = prev
        return 
    
    def reverseBetween(self, B, C):
        if self.head==None or self.head.next==None:
            return
        curr = self.head
        for _ in range(1,B-1):
            curr = curr.next
        if curr==self.head and B==1:
            inti = None
            prev = curr
        else:
            inti = curr
            prev = curr.next
        cs = prev
        cur = prev.next
        for _ in range(B,C):
            nex = cur.next
            cur.next = prev
            prev = cur
            cur = nex
        if inti!=None:
            inti.next = prev
        else:
            self.head = prev
        cs.next = cur
        return

    
ll = MyLinkedList()
ll.head = Node(1)

for i in range(2,11):
    ll.insert(i)
ll.getLL()
print('-----------------')

ll.deleteTrail()
ll.getLL()
print('-----------------')

ll.deleteHead()
ll.getLL()
print('-----------------')

ll.insertHead(10)
ll.getLL()
print('-----------------')

len = ll.length()
print(len)
print('-----------------')

value = ll.atIndex(5)
print(value)
print('-----------------')

b = ll.exists(10)
print(b)
print('-----------------')

ll.insertAt(0,17)
ll.getLL()
print('-----------------')

ll.removeAt(8)
ll.getLL()
print('-----------------')

ll.remove(17)
ll.getLL()
print('-----------------')

ll.reverse()
ll.getLL()
print('-----------------')

ll.reverseBetween(2,3)
ll.getLL()
print('-----------------')