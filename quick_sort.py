# array declaration

arr = list(map(int, input().split()))


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
sorted_arr = quick_sort(arr)
print(sorted_arr)
