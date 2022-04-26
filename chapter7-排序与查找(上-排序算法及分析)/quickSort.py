def quickSort(alist):
    quickSorthelper(alist,0,len(alist)-1)

def quickSorthelper(alist,first,last):
    if first<last:  # 基本结束条件
        splitpoint=partition(alist,first,last)  # 分裂
        quickSorthelper(alist,first,splitpoint-1)  # 递归调用自身
        quickSorthelper(alist,splitpoint+1,last)

def partition(alist,first,last):
    pivotvalue=alist[first]  # 选定中值
    leftmark=first+1  # 左右标初值
    rightmark=last

    done=False
    while not done:
        # 先向右移动左标
        while leftmark<=rightmark and alist[leftmark]<=pivotvalue:
            leftmark=leftmark+1
        # 再向左移动右标
        while leftmark<=rightmark and pivotvalue<=alist[rightmark]:
            rightmark=rightmark-1
        # 两标相错就结束移动
        if rightmark<leftmark:
            done=True
        else: # 没有结束，则交换左右标的值
            temp=alist[leftmark]
            alist[leftmark]=alist[rightmark]
            alist[rightmark]=temp
    # 结束移动了，中值应该到rightmark的位置，交换
    temp=alist[first]
    alist[first]=alist[rightmark]
    alist[rightmark]=temp

    return rightmark  # 返回中值点，也就是分裂点