class list:
#constructor
    def __init__(self):
        self.l=[]
    def accept(self):
        self.n=int(input("Enter no of elements"))
    def data(self):
        i=0
        while(i<self.n):
            print("Enter ",i+1," Elements")
            z=int(input())
            self.l.append(z)
            i=i+1
    def display(self):
        print("Elements")
        i=0
        while(i<self.n):
            print(self.l[i],end=" ")
            i=i+1
#instantiate object to class list
obj=list()
obj.accept()
obj.data()
obj.display()
