"""
Code 1:
--------------------
"""
def List_sum(L1):
    total=0
    for i in L1:
        total+=i
    return total

L1=[int(x) for x in input("Please enter values seperated by space").strip().split()]
print(List_sum(L1))


"""
Code 2:
---------------------------------
"""

def max_pair(dictionary):
    K1=[x for x in dictionary.keys()]
    V1=[int(x) for x in dictionary.values()]
    value_position=V1.index(max(V1))
    print(K1[value_position],":",V1[value_position])

dictionary={'a':1 ,'b':2}
max_pair(dictionary)


"""
Code 3:
----------------------
"""


def maxlen(L1):
    L2=[]
    i=0
    while(i+1<len(L1)-1):
        count=0
        if L1[i]==0:
            count=0
            i+=1
            continue
        if L1[i]==1:
            count=1
            i+=1
            while(L1[i]==1 and i<len(L1)-1):
                if L1[i]==1:
                    count+=1
                i=i+1
            if i==len(L1)-1 and L1[i]==1:
                count+=1
            L2.append(count)
    return(max(L2))
print(maxlen([1,0,0,1,1,1,1,1,0,0,0,1,1,1,1,1]))

            
            
        

