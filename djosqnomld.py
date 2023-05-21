def binary_search(my_list, target):
    low = 0
    high = len(my_list) - 1

    while low <= high:
        mid = len(my_list) // 2

        if my_list[mid] == target:
            return True
        elif my_list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return False


def power(a, b):
    return a ** b


def bubble_sort(my_list):
    n = len(my_list)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]

    return my_list


def merge_sort(my_list):
    if len(my_list) <= 1:
        return my_list

    mid = len(my_list) // 2
    left = merge_sort(my_list[:mid])
    right = merge_sort(my_list[mid:])

    return merge(left, right)


def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def quick_sort(my_list):
    if len(my_list) <= 1:
        return my_list

    pivot = my_list[len(my_list) // 2]
    left = [x for x in my_list if x < pivot]
    middle = [x for x in my_list if x == pivot]
    right = [x for x in my_list if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


# Test binary search
print(binary_search([1, 2, 3, 5, 8], 6))  # False
print(binary_search([1, 2, 3, 5, 8], 5))  # True

# Test power calculation
print(power(3, 4))  # 81

# Test bubble sort
sample_data = [29, 13, 22, 37, 52, 49, 46, 71, 56]
print(bubble_sort(sample_data))  # [13, 22, 29, 37, 46, 49, 52, 56, 71]

# Test merge sort
sample_data = [29, 13, 22, 37, 52, 49, 46, 71, 56]
print(merge_sort(sample_data))  # [13, 22, 29, 37, 46, 49, 52, 56, 71]

# Test quick sort
sample_data = [29, 13, 22, 37, 52, 49, 46, 71, 56]
print(quick_sort(sample_data))  # [13, 22, 29, 37, 46, 49, 52, 56, 71]
