#deletion SLL
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class Linkedlist:
    def __init__(self):
        self.head=None
    
    def insert_position(self,pos,data):
        np=Node(data)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        np.next=temp.next
        temp.next=np
        
    def delete_first(self):
         temp=self.head
         self.head=temp.next
         temp.next=None

    #deleting last node
    def delete_last(self):
         temp=self.head.next
         prev=self.head
         while temp.next is not None:
             temp=temp.next
             prev=prev.next
             prev.next=None#last but before node's next we make as none

    #deleting node in between
    def delete_position(self,pos): 
        temp=self.head.next
        prev=self.head
        for i in range(1,pos-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next
        temp.next=None
        
    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp=self.head
        while temp.data!=None:
            print(temp.data,"-->",end=" ")
        
delete_list=Linkedlist()
delete_list.head=Node(10)
delete_list.head=Node(20)
delete_list.head=Node(30)
delete_list.head=Node(40)
delete_list.head=Node(50)
delete_list.display()
delete_list.delete_first()
