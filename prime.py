class table():
    def __init__(self):
        self.c=2
        self.r=1
    def accept(self):
        self.n=int(input())
    def mul(self):
        while(self.c<self.n/2 and self.r!=0):
            self.r=self.n%self.c
            self.c+=1
        if(self.r!=0):
            print("PRIME")
        else:
            print("NOT A PRIME")
obj=table()
obj.accept()
obj.mul()
