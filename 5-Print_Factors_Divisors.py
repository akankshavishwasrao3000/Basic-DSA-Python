'''
n=int(input("Enter the Number: "))
num=[]

if n==0 :
    print(0)
if n <0:
    print("NOT Allow Negative")    
    
for i in range(1,n+1):
    if n%i==0:
        num.append(i)  

print(num)

'''

n=int(input("Enter the Number: "))
num=[]

if n <=0:
    print("NOT Allow Negative")    
    
for i in range(1,(n//2)+1):
    if n%i==0:
        num.append(i) 

num.append(n)
print(num) 




