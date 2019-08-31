#linked list
class Node:
    def __init__(self,data={}):
        self.data = data
        self.next = None
        self.prev = None
    def traverse(self):
        temp = self.head
        while True:
            print(temp.__dict__)
            temp = temp.next
            if temp.next == self.head:
                print(temp.__dict__)
                break
first=Node.head  = Node(10)
second = Node(20)
third = Node(30)
fourth = Node(40)
first.prev = None
first.next = second
second.prev = first
second.next = third
third.prev = second
third.next = fourth
fourth.prev = third
fourth.next = first

Node().traverse()
