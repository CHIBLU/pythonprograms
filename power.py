class power():
    def __init__(self):
        self.res=1
        self.c=1
    def accept(self):
        self.b=int(input("Enter a number:"))
        self.p=int(input("Enter power number:"))
    def process(self):
        while self.c<=self.p:
            self.res=self.res*self.b
            self.c=self.c+1
    def output(self):
        print(self.res)
d=power()
d.accept()
d.process()
d.output()
