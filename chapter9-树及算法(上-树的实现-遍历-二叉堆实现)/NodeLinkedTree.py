class BinaryTree:
    def __init__(self, rootObject):
        self.key = rootObject
        self.left = None
        self.right = None

    def insertLeft(self, newNode):
        if self.left is None:
            self.left = BinaryTree(newNode)
        else:
            temp = BinaryTree(newNode) # 先将插入的值实例化一个树
            temp.left = self.left #将原来的树挂在这个实例化的树上
            self.left = temp #将实例化的树挂在原来的根上

    def insertRight(self, newNode):
        if self.right is None:
            self.right = BinaryTree(newNode)
        else:
            temp = BinaryTree(newNode)
            temp.right = self.right
            self.right = temp

    def getRightChild(self):
        return self.right

    def getLeftChild(self):
        return self.left

    def setRootVal(self, value):
        self.key = value

    def getRootVal(self):
        return self.key

    def preorder(self):
        print(self.key)
        if self.left:
            self.left.preorder() # 也进行递归
        if self.right:
            self.right.preorder()

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.key)
        if self.right:
            self.right.inorder()

r = BinaryTree('a')
r.insertLeft('b')
r.insertRight('c')
r.getRightChild().setRootVal('hello')
r.getLeftChild().setRootVal('d')
