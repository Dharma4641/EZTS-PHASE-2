stack=[]
eve=[]
odd=[]
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
        c=int(input("enter choice 1.even or 2.odd"))
        for i in range(len(stack)):
              if stack[i]%2 == 0:
                    eve.append(stack[i])
              else:
                  odd.append(stack[i])
                  
        if c==1:
            for i in range(len(eve)):
                  print(eve[i])
            
        elif c==2:
            for i in range(len(odd)):
              print(odd[i])
    
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

























