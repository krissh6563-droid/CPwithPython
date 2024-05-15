def most_frequent(lst):
    # Initialize a dictionary to store the count of each number
    count_dict = {}

    # Iterate through the list and count occurrences of each number
    for num in lst:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    # Initialize variables to store the most frequent number and its count
    most_frequent_num = None
    max_count = 0

    # Iterate through the dictionary to find the most frequent number
    for num, count in count_dict.items():
        if count > max_count:
            most_frequent_num = num
            max_count = count

    return most_frequent_num

# Example usage
my_list = [1, 2, 3, 4, 2, 2, 3, 2, 5, 2]
print("Most frequent number:", most_frequent(my_list))
