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
    def delatend(self):
        temp = self.head
        hold = temp
        while True:
            current = temp
            temp = temp.next
            if temp.next == self.head:
                current.next = temp.next
                hold.prev = current
                temp = None
                break
    def delatbeg(self):
        temp = self.head
        hold = temp.next
        while True:
            temp = temp.next
            if temp.next == self.head:
                temp.next = hold
                hold.prev = temp
                Node.head = hold 
                break
    def delete(self):
        z = int(input())
        count = 1
        temp = self.head
        while True:
            current = temp
            temp = temp.next
            past = temp.next
            count+=1
            if z == count:
                current.next = past
                temp = None
                break
            elif z == 1:
                return Node().delatbeg()
            elif temp.next == None:
                return Node().delatend()
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

Node().delete()
Node().traverse()
