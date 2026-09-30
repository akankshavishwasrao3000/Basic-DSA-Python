# So should you always use a dictionary?
# For learning and solving general Python DSA questions: Yes, dictionary is a very useful default.


'''
# Pattern 1 — Frequency Counting
n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2]


fre={}
for i in n:
    if i in fre:
        fre[i]+=1
    else:
        fre[i]=1

for i in m:
    if i in fre:
        print(f"{i} = {fre[i]}")

    else:
        print(f"{i} = 0")  
'''

'''
# Pattern 2 : using the frequency dictionary pattern to solve a duplicate problem.
n = [1, 2, 5, 4, 6, 5]

fre={}

for i in n:
    if i in fre:
        fre[i]+=1
        print(f"First Duplicate Num is: {i}")
        break
    else:
        fre[i]=1
'''
'''

//Using hashing
n = [1, 2, 1,4, 6, 5]

# count=1
# for i in n:
#    count+=1

# hash_list=[0]*(count+1)

lent=len(n)

   
hash_list=[0]*lent

for i in n:
    hash_list[i]+=1

    if hash_list[i]==2:
        print(f"first duplicate : {i}")
        break    
  '''

# 3️⃣ First/Last occurrence

arr = [5, 3, 2, 5, 3, 7]

fre={}
left=0
righ=0

for i in arr:
    if i in fre:
        left=i
        print(left)
    else:
        righ=i





