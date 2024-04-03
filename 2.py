a=int(input("VALUE"))
b=int(input("VALUE"))
c=int(input("VALUE"))
d=int(input("VALUE"))
e=int(input("VALUE"))
if(a>b):
    if(a>c):
       if(a>d):
           if(a>e):
                print("A IS GREATEST")
           else:
                 print("E IS GREATEST")
       else:
           if(d>e):
                print("D IS GREATEST")
           else:
                print("E IS GREATEST")
    else:
        if(c>d):
            if(c>e):
                 print("C IS GREATEST")
            else:
                 print("E IS GREATEST")
        else:
             if(d>e):
                  print("D IS GREATEST")
             else:
                  print("E IS GREATEST")
else:
    if(b>c):
        if(b>d):
            if(b>e):
                 print("B IS GREATEST")
            else:
                 print("E IS GREATEST")
        else:
            if(d>e):
                 print("D IS GREATEST")
            else:
                 print("E IS GREATEST")
    else:
        if(c>d):
             if(c>e):
                 print("C IS GREATEST")
             else:
                 print("E IS GREATEST")
        else:
             if(d>e):
                  print("D IS GREATEST")
             else:
                  print("E IS GREATEST")
