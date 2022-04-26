def mergeSort(alist):
    # 当len(alist)=1时什么也不做，是基本结束条件
    if len(alist) > 1:
        mid = len(alist) // 2
        left = alist[:mid]
        right = alist[mid:]
        mergeSort(left)  # 递归调用自身
        mergeSort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            # 拉链式交错，把左右部分从小到大归并到结果列表中
            if left[i] < right[j]:
                alist[k] = left[i]
                i = i + 1
            else:
                alist[k] = right[j]
                j = j + 1
            k = k + 1
        while i < len(left):  # 归并左半部分剩余项
            alist[k] = left[i]
            k = k + 1
            i = i + 1
        while j < len(right):  # 归并右半部分剩余项目
            alist[k] = right[j]
            k = k + 1
            j = j + 1
        return alist

# 下面是更加Python化的归并排序
def merge_sort(alist):
    # 递归结束条件
    if len(alist)<=1:
        return alist
    # 分解问题，并递归调用
    mid=len(alist)//2
    left=alist[:mid]
    right=alist[mid:]
    left=mergeSort(left)  # 左半部分排好序
    right=mergeSort(right)  # 右半部分排好序
    # 合并左右半部，完成排序
    merged=[]
    while left and right:
        if left[0]<right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))
    if left:
        merged=merged+left
    else:
        merged=merged+right
    # 如上的if else判断可以整体合并为一行
    # merged.extend(right if right else left)
    # extend表示列表间的合并
    return merged

testlist=[4,5,7,0,1,11,41,51]
print(mergeSort(testlist))
testlist=[4,15,7,44,13,11,41,51]
print(merge_sort(testlist))
