from node import Node


class UnorderedList:
    def __init__(self):
        self.head = None
        self.next = None

    def isEmpty(self):
        return self.head == None

    def addnode(self, newNode):  # 也可以添加数据
        head_old = self.head
        newNode.next = head_old  # 对self.next进行赋值和使用self.setNext()是一样的
        self.head = newNode

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        count = 0
        current_node = self.head
        while current_node != None:
            count = count + 1
            current_node = current_node.getNext()
        return count

    def search(self, item):
        current_node = self.head
        found = False
        while current_node is not None and not found:
            if current_node.getData() == item:
                found = True
            current_node = current_node.getNext()
        return found

    def remove(self, item):
        """
        自己实现的remove方法，只用了一个current_node。也可以维护
        两个node，一个previous一个current去实现
        """
        current_node = self.head
        remove = False
        if current_node == None:
            return remove
        if self.head.getData() == item:  # 先判断下头节点
            self.head = self.head.getNext()
            remove = True
        while current_node.getNext() != None and not remove:
            if current_node.getNext().getData() == item:
                remove = True
                current_node.setNext(current_node.getNext().getNext())
            else:
                current_node = current_node.getNext()
        return remove

    def remove_tech(self, item):  # 假设item一定存在于链表，没有返回值的remove
        previous = None
        current = self.head
        found = False  # 先循环去找，具体在哪找到，后面再删除节点或判断
        while not found:
            if current.getData() != item:
                previous = current
                current = current.getNext()
            else:
                found = True
        if current == self.head:  # 找到的是头节点
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def append(self,item):
        append_node=Node(item)
        if self.head==None:
            self.head=append_node
        current_node=self.head
        while current_node.getNext()!=None:
            current_node=current_node.getNext()
        current_node.setNext(append_node)

    def pop(self,item): #最后一个Node弹出来
        if self.head==None:
            return
        current_node=self.head
        while current_node.getNext().getNext()!=None:
            current_node=current_node.getNext()
        current_node.setNext(None)


unordered_list = UnorderedList()
unordered_list.add("2")
unordered_list.add("TOM")
unordered_list.add(True)
print(unordered_list.remove("TIM"))
print(unordered_list.size())
print(unordered_list.remove_tech("TOM"))
print(unordered_list.size())
unordered_list.append("TIM")
print(unordered_list.size())
print(unordered_list.remove("TIM"))
print(unordered_list.size())
