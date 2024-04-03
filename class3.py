class area:
    def accept(self):
        self.b=int(input("value"))
        self.h=int(input("value"))
    def process(self):
        self.area=0.5*self.b*self.h
    def output(self):
        print("Area=",self.area)
obj=area()
obj.accept()
obj.process()
obj.output()
