class sum_list:
    def __init__(self):
        self.l=[]
    def accept(self):
        self.n=int(input("enter elements"))
    def data(self):
        i=0
        while(i<self.n):
            print("ELEMENT",i+1,":")
            z=int(input())
            self.l.append(z)
            i=i+1
    def big(self):
        big=self.l[ 0]
        i=1
        while(i<self.n):
            if(big<self.l[i]):
                big=self.l[i]
            i=i+1
        print("BIGGEST",big)
obj=sum_list()
obj.accept()
obj.data()
obj.big()
        
