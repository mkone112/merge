def merge(seq, left, mid, right):
    mid += 1; right += 1
    left_part = seq[left:mid]
    right_part = seq[mid:right]
    left_part.append(float('inf'))
    right_part.append(float('inf'))
    left_part, right_part = iter(left_part), iter(right_part)
    left_elt, right_elt = next(left_part), next(right_part)
    for k in range(left, right):
        if left_elt <= right_elt:
            seq[k] = left_elt
            left_elt = next(left_part)
        else:
            seq[k] = right_elt
            right_elt = next(right_part)

def merge_sort(seq, left=None, right=None):
    if left is None and right is None:
        left = 0
        right = len(seq) - 1
    # splitting while arr[left:right]
    if left < right:
        mid = (left + right) // 2
        merge_sort(seq, left, mid)
        merge_sort(seq, mid + 1, right)
        merge(seq, left, mid, right)
    return seq

print(merge_sort([5, 4, 3, 2, 1]))