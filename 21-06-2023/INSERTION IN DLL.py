#INSERTION IN DLL
class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None
class dll:
    def __init__(self):
        self.head=None
    def insert_start(self):
         n=Node(300)
         temp=self.head
         temp.prev=n
         n.next=temp
         self.head=n
    def insert_end(self):
         n=Node(300)
         temp=self.head
         while temp.next is not None:
              temp=temp.next
         temp.next=n
         n.prev=temp
    def insert_pos(self,pos):
        n=Node(44)
        temp=self.head
        for i in range(1,pos-1):
            temp=temp.next
        n.prev=temp
        n.next=temp.next
        temp.next.prev=n
        temp.next=n
    def display(self):
        if self.head is None:
            print("empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"<-->",end=" ")
                temp=temp.next
l=dll()
n1=Node(100)
l.head=n1
n2=Node(200)
n2.prev=n1
n1.next=n2
n3=Node(300)
n3.prev=n2
n2.next=n3
n4=Node(400)
n4.prev=n3
n3.next=n4
l.display()
print("-----------")
l.insert_start()
l.display()
print("-----------")
l.insert_end()
l.display()
print("-----------")
l.insert_pos(3)
l.display()