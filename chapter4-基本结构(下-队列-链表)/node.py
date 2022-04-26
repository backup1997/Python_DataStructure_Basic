class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None  # 初始节点时设置下一个指向为None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):  # 修改值
        self.data = newdata

    def setNext(self, nextNode):
        self.next = nextNode


class DoubleNode:
    def __init__(self, item):
        self.data = item
        self.prior = None
        self.next = None

    def getData(self):
        return self.data

    def setData(self, newData):
        self.data = newData

    def getPrior(self):
        return self.prior

    def setPrior(self, priorNode):
        self.prior = priorNode

    def getNext(self):
        return self.next

    def setNext(self, nextNode):
        self.next = nextNode