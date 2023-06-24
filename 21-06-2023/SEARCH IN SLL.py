#search in SLL
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
        self.last_node=None
    def append(self,data):
        if self.last_node is None:
            self.head=Node(data)
            self.last_node=self.head
        else:
            self.last_node.next=Node(data)
            self.last_node=self.last_node.next
    def display(self):
        current=self.head
        while current is not None:
            print(current.data,"-->",end=' ')
            current=current.next
    def search(self,s):
        temp=self.head
        while temp:
            if temp.data==s:
                flag=1
                break
            temp=temp.next
        if flag==1:
            print("present")
        else:
            print("not present")        

al_llist=Linkedlist()
n=int(input('How Many elements would you like to enter'))
for i in range(n):
    data=int(input("Enter data item;"))
    al_llist.append(data)
    
print("the linked list:",end=' ')
al_llist.display()
print(end="\n")
s=int(input("enter num to search:"))
al_llist.search(s)
