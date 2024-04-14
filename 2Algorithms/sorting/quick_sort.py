def quick_sort(arr):
    n = len(arr)
    if n<=1:
        return arr
    else:
        pivot = arr.pop()
    smaller_element = []
    grater_element = []
    for item in arr:
        if item>pivot:
            grater_element.append(item)
        else:
            smaller_element.append(item)

    return quick_sort(smaller_element)+[pivot]+quick_sort(grater_element)
if __name__ == "__main__":
    arr = list(map(int,input().split()))
    sorted_arr = quick_sort(arr)
    print(sorted_arr)