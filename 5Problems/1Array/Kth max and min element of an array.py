# User function Template for python3
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr.pop()

    item_greater = []
    item_smaller = []

    for item in arr:
        if item > pivot:
            item_greater.append(item)
        else:
            item_smaller.append(item)
    return quick_sort(item_smaller) + [pivot] + quick_sort(item_greater)


def kthSmallest(arr, l, r, k):
    '''
    arr : given array
    l : starting index of the array i.e 0
    r : ending index of the array i.e size-1
    k : find kth smallest element and return using this function

    '''
    sorted_array = quick_sort(arr)
    return sorted_array[k-1]


#  Driver Code Starts
# Initial Template for Python 3

# contributed by RavinderSinghPB
if __name__ == '__main__':
    import random
    t = int(input())
    for tcs in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        k = int(input())
        print(kthSmallest(arr, 0, n-1, k))
