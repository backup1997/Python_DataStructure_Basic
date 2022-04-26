from node import DoubleNode


class DoubleList:
    def __init__(self):
        self.items = []
        self.head = None

    def add(self, item):  # 新节点加到首部
        add_node = DoubleNode(item)
        current_head = self.head
        if current_head is None:  # 当前双向链表为空
            self.head = add_node
        else:
            add_node.next = current_head
            current_head.prior = add_node
            self.head = add_node

    def search(self, item):
        current_node = self.head
        found = False
        while current_node != None and not found:  # 注意是对current_node进行判断！
            if current_node.getData() == item:
                found = True
            current_node = current_node.getNext()
        return found

    def remove(self, item):  # 假设item肯定在链表里
        if self.head.getData() == item:
            self.head = None
            return
        current_node = self.head
        while current_node.getData() != item:
            current_node = current_node.getNext()
        if current_node.getNext() is None:  # 到最后一个节点了
            current_node.getPrior().setNext(None)
        else:
            current_node.getNext().setPrior(current_node.getPrior())
            current_node.getPrior().setNext(current_node.getNext())

    def size(self):
        count = 0
        current_node = self.head
        while current_node is not None:
            count = count + 1
            current_node = current_node.getNext()
        return count

doubleList = DoubleList()
doubleList.add("2")
doubleList.add("Tom")
doubleList.add(True)
print(doubleList.size())
print(doubleList.search("Tom"))
doubleList.remove("Tom")
print(doubleList.size())
print(doubleList.search("2"))
print(doubleList.search(True))
