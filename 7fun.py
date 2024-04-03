def display(a,b,c):
    if(a>b):
        if(a>c):
            print(a,"IS GREATEST")
        else:
            print(c,"IS GREATEST")
    else:
        if(b>c):
            print(b,"IS GREATEST")
        else:
            print(c,"IS GREATEST")
a=int(input(" "))
b=int(input(" "))
c=int(input(" "))
display(a,b,c)
