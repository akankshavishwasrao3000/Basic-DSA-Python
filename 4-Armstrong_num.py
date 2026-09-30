n=int(input("Enter the number: "))
num=n
nop=len(str(n))
total=0

while n > 0:
    digit=n%10
    total=total+digit**nop
    n=n//10

if total == num:
    print("Yes")
else:
    print("No")    

