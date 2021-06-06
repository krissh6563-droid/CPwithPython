arr = [52,66,64,36,45,24,32]
n = len(arr)
max_element = arr.pop()
sum_arr = arr.pop()

for i in range(n-1,-1,-1):
    if arr[i]>max_element:
        sum_arr = sum_arr + arr[i]
        max_element= arr[i]
print(sum_arr)

for i in range(5,1):
    print(i)