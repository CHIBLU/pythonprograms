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
                self.left.next=right
                self.left=right
        return(self.head)
    def display(self):
        left=head
        while left!=None:
            print(left.data.end=" ")
            left=left.next
        print("NONE")
obj=LinkedList()
head1=ob.create()
head2=ob.create()
head3=ob.create()
ob.displ
