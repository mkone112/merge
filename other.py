'''
разобрать
'''
#очень высокая связность fx через параметры, требует передачу лишнего барахла, хотя merge явно должна просто принимать
def MERGE(A,start,mid,end):
    L = A[start:mid]
    R = A[mid:end]
    i = j = 0
    k = start
    for l in range(k,end):
        if j >= len(R) or (i < len(L) and L[i] < R[j]):
            A[l] = L[i]
            i = i + 1
        else:
            A[l] = R[j]
            j = j + 1

def mergeSort(A,p,r):
    if r - p > 1:
        mid = int((p+r)/2)
        mergeSort(A,p,mid)
        mergeSort(A,mid,r)
        MERGE(A,p,mid,r)

A  = [20, 30, 21, 15, 42, 45, 31, 0, 9]
mergeSort(A,0,len(A))
print(A)