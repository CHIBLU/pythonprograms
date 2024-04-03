n=int(input("enter marks1"))
x=int(input("enter marks2"))
z=int(input("enter marks3"))
w=(n+x+z)/3
if(n>=40 and x>=40 and z>=40):
    if w>=90:
        print("O")
    elif(w>=80 and w<90):
        print("A+")
    elif(w>=70 and w<80):
        print("A")
    elif(w>=60 and w<70):
        print("B+")
    elif(w>=50 and w<60):
        print("B")
    elif(w>=40 and w<50):
        print("C")
else:
    print("fail")
