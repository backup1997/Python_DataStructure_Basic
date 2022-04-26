from node import Node
class OrderedList:
    def __init__(self):
        self.head=None
        self.function=None #定义从小到大?


    def size(self):
        count=0
        current_node=self.head
        while current_node is not  None:
            count=count+1
            current_node=current_node.getNext()
        return count

    def search(self,item):
        current=self.head
        found=False
        stop=False #相比于无序表，添加了这个stop标志
        while current!=None and not found and not stop:
            if current.getData()==item:
                found=True
            else:
                if current.getData()>item:
                    stop=True
                else:
                    current=current.getNext()
        return found

    def add(self,item): #总体思想，找到第一个比item大的节点，将item插入它的前面
        newNode=Node(item)
        if self.head is None:
            self.head=newNode
            return
        previous=None
        current_node=self.head
        while current_node!=None and item>current_node.getData():
            previous=current_node
            current_node=current_node.getNext()
        if current_node is None:
            previous.setNext(newNode)
        else:
            if previous is None:
                self.head=newNode
                newNode.setNext(current_node)
            else:
                newNode.setNext(current_node)
                previous.setNext(current_node)

    def add_tech(self,item):
        """
        老师讲的add方法，依旧是先找位置，然后插入
        找位置：当前节点不为none且not stop
        插入：插在表头，插在中间
        :param item:
        :return:
        """
        current=self.head
        previous=None
        stop=False
        while current is not None and not stop: #发现插入位置
            if current.getData()>item:
                stop=True
            else:
                previous=current
                current=current.getNext()
        temp=Node(item)
        if previous is None: #插在表头
            temp.setNext(self.head)
            self.head=temp
        else: #插在表中
            previous.setNext(temp)
            temp.setNext(current)