#declare array 
arr = list(map(int,input().split()))
max = arr[0]
min = arr[0]

#function to get max value 
for i in range(len(arr)):
    if arr[i]>max:
        max = arr[i]
    else:
        max = max
print(max)

for j in range(len(arr)):
    if arr[i]>min:
        min = min
    else:
        min = arr[i]

print(min)
    
    