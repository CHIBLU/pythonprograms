class revs:
    def __init__(self):
        self.rev=0
        self.temp=0
        
    def accept(self):
        self.n=int(input())
    def reverse(self):
        while(self.n>0):
            self.rev=self.n%10
            self.temp=self.temp*10+self.rev
            self.n=self.n//10
    def out(self):
        print(self.temp)
rev=revs()
rev.accept()
rev.reverse()
rev.out()
