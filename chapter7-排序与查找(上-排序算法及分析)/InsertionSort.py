def insertSort(alist):
    # sortedlist=[] #不用新的列表，对原来的列表从前往后遍历即可
    for index in range(1, len(alist)):
        currentvalue = alist[index]  # 新项/插入项
        position = index  # 从index开始往前
        while position > 0 and alist[position - 1] > currentvalue:
            alist[position] = alist[position - 1]
            position = position - 1  # 比对，移动
        alist[position] = currentvalue  # position记录着应当插入的位置，插入新项
