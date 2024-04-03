class opr():
    def __init__(self):
        pass
    def input(self):
        self.a=int(input())
        self.b=int(input())
    def process(self):
        while(self.a!=self.b):
            if(self.a>self.b):
                self.a=self.a-self.b
            else:
                self.b=self.b-self.a
        print(self.a)
obj=opr()
obj.input()
obj.process()
