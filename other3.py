def merge2(array1, array2):
    inv = 0
    merged_array = []
    while array1 or array2:
        if not array1:
            merged_array.append(array2.pop())
        elif (not array2) or array1[-1] > array2[-1]:
            merged_array.append(array1.pop())
            inv += len(array2)
        else:
            merged_array.append(array2.pop())
    merged_array.reverse()
    return merged_array, inv

def _merge_sort(list, merge):
    len_list = len(list)
    if len_list < 2:
        return list, 0
    middle = len_list / 2
    left, left_inv   = _merge_sort(list[:middle], merge)
    right, right_inv = _merge_sort(list[middle:], merge)
    l, merge_inv = merge(left, right)
    inv = left_inv + right_inv + merge_inv
    return l, inv

#or
def merge3(left, right):
    i = j = inv = 0
    merged = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            inv += len(left) - i

    merged += left[i:]
    merged += right[j:]
    return merged, inv