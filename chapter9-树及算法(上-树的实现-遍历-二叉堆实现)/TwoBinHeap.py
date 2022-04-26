import random


class BinHeap:
    def __init__(self, f=None):
        self.heaplist = [0]
        self.currentSize = 0
        if f is None:  # 如果不传比较函数，默认建立大根堆
            def f(a, b):
                return a > b

            self.fun = f
        else:
            self.fun = f

    def default_fun(self, a, b):
        return a > b

    # 根据fun，建立大根堆/小根堆，进行上浮
    def percUp(self, i):
        if i // 2 > 0:
            if self.fun(self.heaplist[i], self.heaplist[i // 2]):
                tmp = self.heaplist[i // 2]
                # 与父节点交换
                self.heaplist[i // 2] = self.heaplist[i]
                self.heaplist[i] = tmp
            i = i // 2  # 沿路径向上

    def insert(self, key):
        self.heaplist.append(key)  # 添加到末尾
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)  # 新key上浮

    def percDown(self, i):
        while (2 * i) <= self.currentSize:
            # 只有一个节点
            if 2 * i + 1 > self.currentSize:
                child = 2 * i
            else:
                if self.fun(self.heaplist[2 * i], self.heaplist[2 * i + 1]):
                    child = 2 * i
                else:
                    child = 2 * i + 1
            # 按照fun，交换下沉
            if self.fun(self.heaplist[child], self.heaplist[i]):
                # 交换下沉
                tmp = self.heaplist[i]
                self.heaplist[i] = self.heaplist[child]
                self.heaplist[child] = tmp
            i = child  # 沿路径向下

    # 小根堆，移走最小的，要拿最大的替补
    def delMin(self):
        min = self.heaplist[1]  # 移走堆顶
        self.heaplist[1] = self.heaplist[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.percDown(1)  # 新顶下沉
        self.heaplist.pop()
        return min

    # 由无序表alist建堆，使用的是下沉法
    def buildHeap(self, alist):
        start = len(alist) // 2
        self.currentSize = len(alist)
        self.heaplist = [0] + alist[:]
        while start > 0:
            print(self.heaplist, start)
            self.percDown(start)
            start = start - 1
        print(self.heaplist, start)

    # 上浮法建堆
    def buildHeapUp(self, alist):
        start = len(alist)
        self.currentSize = len(alist)
        self.heaplist = [0] + alist[:]
        while start > 0:
            print(self.heaplist, start)
            self.percUp(start)
            start = start - 1

    def heapSort(self, alist):
        self.heaplist = alist
        sorted_list = []
        for i in range(len(alist), 0, -1):
            self.buildHeapUp(self.heaplist[:i + 1])
            self.heaplist[1], self.heaplist[i] = self.heaplist[i], self.heaplist[1]
            sorted_list.append(self.heaplist.pop())
            self.heaplist.pop(0)  # 每轮过后要把0元素pop出来修正，才能继续调用buildHeap
        print("after heapSort==>")
        print(sorted_list)
        return sorted_list


def fun(a, b):
    """
    大于则建立大根堆，小于则建立小根堆
    通过影响上浮和下沉的比较来影响建堆过程
    >则上浮时当子节点大于父节点，才交换。下沉时，当子节点大于父节点才下沉交换
    <则上浮时当子节点小于父节点，才上浮。下沉时，当子节点小于父节点才下沉交换
    """
    return a < b


minheap = BinHeap(fun)
alist = []
for i in range(9):
    alist.append(random.randint(1, 100))
minheap.buildHeapUp(alist)
minheap.heapSort(alist)
