#program to find the length of string
'''
str=input("Enter the the string=")
print(str)
print(len(str))
'''
#program to find the length of string without built in
'''
str=input("Enter the string=")
c=0
print(str)
for i in str:
    c=c+1
print("length=",c)
'''
#program to count no of words in the given string
'''
str=input("Enter the string=")
c=1
for i in str:
    if(i==" "):
        c=c+1
print(c)
'''
#program to count no of vowels in a given string
'''
str=input("enter a string=")
c=0
for i in str:
    if(i=="a" or i=="e" or i=="i" or i=="o" or i=="u"):
        c=c+1
5print(c)
'''
#program to count no of vowels in a given string using functions
'''
def vowels(str):
    c=0
    for i in str:
        if(i=="a" or i=="e" or i=="i" or i=="o" or i=="u"):
            c=c+1
    return(c)
str=input("String=")
result=vowels(str)
print(result)
'''
#program to count no of vowels in a given string using functions
'''
def vowels(str):
    c=0
    l="aeiou"
    for i in str:
        if i in l:
            c=c+1
    return(c)
str=input("String=")
result=vowels(str)
print(result)
'''
#program to count no of vowels in a given string using functions
'''
def vowels(str):
    c=0
    l=['a','e','i','o','u']
    for i in str:
        if i in l:
            c=c+1
    return(c)
str=input("String=")
result=vowels(str)
print(result)
'''
#program to find no of vowels and its specifications
'''
def vowels(str):
    x=u=v=w=y=0
    l="aeiou"
    for i in str:
            if i=='a':
                x=x+1
            elif i=='e':
                 u=u+1
            elif i=='i':
                v=v+1
            elif i=='o':
                w=w+1
            elif i=='u':
                y=y+1
    return(x,u,v,w,y)
str=input("String=")
x,u,v,w,y=vowels(str)
print("a:",x)
print("e:",u)
print("i:",v)
print("o:",w)
print("u:",y)
'''
#program to reverse a string
'''
def reverse(sr):
  z=len(sr)
  z=z-1
  rev=""
  while(z>=0):
      rev=rev+sr[z]
      z=z-1
  return(rev)
sr=input("string=")
res=reverse(sr)
print(res)
'''
#reverse
'''
def reverse(sr):
  rev=""
  for ch in sr:
      rev=ch+rev
  return(rev)
sr=input("string=")
res=reverse(sr)
print(res)
'''
#program to check given string is palindrome or not
'''
def palindrome(sr):
    rev=""
    z=sr
    for ch in sr:
        rev=ch+rev
    return rev
sr=input("string=")
res=palindrome(sr)
if sr==res:
    print("PALINDROME")
else:
    print("Not a palindrome")
'''
#program to display all lowercase charachters
'''
print("ALL LOWER CASE CHARACTERS")
for i in range(97,123):
    print(chr(i),end=" ")
'''

#program to display unicode
'''
ch=input("CHARACTER=")
print(ord(ch))
'''
#program to display unicode
'''
ch=int(input("CHARACTER="))
print(chr(ch))
'''
#program to accept list of integers values and display characters
'''
l=[112,65,69,78,120]
for i in l:
    print(chr(i))
'''
#program to count lower case characters
'''
def lower(s):
    c=0
    for ch in s:
        if ord(ch)>=97 and ord(ch)<=122:
            c=c+1
    return c
s=input("STRING=")
res=lower(s)
print(res)
'''
#lowercase without any built in
'''
def lower(s):
    c=0
    for ch in s:
        if ch>='a' or ch<='z':
            c=c+1
    return c
print(lower("How are yoy"))
'''
#with builtin
'''
def lower(s):
    c=0
    for ch in s:
        if ch.islower():
            c=c+1
    return c
print(lower("How are yoy"))
'''
#given character digit or not
'''
def isdigit(s):
    for ch in s:
        if ch>='0' and ch<='9':
            print(ch,"is digit")
        else:
            print(ch,"is not a digit")
print(isDigit("hellovardhaman123456789"))
'''
#no of digits
'''
def digitcount(s):
    c=0
    for i in s:
        if i>'0' and and i<='9':
            c=c+1
    return c
s=input("String")
result=digitcount(s)
print(result)
'''
#program to delete vowels from the given string
'''
def remove(s):
    vowels='aeiouAEIOU'
    result=''
    for ch in s:
        if ch  not in vowels:
            result=result+ch
    return result
s=input("String")
cc=remove(s)
print(cc)
'''
#count and delete vowels
'''
def remove(s):
    vowels='aeiouAEIOU'
    result=''
    c=""
    for ch in s:
        if ch  not in vowels:
            result=result+ch
        if ch in vowels:
            c=c+ch
    return result,c
s=input("String")
cc,rr=remove(s)
print("without vowels",cc)
print("removed vowels",rr)
'''
#program to check given characet is vowel or not
'''
def vowelss(str):
    vowels="aeiouAEIOU"
    if ch.isalpha():
        if ch in vowels:
            print(ch,"is vowel")
        else:
            print(ch,"is constant")
    else:
        print("it is not alphabet")
ch=input("enter character")
vowel(str)
'''
#program to find vowels digits consonants and special characters
'''
def check(str):
    vowels="aeiouAEIOU"
    if ch.isalpha():
        if ch in vowels:
            print(ch,"is vowel")
        else:
            print(ch,"is constant")
    elif ch>='0' and ch<='9':
        print(ch,"is digit")
    else:
        print(ch,"is special character")
ch=input("enter character")
check(str)
'''
#program to find vowels digits consonants and special characters
'''
def checkall(s):
    vowels='aeiouAEIOU'
    v1=0
    c1=0
    d1=0
    sp1=0
    for ch in s:
      if ch.isalpha():
         if ch in vowels:
            v1+=1
         else:
            c1+=1
      elif ch>='0' and ch<='9':
          d1+=1
      else:
          sp1+=1
    return v1,c1,d1,sp1
s=input("enter:")
v1,c1,d1,sp1=checkall(s)
print("vowels:",v1)
print("consonants:",c1)
print("special:",sp1)
print("digits:",d1)
'''
#username to be valid only if characters and digits else invalid
#program to read username contains and numericals is allowed or else invalid
'''isalnum()=this function check weather the string contqins only letterrs or numbers or both 
def user(s)
    if s.isalnum():
            print("Valid")
        else:
            print("Invalid")
s=input("Enter a string:")
user(s)
'''
#program to read username contains and numericals is allowed or else invalid without is allnum

#program to read username and check for
'''
def user(i):
    found=True
    for s in i:
        if  s>='0'and s<='9' or s>='a' and s<='z':
                continue
        else:
                found=False
                break
    if found==True:
            print("Valid")
    else:
            print("Invalid")
i=input("Enter a string:")
user(i)
'''
#program to find missing number
'''
l=[1,2,3,5,6,7,8,9]
n=len(l)+1
sum1=n*(n+1)/2
sum2=0
for i in l:
    sum2=sum2+i
missing=sum1-sum2
print("missing number",missing)
'''
#program to delete duplicate elemnets
l=[1,2,3,4,5,6,7,8,9,1,1,1,1,2,2,2,3,4]
result=[]
c=0
for num in l:
    if num not in result:
        result.append(num)
    else:
        c=c+1
print(result)
print(c)
