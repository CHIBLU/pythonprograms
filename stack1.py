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
        return True
    else:
        return False
def size(list):
    print("Size of list",len(list))
    return len(list)
def top(list):
    return list[-1]
list=[]
push(list,10)
push(list,20)
push(list,30)
push(list,40)
push(list,50)
push(list,60)
pop(list)
pop(list)
pop(list)
pop(list)
pop(list)
pop(list)




