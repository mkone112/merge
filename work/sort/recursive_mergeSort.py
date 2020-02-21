from merge.work.merge.merge_for import merge

def merge_sort(seq):
    len_seq = len(seq)
    if len_seq < 2:
        return seq    #раньше здесь была копия
    else:
        mid = len_seq // 2
        left = merge_sort(seq[:mid])
        right = merge_sort(seq[mid:])
        return merge(left, right)