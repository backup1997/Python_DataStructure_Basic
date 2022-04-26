def shellSort(alist):
    sublistcount = len(alist) // 2  # 间隔设定
    while sublistcount > 0:
        for start in range(sublistcount):  # 间隔长度=子列表个数
            # 有多少子列表，就会在for中调用多少次gapInsertSort
            gapInsertSort(alist, start, sublistcount)  # 子列表排序
        print("After increments of size", sublistcount, "The list is", alist)
        sublistcount = sublistcount // 2  # 间隔缩小


def gapInsertSort(alist, start, gap):
    """
    带间隔的插入排序
    :param alist: 待排序列
    :param start: 起始
    :param gap: 间隔
    """
    for i in range(start + gap, len(alist), gap):
        currentvalue = alist[i]
        position = i
        while position >= gap and alist[position - gap] > currentvalue:
            alist[position] = alist[position - gap]
            position = position - gap  # 变成了减去间隔
        alist[position] = currentvalue
