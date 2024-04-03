a=int(input("VALUE:"))
b=int(input("VALUE:"))
c=int(input("VALUE:"))
d=int(input("VALUE:"))

if(a>b):
    if(a>c):
        big=a
    else:
        big=c
else:
    if(b>c):
        big=b
    else:
        big=c
if(big<d):
    big=d
print(big,"IS BIGGEST")
