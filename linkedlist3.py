#even number sum and odd number sum seperately
class Node:
    def __init__(self,num):
        self.num=num
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def create(self):
        while True:
            num=int(input("enter a value:"))
            if num==0:
                break
            if self.head==None:
                self.head=Node(num)
                left=self.head
            else:
                right=Node(num)
                left.next=right
                left=right
    def display(self):
        left=self.head
        while(left!=None):
            print(left.num)
            left=left.next
    def add(self):
        n1=0
        n2=0
        left=self.head
        while(left!=None):
            if(left.num%2==0):
                n1=n1+left.num
            else:
                n2=n2+left.num
            left=left.next
        print("SUM OF EVEN",n1)
        print("SUM OF ODD",n2)
obj=LinkedList()
obj.create()
obj.display()
obj.add()
