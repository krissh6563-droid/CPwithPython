# Given a sorted array, check if there exist two numbers whose sum is zero.

def has_zero_sum_pair(arr):
    left = 0
    right = len(arr) - 1  
    while left < right:
        sum = arr[left] + arr[right]
        if sum == 0:
            return True
        elif sum > 0:
            right -= 1
        else:
            left += 1 
    return False

# Example usage:
arr = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
print(has_zero_sum_pair(arr))  

    