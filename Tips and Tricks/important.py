#take multiple inputs in one line separated by space
arr = list(map(int,input().split()))

#take two input in the same line
a, b  = input().split()
a = int(a)
b = int(b)
print(a,b)

#ASCII value
a = 97
b = 98

A = 65
B = 66

#how to print ASCII value
print(ord('a'))

#how to print character from ASCII
print(chr(97))

#reversing list and string in python 
str = "Krishan"
arr = [1,2,3,4]
print(str[::-1])
print(arr[::-1])

#find max and min value 
print(max(2,3))  # --->3
print(min(2,3))  # --->2

arr = [2,3,1,5,6,7]
print(max(arr))
print(min(arr))

#Permutation and combination
# nPr = (n!) / (n-r)!
# nCr = (n!) / r!(n-r)!

#Convert decimal to binary
x = 2
print(bin(x).replace("0b",""))

#Convert binary to decimal
x = '10'
print(int(x,2))