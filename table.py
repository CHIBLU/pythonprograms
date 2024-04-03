class table():
    def __init__(self):
        self.i=1
    def accept(self):
        self.n=int(input())
    def mul(self):
        for i in range(1,11):
            print(self.n,"*",i,"=",self.n*i)
obj=table()
obj.accept()
obj.mul()
