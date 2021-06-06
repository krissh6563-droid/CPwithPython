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

def row_wise(m):
    for i in range(len(m)):
        temp = m[i]
        x = quick_sort(temp)
        m[i] = x
    return m

m = [[9, 8, 7, 1 ],[7, 3, 0, 2],[9, 5, 3, 2],[ 6, 3, 1, 2 ]]

y = row_wise(m)
print(y)
