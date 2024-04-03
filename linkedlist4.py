#program to find biggest element and its postion
class Node:
    def __init__(self,pos,num):
        self.num=num
        self.pos=pos
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def create(self):
        while True:
            num=int(input("Enter a value"))
            if num==0:
                break
            pos=int(input("ENTER POSITION"))
            if self.head==None:
                self.head=Node(num,pos)
                left=self.head
            else:
                right=Node(num,pos)
                left.next=right
                left=right
    def display(self):
        left=self.head
        while(left!=None):
            print(left.pos," ",left.num)
            left=left.next
    def greatest(self):
        
        
obj=LinkedList()
obj.create()
obj.display()
obj.greatest()
