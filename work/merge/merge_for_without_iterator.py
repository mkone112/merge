def merge(seq0, seq1):
    result = []
    j = 0
    for element in seq0:
        while j < len(seq1) and element > seq1[j]:
            result.append(seq1[j])
            j += 1
        result.append(element)
    return result + seq1[j:]