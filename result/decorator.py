def merge(arr, left, mid, right):
    left_part = arr[left:mid + 1]
    right_part = arr[mid + 1:right + 1]
    # цикл построен таким образом что при один из счетчиков достигает out of range за шаг до конца цикла
    # дополнительный эл-т в конце решает эту проблему
    left_part.append(float('inf'))
    right_part.append(float('inf'))
    i = j = 0
    for k in range(left, right + 1):
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1

#инициализация fx на первом шаге
def init_func(function):
    '''
    возвращаем функцию которая либо вызывает merge_sort(seq, len(seq) - 1) либо merge_sort
    с переданными параметрами, а в конце возвращает (что?)
    :param function:
    :return:
    '''
    def wrapper(*args):
        a = []
        if len(args) == 1:
            a = args[0]
            function(a, 0, len(a) - 1)
        else:
            function(*args)
        return a

    return wrapper

@init_func
def merge_sort(seq, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(seq, left, mid)
        merge_sort(seq, mid + 1, right)
        merge(seq, left, mid, right)
if __name__ == "__main__":
    test = [5, 4, 3, 2, 1]
    print(merge_sort(test))