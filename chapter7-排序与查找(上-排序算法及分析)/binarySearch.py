# 二分查找
def binarySearch(orderedlist, item):
    start = 0
    end = len(orderedlist)  # end应该为len(alist)-1
    found = False
    while start <= end and not found:
        mid = (start + end) // 2
        if orderedlist[mid] == item:
            found = True
        elif orderedlist[mid] > item:
            end = mid - 1
        else:
            start = mid + 1
    return found


# 下面是递归解法
def binarySearchUp(alist, item):
    if len(alist) == 0:  # 基本结束条件，也可以改为下面版本
        return False
    # if len(alist)==1:
    #     return alist[0]==item
    else:
        mid = (0 + len(alist) - 1) // 2
        if alist[mid] == item:
            return True
        elif alist[mid] > item:  # 缩小规模，调用自身
            return binarySearchUp(alist[:mid], item)  # 应该是mid而不是mid-1
        else:
            return binarySearchUp(alist[mid + 1:], item)


testlist = [0, 1, 4, 5, 7, 11, 41, 51]
print(binarySearch(testlist, 3))
