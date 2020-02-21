#работает
def merge(seq0, seq1):
    if not seq0:  return [seq1]
    if not seq1:  return [seq0]
    # l2 will contain last element.
    # иначе seq1 закончится раньше seq0
    if seq0[-1] > seq1[-1]:
        seq0, seq1 = seq1, seq0
    result = []
    seq1 = iter(seq1)
    j = next(seq1)
    # это не выйдет переписать во включения - составные операторы
    for i in seq0:
        #не удастся переписать на for т.к.
        # for будет дергать эл-т даже if его еще рано добавлять
        while j < i:
            result.append(j)
            j = next(seq1)
        result.append(i)
    result.append(j)
    result.extend(seq1)
    return result      #return result + [j] + seq1