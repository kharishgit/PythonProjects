class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None
    def printLL(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, end="->")
                n = n.ref

    def add_begin(self, data):
        nn = Node(data)
        nn.ref = self.head
        self.head = nn

    def add_end(self,data):
        nn = Node(data)
        if self.head is None:
            self.head = nn
            nn.ref = None
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = nn
            nn.ref = None

    def add_after_node(self,data,x):
        n= self.head
        while n is not None:
            if n.data == x:
                break
            n= n.ref
        if n is None:
            print("The node is not available")
        else:
            nn = Node(data)
            nn.ref = n.ref
            n.ref = nn

    def add_before(self, data, x):
        if self.head is None:
            print("Linked List is empty")
            return
        if self.head.data == x:
            nn = Node(data)
            nn.ref = self.head
            self.head = nn
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n.ref is None:
            print("Node not found")
        else:
            nn = Node(data)
            nn.ref = n.ref
            n.ref = nn

    def delete_begin(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            self.head = self.head.ref

LL1= LinkedList()
LL1.add_begin(10)
LL1.add_begin(20)
LL1.add_begin(30)
LL1.add_end(5)
LL1.add_end(3)
LL1.add_end(1)
LL1.add_after_node(120,10)
LL1.add_before(555,5)
LL1.delete_begin()
LL1.printLL()


