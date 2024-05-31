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