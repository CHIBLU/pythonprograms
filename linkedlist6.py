class Node:
    def _init_(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def _init_(self):
        self.head=None
    def create(self):
        while True:
            data=int(input("enter 0 to quit"))
            if data==0:
                break
            if self.head==None:
                self.head=Node(data)
                left=self.head
            else:
                right=Node(data)
                left.next=right
                left=right
    def displayodd(self):
        left=self.head
        count=1
        while(left!=None):
            if(count%2!=0):
                print(left.data,end='->')
            count+=1
            left=left.next
        print("None")
    def displayeven(self):
        left=self.head
        count=1
        while(left!=None):
            if(count%2==0):
                print(left.data,end="->")
            count+=1
            left=left.next
        print("None")
obj=LinkedList()
obj.create()
obj.displayodd()
obj.displayeven()
