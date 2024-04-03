class sqrnum:
    def __init__(self):
        self.sum=0
    def accept(self):
        self.n=int(input())
    def sqr(self):
        while(self.n>0):
            r=self.n%10
            self.sum=self.sum+(r*r)
            self.n=self.n//10
    def output(self):
        print(self.sum)
obj=sqrnum()
obj.accept()
obj.sqr()
obj.output()
