class demo:
    def __init__(self):
        self.c=1
        self.a=int(input("VALUE:"))
    def process(self):
        while(self.c<=self.a):
            print("Vande mataram",self.c)
            self.c=self.c+1
obj=demo()
obj.process()

          
