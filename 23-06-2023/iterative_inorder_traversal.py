class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def inorder(root):
    current=root
    stack=[]
    done=0
    while True:
        if current is not None:
            stack.append(current)
            current=current.left
        elif (stack):
            current=stack.pop()
            print(current.data,end=" ")
            current=current.right
        else:
            break
    print()
root=Node(int(input("enter root node:")))
root.left=Node(int(input("enter root.left node:")))
root.right=Node(int(input("enter root.right node:")))
root.left.left=Node(int(input("enter root.left.left node:")))
root.left.right=Node(int(input("enter root.left.right node:")))

inorder(root)
