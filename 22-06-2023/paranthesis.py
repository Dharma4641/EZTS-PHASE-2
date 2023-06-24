s=list(input("enter the paranthesis combination:"))
print(s)
stack=[]
flag=0

def push(k):
    stack.append(k)
    
def pop(k):
    e=stack.pop()
    if (s[i],e)==(')','(') or  (s[i],e)==('}','{') or (s[i],e)==(']','['):
         if stack==[]:
             print("balanced")
        
    else:
        print("unbalanaced")
        flag=1
        
for i in range(len(s)):
    if s[i]=='(' or s[i]=='{' or s[i]=='[' :
        push(s[i])
    elif s[i]==')'or s[i]=='}' or s[i]==']' :
        if flag==1:
            break
        if stack!=[]:
            pop(s[i])
    else:
        print("enter valid:")
        
    
