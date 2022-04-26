class Node:
    def  __init__(self,item):
        self.data=item
        self.next=None
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self,item):
        self.data=item
    def setNext(self,nextNode):
        self.next=nextNode

class Chain:
    def __init__(self):
        self.head=None

    def size(self):
        current_node=self.head
        count=0
        while current_node:
            count=count+1
            current_node=current_node.getNext()
        return count

    def add(self,item):
        newNode=Node(item)
        if self.head is None:
            self.head=newNode
            return
        if not self.search(item):
            current_node=self.head
            while current_node.getNext() is not None:
                current_node=current_node.getNext()
            current_node.setNext(newNode)

    def search(self,item):
        current_node=self.head
        found=False
        while current_node is not None and not found:
            if current_node.getData()==item:
                found=True
            else:
                current_node=current_node.getNext()
        return found

def squareHash(num,hashtable):
    base=len(hashtable)
    square_num=num*num
    str_num=str(square_num)
    mid=len(str_num)//2
    hashvalue=(int(str_num[mid])*10+int(str_num[mid+1]))%base
    hashtable[hashvalue].add(num)  # 无论是不是空，都可以加到链表上去
    return hashtable

hashtable=[Chain()]*10
squareHash(122,hashtable)
squareHash(133,hashtable)
squareHash(123,hashtable)
squareHash(133,hashtable)
squareHash(123,hashtable)