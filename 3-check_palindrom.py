n=int(input("Enter the Number: "))
num=n
rev=0

while n>0:
    digit=n%10
    rev=rev*10+digit
    n=n//10

if rev==num:
    print("YES")
else:
    print("NO")        
