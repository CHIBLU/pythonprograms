#declaration of list
l=[]
#accept no of elements
n=int(input("No of elements"))
i=0
while(i<n):
    print("ENTER ",i+1," ELEMENTS")
    z=int(input())
    l.append(z)
    i=i+1
print("ELEMENTS OF LIST:")
i=0
while(i<n):
    print(l[i],end=" ")
    i=i+1
