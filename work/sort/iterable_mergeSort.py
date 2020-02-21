#полностью работает
def mergeSort(seq):
    if not seq: return seq
    from merge.work.merge.merge_for import merge
    seq = [[i] for i in seq]
    while len(seq) > 1:     #при != сломается на пустом массиве
        for i in range(0,len(seq)//2):
            #сливаем по два
            seq[i:i+2] = [merge(seq[i], seq[i+1])]
    return seq[0]