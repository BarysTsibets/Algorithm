def binary_search(new_list, item):
    low = 0
    high = len(new_list)-1

    while low <= high:
        mid = int((low + high)/2)
        guess = new_list[mid]
        if guess == item:
            return mid
        if item < guess:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_list = [1,3,5,7,9]
print(binary_search(my_list, 5))

print(int(3/2))