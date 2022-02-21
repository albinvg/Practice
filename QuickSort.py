def fnQuickSort(seq):
    if len(seq) <= 1:
        return (seq)
    else:
        smallerList = []
        greaterList = []
        pivot = seq.pop()

        for i in seq:
            if i < pivot:
                smallerList.append(i)
            else:
                greaterList.append(i)

        return fnQuickSort(smallerList) + [pivot] + fnQuickSort(greaterList)

print(fnQuickSort([3,3,5,1,8,99,3,5,2,8,0]))
