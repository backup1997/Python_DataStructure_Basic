def bubbleSort(alist):
    for i in range(len(alist) - 1):
        for j in range(len(alist) - i - 1):  # 趟数是n-1一直到1
            if alist[j] > alist[j + 1]:
                t = alist[j]
                alist[j] = alist[j + 1]
                alist[j + 1] = t
                # Python语言支持直接交换alist[i],alist[i+1]=alist[i+1],alist[i]
    return alist


testlist = [11, 5, 4464, 66, 44, 33]
print(bubbleSort(testlist))
