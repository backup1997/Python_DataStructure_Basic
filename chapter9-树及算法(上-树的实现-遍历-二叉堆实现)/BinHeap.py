import random


class BinHeap:
    def __init__(self):
        self.heaplist = [0]
        self.currentSize = 0

    # 小根堆，小的数上浮
    def percUp(self, i):
        if i // 2 > 0:
            if self.heaplist[i] < self.heaplist[i // 2]:
                tmp = self.heaplist[i // 2]
                # 与父节点交换
                self.heaplist[i // 2] = self.heaplist[i]
                self.heaplist[i] = tmp
            i = i // 2  # 沿路径向上

    def insert(self, key):
        self.heaplist.append(key)  # 添加到末尾
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)  # 新key上浮

    # 如下自己实现的存在错误，没有保证i没有超出节点范围限制
    # def percDown(self, i):
    #     while self.heaplist[i] < min(self.heaplist[2 * i], self.heaplist[2 * i + 1]):
    #         if self.heaplist[2 * i] < self.heaplist[2 * i + 1]:
    #             temp = self.heaplist[i]
    #             self.heaplist[i] = self.heaplist[2 * i]
    #             self.heaplist[2 * i] = temp
    #             i = 2 * i
    #         else:
    #             temp = self.heaplist[i]
    #             self.heaplist[i] = self.heaplist[2 * i + 1]
    #             self.heaplist[2 * i + 1] = temp
    #             i = 2 * i + 1

    def percDown(self, i):
        while (2 * i) <= self.currentSize:
            minchild = self.minChild(i)
            # 如果父节点比子节点大，交换下沉
            if self.heaplist[i] > self.heaplist[minchild]:
                # 交换下沉
                tmp = self.heaplist[i]
                self.heaplist[i] = self.heaplist[minchild]
                self.heaplist[minchild] = tmp
            i = minchild  # 沿路径向下

    # 返回两个子节点中最小值的下标，如果只有一个子节点，则返回它即可
    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:  # 只有一个子节点
            return i * 2
        else:  # 返回较小的
            if self.heaplist[2 * i] < self.heaplist[2 * i + 1]:
                return i * 2
            else:
                return i * 2 + 1

    # 小根堆，移走最小的，要拿最大的替补
    def delMin(self):
        min = self.heaplist[1]  # 移走堆顶
        self.heaplist[1] = self.heaplist[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.percDown(1)  # 新顶下沉
        self.heaplist.pop()
        return min

    # 由无序表alist建小根堆
    def buildHeap(self, alist):
        start = len(alist) // 2
        self.currentSize = len(alist)
        self.heaplist = [0] + alist[:]
        while start > 0:
            print(self.heaplist, start)
            self.percDown(start)
            start = start - 1
        print(self.heaplist, start)


minheap = BinHeap()
alist = []
for i in range(100):
    alist.append(random.randint(1, 100))
minheap.buildHeap(alist)
