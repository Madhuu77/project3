stack=[]
n=int(input("limit of stack:"))
def push():
    if len(stack)==n:
        print("stack is full")
    else:
         element=int(input("enter element to push to stack:"))
         stack.append(element)
         print(stack)
    
def pop():
        if len(stack)==0:
            print("stack is empty")
        else:
            e=stack.pop()
            print("removed element form stack is:",e)
            print(stack)
def isEmpty():
    if stack!=[]:
        print(False)
    elif stack==[]:
        print(True)
    else:
        return

while True:
    print("select the operation 1.push 2.pop 3.isEmpty 4.exit.")
    choice=int(input())
    if choice==1:
        push()
    elif choice==2:
        pop()
    elif choice==3:
        isEmpty()
    elif choice==4:
        break
    else:
        print("enter the correct operation")
 
