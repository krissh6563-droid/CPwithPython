arr = list(map(int,input().split()))
n = int(input())
index = 0
for i in range(len(arr)):
    if arr[i]==n:
        index = i
        break
print(index)
    