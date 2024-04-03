class pal:
        def __init__(self):
            self.rev=0
        def accept(self):
            self.n=int(input())
            self.temp=self.n
        def reverse(self):
            while(self.n>0):
                r=self.n%10
                self.rev=self.rev*10+r
                self.n=self.n//10
        def palindrome(self):
            if(self.rev==self.temp):
                print("PALINDROME")
            else:
                print("Not a palindrome")
obj=pal()
obj.accept()
obj.reverse()
obj.palindrome()
