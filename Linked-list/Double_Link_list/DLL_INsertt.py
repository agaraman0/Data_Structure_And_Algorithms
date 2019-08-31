#linked list
class Node:
    def __init__(self,data={}):
        self.data = data
        self.next = None
        self.prev = None
    def traverse(self):
        temp = self.head
        count = 0
        while temp != None:
            print(temp.__dict__)
            temp = temp.next
            count +=1
        print(count)
    def insertatbeg(self):
        x = input()
        zero = Node(x)
        zero.prev = None
        zero.next = self.head
        Node.head = zero
    def insertatend(self):
        y = input()
        last = Node(y)
        temp = self.head
        while True:
            temp = temp.next
            if temp.next == None:
                last.next = None
                last.prev = temp
                temp.next = last
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
                    return Node().insertatend()
                else:
                    w = input()
                    new = Node(w)
                    current.next = new
                    new.next = temp
                    new.prev = temp.prev
                    temp.prev = new
                    break
            elif z == 1:
                return Node().insertatbeg()
            
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
fourth.next = None


if __name__== "__main__":
    Node().insert()
    Node().traverse()
