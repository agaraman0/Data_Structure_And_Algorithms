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
    def delatbeg(self):
        temp = self.head
        Node.head = temp.next
        temp = None
    def delatend(self):
        temp = self.head
        while True:
            current = temp
            temp = temp.next
            if temp.next == None:
                current.next = None
                temp = None
                break
    def delete(self):
        z = input()
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
            elif z == 1:
                return Node().delatbeg()
            elif temp.next == None:
                return Node().delatend()
            
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
    
    Node().traverse()
    Node().delatend()
    Node().traverse()
