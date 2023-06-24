stack=[]

def push():
    element=int(input("enter element:"))
    stack.append(element)
    print(stack)
    
def pop():
    if not stack:
        print("stack is empty")
    else:
        e=stack.pop()
        print("removed element is:",e)
        print(stack)
        
def display():
    if not stack:
        print("stack is empty")
    else:
        print(stack)
    
def peek():
    if not stack:
        print("stack is empty")
    else:
        print(stack[-1])
    
while True:
    choice=int(input("enter choice 1:push 2:pop 3:display 4:peek 5:exit"))
    if choice== 1:
        push()
    elif choice==2:
        pop()
    elif choice==3:
        display()
    elif choice==4:
        peek()
    elif choice==5:
        exit()
    else:
        print("enter valid choice")
        
        
