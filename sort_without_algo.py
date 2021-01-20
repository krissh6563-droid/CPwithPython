#User function Template for python3
#but is not in-place algorithm

def sort012(arr,n):
    # code here
    zero_arr = []
    one_arr = []
    two_arr = []
    for item in arr:
        if item==0:
            zero_arr.append(item)
        elif item==1:
            one_arr.append(item)
        else:
            two_arr.append(item)

    return zero_arr + one_arr + two_arr
            





#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        x = sort012(arr,n)
        for i in x:
            print(i, end=' ')
        
