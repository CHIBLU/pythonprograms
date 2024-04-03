def  push(list,item):
    list.append(item)
    print(item," pushed")
def pop(list):
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
pop(list)
pop(list)
isEmpty(list)

print("list is Empty:",isEmpty(list))
size(list)
top(list)
print("Top of list:",top(list))



