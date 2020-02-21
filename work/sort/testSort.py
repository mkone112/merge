#помоему это тест
from merge.other2 import merge_sort as mergeSort
def sortTest(mergeSort=mergeSort):
    #лучше передавать сюда fx по названию
    from random import randrange as rand
    for i in range(10):
        d = -30,30
        L = [rand(*d) for i in range(rand(*d))]
        assert mergeSort(L) == sorted(L)
    return 'passed'

# from merge.work.sort.iterable_mergeSort import mergeSort
# print(sortTest())
# from merge.work.sort.recursive_mergeSort import merge_sort as mergeSort
# print(sortTest())
# from merge.functional_merge_sort import mergesort as mergeSort
# print(sortTest())
print(sortTest())