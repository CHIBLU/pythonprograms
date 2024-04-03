#count no of characters in a given string
'''
def count(s):
    cnt=[0]*26
    n=len(s)
    for i in range(n):
        cnt[ord(s[i])-97]+=1
    for i in range(26):
        if cnt[i]!=0:
            print(chr(i+97),cnt[i])
s=input()
count(s)
'''
#count no of characters in a given string without repeation
'''
def count(s):
    cnt=[0]*26
    n=len(s)
    for i in range(n):
        cnt[ord(s[i])-97]+=1
    for i in range(n):
        if cnt[ord(s[i])-97]!=0:
            print(s[i],"-->",cnt[ord(s[i])-97])
            cnt[ord(s[i])-97]=0
s=input()
count(s)
'''
#program to check given to strings are anagrams
'''
def anagram(s,u):
    c1=[0]*26
    c2=[0]*26
    l1=len(s)
    l2=len(u)
    for i in range(l1):
         c1[ord(s[i])-97]+=1
    for i in range(l2):
         c2[ord(u[i])-97]+=1
    if(c1==c2):
        print("ANAGRAM")
    else:
        print("NOT AN ANAGRAM")
s=input("String=")
u=input("String=")
anagram(s,u)
'''
#write a program to convert each character case
'''
def case(s):
    s1=""
    l=len(s)
    for i  in range(l):
        if(ord(s[i])>=97):
           s1=s1+chr(ord(s[i])-32)
        else:
            s1=s1+chr(ord(s[i])+32)
    print(s1)
s=input()
case(s)
'''
#write a program to convert each character case
'''
def case(s):
    s1=""
    l=len(s)
    for i  in range(l):
        s1=s1+chr(ord(s[i])^32)
    print(s1)
s=input()
case(s)
'''
#Palindrome
'''
def palindrome(s):
    left=0
    right=len(s)-1
    mid=len(s)//2
    for i in range(mid+1):
        if(s[left]==s[right]):
            left=left+1
            right=right-1
        else:
            print("NOT A PALINDROME")
            return
    print("PALINDROME")
s=input("STRING=")
palindrome(s)
'''
#Write a program to generate all substrings in a given string
'''
def substring(s):
    l=len(s)
    for i in range(l):
          s1=""
          for j in range(i,l):
              s1=s1+s[j]
              print(s1)
s=input("STRING=")
substring(s)
'''
#Program to find first non repeating character in a string
'''
def repeat(s):
    cnt=[0]*26
    n=len(s)
    for i in range(n):
        cnt[ord(s[i])-97]+=1
    for i in range(n):
        if cnt[ord(s[i])-97]==1:
            print(s[i])
            break
    for i in range(26):
        if cnt[i]==1:
            print(chr(i+97))
            break
s=input()
repeat(s)
'''
#Program to find first  repeating character in a string
'''
def repeat(s):
    cnt=[0]*26
    n=len(s)
    for i in range(n):
        cnt[ord(s[i])-97]+=1
    for i in range(n):
        if cnt[ord(s[i])-97]>1:
            print(s[i])
            break
    for i in range(26):
        if cnt[i]>1:
            print(chr(i+97))
            break
s=input()
repeat(s)
'''
#Largest Palindrome Substring
'''
def palindrome(s):
    left=0
    right=len(s)-1
    mid=(left+right)//2
    for i in range(mid+1):
        if s[left]==s[right]:
            left=left+1
            right=right-1
        else:
            #print("no")
            return False
    #print("yes")
    return True
def substr(s):
    l=[]
    n=len(s)
    for i in range(n):
        si=""
        for j in range(i,n):
            si=si+s[j]
            l.append(si)
    return l
s=input()
l=substr(s)
n=len(l)
maxlen=0
ans=''
for i in range(n):
    if palindrome(l[i])==True:
        length=len(l[i])
        if length>maxlen:
            maxlen=length
            ans=l[i]
print(ans,maxlen)
'''
##Largest Palindrome Substring
'''
def large(s):
    l=len(s)
    maxlen=1
    if(l<2):
        print(s,l)
    else:
        for i in range(l):
            left=i-1
            right=i+1
            while(left>=0 and s[left]==s[i]):
                left=left-1
            while right<l and s[right]==s[i]:
                right=right+1
            while(left>=0 and right<l and s[right]==s[left]):
                left=left-1
                right=right+1
            length=right-left-1
            if length>maxlen:
                maxlen=length
                index=left+1
        print(s[index:index+maxlen],maxlen)
s=input()
large(s)
'''           
#minimum substring in a given string
def enclose(s,p):
    sc=[0]*26
    pc=[0]*26
    pn=len(p)
    sn=len(s)
    start=0
    index=0
    minlen=sn+1
    count=0
    for i in range(pn):
        pc[ord((p[i]))-97]+=1
    for j in range(sn):
        sc[ord(s[j])-97]+=1
        if sc[ord(s[j])-97]<=pc[ord(s[j])-97]:
           count+=1
        if count==pn:
           while sc[ord(s[start])-97]>pc[ord(s[start])-97] or pc[ord(s[start])-97]==0:
               if sc[ord(s[start])-97]>pc[ord(s[start])-97]:
                   sc[ord(s[start])-97]-=1
               start=start+1
           length=j-start+1
           if length<minlen:
               minlen=length
               index=start
    print(s[start:start+minlen],minlen)
s='maqxbbcvyaxayzay'
p='aybxacy'
enclose(s,p)



           
                
                
        































  
