Max=5
Tos=-1
def  push(list,item):
    global Max
    global Tos
    if(Tos==Max-1):
        print("Stack is full")
    else:
        Tos=Tos+1
        list.append(item)
        print(item," pushed")
def pop(list):
    global Tos
    if(Tos==-1):
        print("Stack is empty")
    else:
        Tos=Tos-1
        print("Last elemnt popped",list.pop())
def isEmpty(list):
    if list==[]:
         print("True")
    else:
        print("False")
def size(list):
    print("Size of list",len(list))
    return len(list)
def top(list):
    print(list[-1]) 
list=[]
while(True):
    print("1 PUSH")
    print("2 POP")
    print("3 isEMpty")
    print("4 Size")
    print("5 TOP OF STACK")
    print("6 for EXIT")
    choice=int(input("ENTER YOUR CHOICE"))
    if(choice==1):
        while True:
            print("ENTER THE ELEMENT '0' to QUIT")
            item=int(input(""))
            if item==0:
                break
            push(list,item)
    elif(choice==2):
        pop(list)
    elif(choice==3):
        isEmpty(list)
    elif(choice==4):
        size(list)
    elif(choice==5):
        top(list)
    else:
        break
    




