#непонятно что куда возвращать
def mergeSort(seq):
    #print('spliting', seq)
    if len(seq)>1:
        mid = len(seq) // 2
        righthalf = seq[:mid]
        lefthalf = seq[mid:]
        mergeSort(seq[:mid])
        mergeSort(seq[mid:])
        i=j=k=0
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                seq[k]=lefthalf[i]
                i=i+1
            else:
                seq[k]=righthalf[j]
                j=j+1
            k=k+1

        print(seq+lefthalf[i:] + righthalf[j:])
    #print("Merging ", seq)

seq = [54, 26, 93, 17, 77, 31, 44, 55, 20]
mergeSort(seq)
print(seq)
