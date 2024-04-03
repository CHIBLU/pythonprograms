class Node:
    def __init__(self,sno):
        self.sno=sno
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def create(self):
        sum=0
        while True:
            sno=int(input("ENTER SNO 0 to break"))
            if sno==0:
                break
            
            if self.head==None:
                self.head=Node(sno)
                left=self.head
            else:
                right=Node(sno)
                left.next=right
                left=right
    def display(self):
        left=self.head
        while(left!=None):
            left=left.next
    def add(self):
        sum=0
        left=self.head
        while(left!=None):
            sum=sum+left.sno
            left=left.next
        print("SUM OF NODES",sum)
        
obj=LinkedList()
obj.create()
obj.display()
obj.add()
