# огромное кол-во шагов и переменных
def merge_sort(seq):
    unit = 1        # размер блока
    # пока unit не достигнет размера массива
    while unit <= len(seq):
        h = 0   # ?
        """Inplace merge sort of array without recursive. The basic idea
        is to avoid the recursive call while using iterative solution.
        The algorithm first merge chunk of length of 2, then merge chunks
        of length 4, then 8, 16, .... , until 2^k where 2^k is large than
        the length of the array
        """
        # при этом он не объединяем последовательности в под массивы
        for h in range(0, len(seq), unit * 2):
            l, r = h, min(len(seq), h + 2 * unit)
            mid = h + unit
            # merge xs[h:h + 2 * unit]
            p, q = l, mid
            while p < mid and q < r:
                # use <= for stable merge merge
                if seq[p] <= seq[q]:
                    p += 1
                else:
                    tmp = seq[q]
                    seq[p + 1: q + 1] = seq[p:q]
                    seq[p] = tmp
                    p, mid, q = p + 1, mid + 1, q + 1
        unit *= 2
    return seq
from random import shuffle
L = [*range(10)]
shuffle(L)
print(merge_sort(L))