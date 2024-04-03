class armstrong():
    def __init__(self):
        self.c=0
        self.sum=0
    def accept(self):
        self.n=int(input())
        self.w=self.n
        self.g=self.n
    def dig(self):
        while(self.n>0):
            self.c=self.c+1
            self.n=self.n//10
        
    def armstrong(self):
        while(self.w>0):
            r=self.w%10
            self.sum=self.sum+(r**self.c)
            self.w=self.w//10
        
    def out(self):
        if(self.g==self.sum):
            print("ARMSTRONG")
        else:
            print("NOT AN ARMStroNG")
        
obj=armstrong()
obj.accept()
obj.dig()
obj.armstrong()
obj.out()
