def selectionSort(alist):
    for i in range(len(alist) - 1):
        maxLocation = 0
        max = 0
        for j in range(len(alist) - i):
            if alist[j] > max:
                maxLocation = j
                max = alist[j]
        temp = max
        alist[maxLocation] = alist[len(alist) - i - 1]
        alist[len(alist) - i - 1] = temp
    return alist


testlist = [11, 5, 4464, 66, 44, 33]
print(selectionSort(testlist))
