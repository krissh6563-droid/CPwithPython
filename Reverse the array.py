#1) Initialize start and end indexes as start = 0, end = n-1 
#2) In a loop, swap arr[start] with arr[end] and change start and end as follows : 
#start = start +1, end = end – 1


arr = list(map(int,input().split()))
start = 0
end = len(arr)-1
while start<end:
    arr[start], arr[end] = arr[end], arr[start]
    start = start+1
    end = end-1
print(arr)