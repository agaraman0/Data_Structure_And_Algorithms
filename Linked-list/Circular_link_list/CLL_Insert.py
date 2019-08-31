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
    def insatbeg(self):
        temp = self.head
        hold = temp
        while True:
            temp = temp.next
            if temp.next == self.head:
                x = input()
                newnode = Node(x)
                newnode.next = hold
                temp.next = newnode
                newnode.prev = temp
                Node.head = newnode
                break
    def insatend(self):
        temp = self.head
        hold = temp
        while True:
            temp = temp.next
            if temp.next == self.head:
                x = input()
                newnode = Node(x)
                newnode.next = hold
                temp.next = newnode
                newnode.prev = temp
                break
    def insert(self):
        z = int(input())
        count = 1
        temp = self.head
        while True:
            current = temp
            temp = temp.next
            count +=1
            if z == count:
                if temp == None:
                    return Node().insatend()
                else:
                    w = input()
                    new = Node(w)
                    current.next = new
                    new.next = temp
                    new.prev = temp.prev
                    temp.prev = new
                    break
            elif z == 1:
                return Node().insatbeg()
first=Node.head  = Node(10)
second = Node(20)
third = Node(30)
fourth = Node(40)
first.prev = fourth
first.next = second
second.prev = first
second.next = third
third.prev = second
third.next = fourth
fourth.prev = third
fourth.next = first

Node().insert()
Node().traverse()
