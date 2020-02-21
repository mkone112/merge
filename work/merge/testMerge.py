from merge.work.merge.merge_for import merge
from merge.work.merge.merge_while import merge
def testMerge(n):
    from random import randrange as rand
    for i in range(n):
        d = -200,200
        L = [rand(*d) for i in range(10)]

        mid = len(L)//2
        a,b = sorted(L[mid:]),sorted(L[:mid])
        assert merge(a,b) == sorted(L)
    return 'passed'
print(testMerge(10))