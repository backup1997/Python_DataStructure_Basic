from graph import Graph
from graph import Vertex


class PriorityQueue:
    # 这个二叉堆的实现采用键值对，key value key是一个数字,value是真正有意义的内容
    # 我们将假设所有的键都是可比较的
    def __init__(self):
        blankVert = Vertex(0)
        self.heapArray = [(0, blankVert)]
        self.currentSize = 0

    def isEmpty(self):
        return self.currentSize == 0

    def add(self, k):
        self.heapArray.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    # 小根堆，小的数上浮
    def percUp(self, i):
        if i // 2 > 0:
            if self.heapArray[i][0] < self.heapArray[i // 2][0]:
                tmp = self.heapArray[i // 2]
                # 与父节点交换
                self.heapArray[i // 2] = self.heapArray[i]
                self.heapArray[i] = tmp
            i = i // 2  # 沿路径向上

    def insert(self, key):
        self.heapArray.append(key)  # 添加到末尾
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)  # 新key上浮

    def percDown(self, i):
        while (2 * i) <= self.currentSize:
            minchild = self.minChild(i)
            # 如果父节点比子节点大，交换下沉
            if self.heapArray[i][0] > self.heapArray[minchild][0]:
                # 交换下沉
                tmp = self.heapArray[i]
                self.heapArray[i] = self.heapArray[minchild]
                self.heapArray[minchild] = tmp
            i = minchild  # 沿路径向下

    # 返回两个子节点中最小值的下标，如果只有一个子节点，则返回它即可
    def minChild(self, i):
        if i * 2 > self.currentSize:
            return -1
        else:
            if i * 2 + 1 > self.currentSize:  # 只有一个子节点
                return i * 2
            else:  # 返回较小的
                if self.heapArray[2 * i][0] < self.heapArray[2 * i + 1][0]:
                    return i * 2
                else:
                    return i * 2 + 1

    # 小根堆，移走最小的，要拿最大的替补
    def delMin(self):
        retval = self.heapArray[1][1]  # 移走堆顶
        self.heapArray[1] = self.heapArray[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapArray.pop()
        self.percDown(1)  # 新顶下沉
        return retval

    # 由无序表alist建小根堆
    def buildHeap(self, alist):
        start = len(alist) // 2
        self.currentSize = len(alist)
        self.heapArray = [(0, 0)] + alist[:]
        while start > 0:
            print(self.heapArray, start)
            self.percDown(start)
            start = start - 1
        print(self.heapArray, start)

    def dicreaseKey(self, val, amt):
        # this is a little wierd, but we need to find the heap thing to decrease by
        # looking at its value
        done = False
        i = 1
        myKey = 0
        while not done and i <= self.currentSize:
            if self.heapArray[i][1] == val:
                done = True
                myKey = i
            else:
                i = i + 1
        if myKey > 0:
            self.heapArray[myKey] = (amt, self.heapArray[myKey][1])
            self.percUp(myKey)


import sys


def prim(G: Graph, start: Vertex):
    pq = PriorityQueue()
    for v in G:
        v.setDistance(sys.maxsize)
        v.setPred(None)
    start.setDistance(0)
    pq.buildHeap([(v.getDistance(), v) for v in G])
    while not pq.isEmpty():
        currentVert = pq.delMin()
        for nextVert in currentVert.getConnections():  # 跟现有节点相连的所有其他节点
            newCost = currentVert.getWeight(nextVert)
            # 需要在优先队列里，也即不在生成树中，安全添加
            if nextVert in pq and newCost < nextVert.getDistance():
                nextVert.setPred(currentVert)
                nextVert.setDistance(newCost)
                pq.dicreaseKey(nextVert, newCost)
