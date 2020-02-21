def merge_sort(array):
    n = len(array)
    if n > 1:
        mid = n//2
        left = array[0:mid]
        right = array[mid:n]
        print(mid, left, right, array)
        merge_sort(left)
        merge_sort(right)
        merge(left, right, array)

def merge(left, right, array):
    array_length = len(array)
    right_length = len(right)
    left_length = len(left)
    left_index = right_index = 0
    for array_index in range(0, array_length):
        if right_index == right_length:
            array[array_index:array_length] = left[left_index:left_length]
            break
        elif left_index == left_length:
            array[array_index:array_length] = right[right_index:right_length]
            break
        elif left[left_index] <= right[right_index]:
                array[array_index] = left[left_index]
                left_index += 1
        else:
            array[array_index] = right[right_index]
            right_index += 1
