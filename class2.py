class Sum:#declaration of class
    def accept_data(self):
        self.a=int(input("Enter a value"))
        self.b=int(input("Enter a value"))
    def process(self):
        self.c=self.a+self.b
    def output(self):
        print(f'{self.a}+{self.b}={self.c}')
#instartiating the object
obj=Sum()
obj.accept_data()
obj.process()
obj.output()
