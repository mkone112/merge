# обычная сортировка, но с перезаписью фрагментов seq
def merge_sort(seq):
    len_seq = len(seq)
    if len_seq < 2:
        return seq
    mid = len_seq // 2
    seq[:mid] = merge_sort(seq[:mid])
    seq[mid:] = merge_sort(seq[mid:])
    return merge(seq[:mid], seq[mid:])