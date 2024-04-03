class fact():
    def __init__(self):
        self.c=1
        self.fact=1
    def accept(self):
        self.n=int(input())
        
    def facto(self):
        while(self.c<=self.n):
            self.fact=self.fact*self.c
            self.c=self.c+1
            print("FACTORIAL OF GIVEN NO",i,self.fact)
obj=fact()
obj.accept()
obj.facto()
        
