class Node:
    def __init__(self,data={}):
        self.data = data
        self.next = None
        self.prev = None
    def gfg(self):
        self.head = None

def traverse():
    temp = input()
    while temp.next != None:
        print(temp.__dict__)
        temp = Node(temp.next)
first =Node.gfg.head = Node(10)
second = Node(20)
third = Node(30)
fourth = Node(40)
Node.gfg.head.prev = None
Node.gfg.head.next = second
second.prev = Node.gfg.head
second.next = third
third.prev = second
third.next = fourth
fourth.prev = third
fourth.next = None
print(Node.gfg.head.__dict__)
print(second.next.__dict__)
print(type(second))
traverse()
