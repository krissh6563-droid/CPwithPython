#Two Pointer Approach: The idea is to solve this problem with constant space and 
#linear time is by using a two-pointer or two-variable approach where we simply 
# take two variables like left and right which hold the 0 and N-1 indexes. Just need to check that :
#
#Check If the left and right pointer elements are negative then simply increment the left pointer.
#Otherwise, if the left element is positive and the right element is negative then simply swap the elements, and simultaneously increment and decrement the left and right pointers.
#Else if the left element is positive and the right element is also positive then simply decrement the right pointer.
#Repeat the above 3 steps until the left pointer ? right pointer.

def segregateElements(self, arr, n):
    # Your code goes here
    l = 0
    r = n-1
    while l <= r:
        if arr[l] < 0 and arr[r] < 0:
            l = l+1
        elif arr[l] > 0 and arr[r] < 0:
            arr[l], arr[r] = arr[r], arr[l]
            l = l+1
            r = r-1
        elif arr[l] > 0 and arr[r] > 0:
            r = r-1
        else:
            l = l+1
            r = r-1

    return arr
