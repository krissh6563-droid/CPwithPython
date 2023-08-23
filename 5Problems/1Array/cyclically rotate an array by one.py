#Assign every element with its previous element and first element with the last element .

def rotate( arr, n):
    last = arr[n-1]
    for i in range(n-1,0,-1):
        arr[i] = arr[i-1]
    arr[0] = last
    return arr