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
            

