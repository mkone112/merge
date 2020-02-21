from collections import deque

def atomize(l):
    return deque(
        map(
            lambda x: deque([x]),
            l if l is not None else []
        )
    )

def merge(l, r):
    res = deque()
    while (len(l) + len(r)) > 0:
        if len(l) < 1:
            res += r
            r = deque()
        elif len(r) < 1:
            res += l
            l = deque()
        else:
            if l[0] <= r[0]:
                res.append(l.popleft())
            else:
                res.append(r.popleft())
    return res

def iter_merge_sort(l):
    atoms = atomize(l) # O(n)
    while len(atoms) > 1: # O(n - 1)
        atoms.append(merge(atoms.popleft(), atoms.popleft()))
    return list(atoms[0])