"""Given an array and a number k, remove all occurrences of k from the array (in-place).
 Return the number of elements 'remainingSize' left after removing k. Note that removing
 the occurences is mandatory and will be checked in the main method.
 There can be anything beyond the first 'remainingSize' elements. It will be ignored."""

# List Comprehension

arr = [1, 3, 4, 6, 5, 1]
k = 1

res = [i for i in arr if i!=k]
print(res)
print(len(res))

# Two Pointer

j = 0
temp =[]
for i in range(len(arr)):
    if arr[i] != k:
        
        temp.append(arr[i])
        j+=1

print(j)
print(temp)

# Two pointer 
mylist = [1,2,3,1,2,1]
t = 1
j = 0
for i in range(len(mylist)):
    if mylist[i]!=t:
        mylist[j]= mylist[i]
        j = j+1
print(j)
del mylist[j:]
print(mylist)

# Using filter function


