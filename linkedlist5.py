class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def create(self):
        while True:
            data=int(input("enter the number 0 to quit:"))
            if data==0:
                break
            if self.head==None:
                self.head=Node(data)
                left=self.head
            else:
                right=Node(data)
                #establish link between left and right by assigning address of right to left.next
                left.next=right
                left=right
    def display(self):
        left=self.head
        print("elements of the linked list :")
        while left!=None:
            print(left.data,end='_>')
            left=left.next
        print('None')
    def insert(self):
        while True:
            print("1.insert as first node")
            print("2.insert as last node")
            print("3.insert any where except first and last")
            print("4.back to main menu")
            choice=int(input("enter your choice"))
            if choice==1: 
                data=int(input("enter a element to insert"))
                temp=Node(data)
                temp.next=self.head
                self.head=temp
                print("node inserted")
            elif choice==2:
                left=self.head
                while left.next!=None:
                    left=left.next
                data=int(input("enter the element to insert"))
                temp=Node(data)
                left.next=temp
                print("node inserted")
            elif choice==3:
                print("insert any where")
                left=self.head
                num=int(input("enter the number,after which you want to insert:"))
                while left.data!=num and left!=None:
                    left=left.next
                if left.data==num:
                    data=int(input("enter elemnet to insert:"))
                    temp=Node(data)
                    right=left.next
                    left.next=temp
                    temp.next=right
                    print("node inserted")
            else:
                return
    def delete(self):
       while True:
           print("1.delete first Node:")
           print("2.delete last Node:")
           print("3.delete any Node except 1st and last:")
           print("back to main menu:")
           choice=int(input("enter your choice:"))
           if choice==1:
               temp=self.head
               self.head=self.head.next
               print(temp.data,'is deleted')
           elif choice==2:
               right=self.head
               while right.next!=None:
                   left=right
                   right=right.next
               left.next=None
               del(right)
               print('last node deleted')
               self.display()
               left=self.head
               while left.next.next!=None:
                   left=left.next
               left.next=None
               print("node deleted")
           elif choice==3:
               serial=int(input("enter number to delete:"))
               right=self.head
               while right.data!=sno and right.next!=None:
                   left=right
                   right=right.next
               if right.data==serial:
                   left.next=right.next
                   del(right)
                   print(serial,"delete")
                   self.display()
               else:
                   print(serial,"not found")
                   self.display()
           elif choice==4:
               return
#main
obj=LinkedList()
while True:
    print('1.create')
    print('2.display')
    print('3.insert')
    print('4.delete')
    print('5.exit')
    choice=int(input('enter your choice :'))
    if choice==1:
        obj.create()
    elif choice==2:
        obj.display()
    elif choice==3:
        obj.insert()
    elif choice==4:
        obj.delete()
    else:
        break
