def accept():
    n=int(input("Enter no of elements"))
    return n
def data(l,n):
    i=0
    while(i<n):
        print("Enter ",i+1," Elements")
        z=int(input())
        l.append(z)
        i=i+1
def disply(l,n):
    print("Elements of list")
    i=0
    while(i<n):
        print(l[i],end=" ")
        i=i+1
l=[]
n=accept()
data(l,n)
disply(l,n)
    
