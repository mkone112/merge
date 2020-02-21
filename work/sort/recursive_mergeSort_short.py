def mergesort(seq):
    if len(seq) < 2:
        return seq
    mid = len(seq) // 2
    # делим пока не дойдем до len_a < 2
    return merge(mergesort(seq[:mid]), mergesort(seq[mid:]))