'''
#It is not optimal solution
n=[5,3,2,2,1,5,5,7,5,10]
m=[10,111,1,9,5,67,2]

for i in m:
    
    count=0
    for x in n:
        if x==i:
            count+=1
            
    print(i, "=",count) 

'''

'''
#it is optimal solution...using hashing

n=[5,3,2,2,1,5,5,7,5,10]
m=[10,111,1,9,5,67,2]

hash_list=[0]*11

for i in n:
    hash_list[i]+=1

for i in m:
    if i<1 or i>10:
        print(f"{i}= 0")
    else:
        print(f"{i} = {hash_list[i]}")    

'''

'''
# using Dictionary

n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2]

freq={}

for i in n:
    if i in freq:
        freq[i]+=1

    else:
        freq[i]=1  
        
for i in m:
    if i in freq:
        print(f"{i} = {freq[i]}")
    else:
        print(f"{i} = 0")          
'''

'''
# Character Hashing

s="azyxyyzaaa"
q=["a","d","y","x"]


hash_list=[0]*26

for ch in s:
    ascii_val=ord(ch)
    index=ascii_val-97
    hash_list[index]+=1

for ch in q:
    ascii_val=ord(ch)
    index=ascii_val-97
    print(hash_list[index])
'''


'''
# character using dictionary

s="azyxyyzaaa"
q=["a","d","y","x"]

fre={}

for ch in s:
    ascii_val=ord(ch)
    index=ascii_val-97
    if index in fre:
        fre[index]+=1
    else:
        fre[index]=1  


for ch in q:
    ascii_val= ord(ch)
    index=ascii_val-97

    if index in fre:
        print(f"{ch} = {fre[index]}")
    else:
        print(f"{ch} = {0}")        
'''

'''
s="ayzYZxYYzaZayaJAJOPZy"
q=["a","d","Y","y","x","A","J","Z","P","O"]

fre={}

for ch in s:
    ascii_val=ord(ch)
    index=ascii_val-127
    if index in fre:
        fre[index]+=1
    else:
        fre[index]=1  


for ch in q:
    ascii_val= ord(ch)
    index=ascii_val-127

    if index in fre:
        print(f"{ch} = {fre[index]}")
    else:
        print(f"{ch} = {0}")  

#-----------or------------ 

s = "ayzYZxYYzaZayaJAJOPZy"
q = ["a","d","Y","y","x","A","J","Z","P","O"]

fre = {}

for ch in s:
    if ch in fre:
        fre[ch] += 1
    else:
        fre[ch] = 1

for ch in q:
    if ch in fre:
        print(f"{ch} = {fre[ch]}")
    else:
        print(f"{ch} = 0")


'''

           