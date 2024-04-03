class stack_demo():
    def __init__(self):
        self.stack=[]
        self.max=5
        self.tos=-1
    def push(self,item):
        if(self.tos==self.max-1):
            print("Stack is full")
            return
        else:
            self.stack.append(item)
            self.tos+=1
    def pop(self):
        if (self.tos==-1):
            print("Satck is empty")
            return
        else:
             print("The element popped is",self.stack.pop())
            self.tos-=1
    def isEmpty(self):
        if(self.stack==[]):
            print("Stack is empty")
            return True
        else:
            print("Stack is not Empty")
            return False
    def size(self):
        print(len(self.stack))
    def peek(self):
        print(self.stack.pop(0))
    def display(self):
        n=len(self.stack)-1
        while(n>=0):
            print(self.stack[n],end=" ")
            n=n-1

s=stack_demo()
while(True):
    print("1.Push\n 2.Pop\n 3.isEmpty\n 4.Size\n 5.Peek\n 6.Display \n 7.Exit")
    choice=int(input("Enter your Choice"))
    if(choice==1):
        while(True):
            item=int(input("Enter the element"))
            print("0 to quit")
            if(item==0):
                break
            else:
                s.push(item)
    
    elif(choice==2):
        s.pop()
    elif(choice==3):
        s.isEmpty()
    elif(choice==4):
        s.size()
    elif(choice==5):
        s.peek()
    elif(choice==6):
        s.display()
    else:
        print("Invalid Choice")
    
        
            
    
            
        
        
        
