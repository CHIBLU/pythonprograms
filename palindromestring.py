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
