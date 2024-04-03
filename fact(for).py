class fact():
    def __init__(self):
        self.c=1
        self.fact=1
    def accept(self):
        self.n=int(input())
    def facto(self):
        for i in range(1,self.n+1):
            self.fact=self.fact*i
            print("FACTORIAL OF GIVEN NO",i,self.fact)
obj=fact()
obj.accept()
obj.facto()
