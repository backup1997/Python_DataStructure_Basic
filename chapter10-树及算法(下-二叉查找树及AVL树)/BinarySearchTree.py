class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0
        self.balanceFactor = 0

    def length(self):
        return self.size

    # 如果定义了下面这个内置的Python函数len，则可以len()
    def __len__(self):
        return self.size

    # 只要定义了这个iter这个特殊方法，即可用for node in BST这个方法
    def __iter__(self):
        return self.root.__iter__()

    def put(self, key, val):
        if self.root:  # root存在，不控的BST，调用递归，在为根节点的子树上插入key
            self._put(key, val, self.root)
        else:  # root不存在，构造单个节点的二叉查找树
            self.root = TreeNode(key, val)
        self.size = self.size + 1

    def _put(self, key, val, currentNode):
        # 递归寻找合适的插入位置，当且仅当是None，才可以挂在上面
        if key < currentNode.key:  # 如果key比currentNode小，则put到左子树，但如果没有左子树，则key成为左子节点
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)  # 递归左子树
            else:  # 寻找到了可以插入的空的左子树
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
                self.updateBalance(currentNode.leftChild)
        else:  # 如果key比currentNode大，则put到右子树。但如果没有右子树，则key成为右子节点
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChlid)  # 递归右子树
            else:  # 寻找到了可以插入的空的右子树
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)
                self.updateBalance(currentNode.rightChild)

    def updateBalance(self, currentNode):
        # 重新平衡
        if currentNode.balanceFactor > 1 or currentNode.baanceFactor < -1:
            self.rebalance(currentNode)
            return
        # 因为插入新节点，要调整父节点平衡因子
        if currentNode.parent != None:
            if currentNode.isLeftChild():
                currentNode.parent.balanceFactor += 1
            elif currentNode.isRightChild():
                currentNode.parent.balanceFactor -= 1
            # 调整完父节点平衡因子后，看是否为0，为0则不用再往上调整，否则递归网上调整
            if currentNode.parent.balanceFactor != 0:
                self.updateBalance(currentNode.parent)  # 递归调整父节点因子

    def rebalance(self, currentNode):
        if currentNode.balanceFactor < 0:  # 右重需要左旋
            # 实施左旋之前，检查右子节点是不是左重
            if currentNode.rightChild.balanceFactor > 0:
                # 先做一个右旋再左旋
                self.rotateRight(currentNode.rightChild)
                self.rotateLeft(currentNode)
            else:
                # 只左旋
                self.rotateLeft(currentNode)
        elif currentNode.balanceFactor > 0:  # 左重需要右旋
            # 实施右旋之前，检查左子节点是否右重
            if currentNode.leftChild.balanceFactor < 0:
                # 先左一个左旋再右旋
                self.rotateLeft(currentNode.leftChild)
                self.rotateRight(currentNode)
            else:
                # 只右旋
                self.rotateRight(currentNode)

    def rotateLeft(self, rotRoot):
        # 先取旧根的右子节点作为新根
        newRoot = rotRoot.rightChild
        # 因为新根原来是旧根的右孩子，旋转后旧根的右孩子掉了，
        # 新根的左孩子就可以挂到旧根的右孩子上，如果新根的左孩子不是None的话，
        # 还要修改其向上指向，到旧根。
        rotRoot.rightChild = newRoot.leftChild
        if newRoot.leftChild:
            newRoot.leftChild.parent = rotRoot
        # 接着修改新根的父节点
        newRoot.parent = rotRoot.parent
        # 旧根是不是树根，如果是树根，则新根设为树根
        if rotRoot.isRoot():
            self.root = newRoot
        else:
            # 如果旧根是左/右子树，则修改父节点的向下指向
            if rotRoot.isLeftChild():
                rotRoot.parent.leftChild = newRoot
            else:
                rotRoot.parent.rightChild = newRoot
        # 设置旧根为新根的左孩子，新根为旧根的父亲，即修改向下指向旧根和旧根的向上指向
        newRoot.leftChild = rotRoot
        rotRoot.parent = newRoot
        # 仅有两个节点需要调整因子
        # 修改旧根和新根的平衡因子balanceFactor
        rotRoot.balanceFactor = rotRoot.balanceFactor + \
                                1 - min(newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.balanceFactor + \
                                1 + max(rotRoot.balanceFactor, 0)

    def rotateRight(self,rotRoot):
        newRoot=rotRoot.leftChild
        rotRoot.leftChild=newRoot.rightChild
        if newRoot.rightChild:
            newRoot.rightChild.parent=rotRoot
        newRoot.parent=rotRoot.parent
        if rotRoot.isRoot():
            self.root=newRoot
        else:
            if rotRoot.isLeftChild():
                rotRoot.parent.leftChild=newRoot
            else:
                rotRoot.parent.rightChild=newRoot
        newRoot.rightChild=rotRoot
        rotRoot.parent=newRoot
        rotRoot.balanceFactor = rotRoot.balanceFactor + \
                                1 - min(newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.balanceFactor + \
                                1 + max(rotRoot.balanceFactor, 0)


    def __setitem__(self, key, value):
        self.put(key, value)

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)  # 取key的节点
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    # 返回的是Node
    def _get(self, key, currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif currentNode.key > key:  # 要找的key<currentNode.key，到左子树里找
            return self._get(key, currentNode.getLeftChild())
        else:  # 要找的key>currentNode.key,到右子树里找
            return self._get(key, currentNode.getRightChild())

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False

    def delete(self, key):
        if self.size > 1:
            # 先通过_get找到要删除的节点
            nodeToRemove = self._get(key, self.root)
            # 如果能找到，调用remove删除
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size = self.size - 1
            else:
                raise KeyError('Error,key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError('Error,key not in tree')

    def remove(self, currentNode):
        if currentNode.isLeaf():  # 要删除的节点是一个叶子节点
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None
        else:  # 要删除的节点有孩子
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():  # 本身是左子节点，有一个左子节点，进行删除
                    currentNode.leftChild.parent = currentNode.parent  # 向上指的指针赋值
                    currentNode.parent.leftChild = currentNode.leftChild  # 向下指的指针修改，反过来的话就错了
                elif currentNode.isRighChild():  # 本身是右子节点，有一个左子节点，进行删除
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                else:  # 本身是根节点，有一个左子节点，进行删除
                    currentNode.replaceNodeData(currentNode.leftChild.key,
                                                currentNode.leftChild.payload,
                                                currentNode.leftChild.leftChild,
                                                currentNode.leftChild.rightChild)
            else:
                if currentNode.isLeftChild():  # 本身是左子节点，有唯一的右子节点，进行删除
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild
                elif currentNode.isRightChild():  # 本身是右子节点，有唯一的左子节点，进行删除
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                else:  # 还是一个根节点
                    currentNode.replaceNodeData(currentNode.rightChild.key,
                                                currentNode.rightChild.payload,
                                                currentNode.rightChild.leftChild,
                                                currentNode.rightChild.rightChild)


class TreeNode:
    def __init__(self, key, val, left=None,
                 right=None, parent=None):
        self.key = key  # 键值
        self.payload = val  # 数据项
        self.leftChild = left  # 左右子节点
        self.rightChild = right
        # 根据在表达式解析时需要额外的栈保存父节点
        # 这里使用parent来方便回溯
        self.parent = parent  # 父节点

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    # 判断treeNode是不是左节点
    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    # 判断treeNode是不是右节点
    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    # 没有父节点就是根节点
    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not self.leftChild and not self.rightChild

    def hasAnyChildren(self):
        return self.leftChild or self.rightChild

    def hasBothChildren(self):
        return self.leftChild and self.rightChild

    def replaceNodeData(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

    def __iter__(self):
        if self:  # 如果根不为空，递归的基本结束条件
            if self.hasLeftChild():
                for elem in self.leftChild:  # for in应该是用一个迭代器，for in 是一个递归调用。
                    yield elem
            yield self.key  # 取完左子树，取根
            if self.hasRightChild():
                for elem in self.rightChild:  # 取右子树
                    yield elem

    # 寻找被摘出来后，应该替补的后继节点，即右子树中最左下角的节点。
    def findSuccessor(self):
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findMin()  # 到右子节点中找最小的节点
        else:  # 目前用不到下面代码，已经假设了会有右子节点
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent
                else:
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self
        return succ

    # 根据给出的根self，找其下的最小节点，即循环往左下找
    def findMin(self):
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current

    # 摘出节点spliceOut()
    def spliceOut(self):
        if self.isLeaf():  # 摘出叶节点
            # 如果叶节点是左节点，则赋值父亲的左子节点为空，表示摘出来
            if self.isLeftChild():
                self.parent.leftChild = None
            # # 如果叶节点是右节点，则赋值父亲的右子节点为空，表示摘出来
            else:
                self.parent.rightChild = None
        elif self.hasAnyChildren():
            # 要摘除节点有左子节点，摘出来。但目前不会遇到
            if self.hasLeftChild():
                if self.isLeaf():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else:  # 摘出来带右子节点的节点
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent
