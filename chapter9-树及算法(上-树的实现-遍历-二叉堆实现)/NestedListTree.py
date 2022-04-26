def BinaryTree(r):
    return [r, [], []]


def insertLeft(root, newBranch):
    t = root.pop(1)  # 把左子树pop出来到t
    if len(t) > 1:  # 左子树有子树，用t构造一个新的子树
        root.insert(1, [newBranch, t, []])
    else:  # 左子树没有子树，不用拷贝，构造一个[newBranch,[],[]]的树作为左子树
        root.insert(1, [newBranch, [], []])
    return root


def insertRight(root, newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [newBranch, [], t])
    else:
        root.insert(2, [newBranch, [], []])
    return root


def getRootVal(root):
    return root[0]


def setRootVal(root, newVal):
    root[0] = newVal


def getLeftChild(root):
    return root[1]


def getRightChild(root):
    return root[2]
