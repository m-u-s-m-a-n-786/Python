s="maham"
n=len(s)
x=0
for i in range(0,n):
    if s[i] != s[n-i-1]:
        x=1
        break

if x==0:
    print("palindrome")
else:
    print("not a palindrome")