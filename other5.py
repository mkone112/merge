def mergesort(lis):
    if len(lis) > 1:
        left, right = map(lambda l: list(reversed(mergesort(l))), (lis[::2], lis[1::2]))
        lis.clear()
        while left and right:
            lis.append(left.pop() if left[-1] < right[-1] else right.pop())
        lis.extend(left[::-1])
        lis.extend(right[::-1])
    return lis