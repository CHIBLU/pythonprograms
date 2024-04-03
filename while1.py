class demo:
    def __init__(self):
        self.c=1
        self.a=int(input("VALUE:"))
        self.sum=0
    def out(self):
        while(self.c<=self.a):
            self.sum=self.sum+self.c
            self.c=self.c+1
        print(self.sum)
obj=demo()
obj.out()
