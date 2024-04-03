class Node:
    def __init__(self,id,name,total):
        self.id=id
        self.name=name
        self.total=total
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def create(self):
        while True:
            id=int(input("ENTER ID 0 to quit"))
            if id==0:
                break
            name=input("ENTER NAME")
            total=int(input("ENTER TOTAL"))
            if self.head==None:
                self.head=Node(id,name,total)
                left=self.head
            else:
                right=Node(id,name,total)
                left.next=right
                left=right
    def display(self):
        left=self.head
        print("THE ELEMENTS OF LINKED LIST")
        while(left!=None):
            print(left.id," ",left.name," ",left.total,end="->")
            left=left.next
obj=LinkedList()
obj.create()
obj.display()

