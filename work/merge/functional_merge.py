def merge(seq0, seq1):
    if not seq0: return seq1
    if not seq1: return seq0
    return seq0[:1] + merge(seq0[1:], seq1) if seq0[0] < seq1[0] else seq1[:1] + merge(seq0, seq1[1:])
