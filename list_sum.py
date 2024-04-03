class sum_list:
    def __init__(self):
        self.l=[]
    def accept(self):
        self.n=int(input("en  ter elements"))
    def data(self):
        i=0
        while(i<self.n):
            print("ELEMENT",i+1,":")
            z=int(input())
            self.l.append(z)
            i=i+1
    def display(self):
        sum=0
        i=0
        while(i<self.n):
            sum=sum+self.l[i]
            i=i+1
        print("SUM=",sum)
obj=sum_list()
obj.accept()
obj.data()
obj.display()
        
