class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.head = None
       
    def printlist(self):
    	self.head = temp
    	while temp != None:
    		print(self.data)
    		temp.next = next   
zero = Node(18)
first = Node(12)
second = Node(13)
third = Node(14)
Node.head = zero
zero.next = first
first.next = second
second.next = third
print(zero.__dict__)
print(Node.__dict__)
print(first.__dict__)
print(third.__dict__)
print(second.__dict__)
print(Node().printlist())
